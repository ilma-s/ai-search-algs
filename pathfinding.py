from collections import deque
import heapq
from math import sqrt
import time
from memory_profiler import memory_usage 

class PathFinding:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # find start and goal positions
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 'S':
                    self.start = (i, j)
                elif grid[i][j] == 'G':
                    self.goal = (i, j)
        self.nodes_expanded = 0  # counter for nodes expanded

    def get_neighbors(self, pos):
        """Returns valid neighboring positions"""
        row, col = pos
        # define possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            # check if position is valid and not a wall
            if (0 <= new_row < self.rows and 
                0 <= new_col < self.cols and 
                self.grid[new_row][new_col] != 'X'):
                neighbors.append((new_row, new_col))
        self.nodes_expanded += 1  # increment counter when expanding nodes
        print(f"\rNodes expanded: {self.nodes_expanded}", end="")  # show real-time node expansion
        return neighbors

    def bfs(self):
        """BFS: Guarantees shortest path in unweighted graph"""
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        
        while queue:
            current, path = queue.popleft()
            
            if current == self.goal:
                return path
                
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def dfs(self):
        """DFS: Finds a path, but not necessarily the shortest"""
        stack = [(self.start, [self.start])]
        visited = set()
        
        while stack:
            current, path = stack.pop()
            
            if current == self.goal:
                return path
                
            if current not in visited:
                visited.add(current)
                for neighbor in self.get_neighbors(current):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None

    def manhattan_distance(self, pos):
        """Manhattan distance heuristic"""
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def astar(self):
        """A* Search: Finds shortest path using heuristics"""
        pq = [(0, self.start, [self.start])]
        visited = set()
        g_score = {self.start: 0}
        
        while pq:
            _, current, path = heapq.heappop(pq)
            
            if current == self.goal:
                return path
                
            if current not in visited:
                visited.add(current)
                for neighbor in self.get_neighbors(current):
                    tentative_g = g_score[current] + 1
                    
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        g_score[neighbor] = tentative_g
                        heuristic = getattr(self, 'current_heuristic', self.manhattan_distance)
                        f_score = tentative_g + heuristic(neighbor)
                        heapq.heappush(pq, (f_score, neighbor, path + [neighbor]))
        return None

    def euclidean_distance(self, pos):
        """Euclidean distance heuristic"""
        return sqrt((pos[0] - self.goal[0])**2 + (pos[1] - self.goal[1])**2)


    def run_with_metrics(self, algorithm):
        """Run specified algorithm with performance metrics"""
        self.nodes_expanded = 0
        start_time = time.time()
        
        print(f"\nRunning {algorithm.upper()}...")
        print("----------------------------------------")
        
        # Run the specified algorithm
        if algorithm == 'bfs':
            path = self.bfs()
        elif algorithm == 'dfs':
            path = self.dfs()
        elif algorithm == 'astar':
            path = self.astar()
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")
        
        end_time = time.time()
        execution_time = end_time - start_time
        mem_usage = memory_usage(-1, interval=0.1, timeout=1)[0]
        
        # Print metrics to console
        print(f"\nAlgorithm completed:")
        print(f"  Time taken: {execution_time:.4f}s")
        print(f"  Memory used: {mem_usage:.2f}MB")
        print(f"  Nodes expanded: {self.nodes_expanded}")
        print("----------------------------------------")
        
        return {
            'execution_time': execution_time,
            'memory_usage': mem_usage,
            'nodes_expanded': self.nodes_expanded,
            'path': path
        }

def compare_algorithms(grid, algorithms=None, heuristics=None):
    """Compare performance of different algorithms and heuristics"""
    if algorithms is None:
        algorithms = ['bfs', 'dfs', 'astar']
    if heuristics is None:
        heuristics = ['manhattan', 'euclidean']

    results = {}
    pathfinder = PathFinding(None, None, grid)  # start / goal will be found in init

    for algo in algorithms:
        results[algo] = {}
        
        # For A*, test different heuristics
        if algo == 'astar':
            for heuristic in heuristics:
                if heuristic == 'manhattan':
                    pathfinder.current_heuristic = pathfinder.manhattan_distance
                elif heuristic == 'euclidean':
                    pathfinder.current_heuristic = pathfinder.euclidean_distance
                
                metrics = pathfinder.run_with_metrics(algo)
                results[algo][heuristic] = metrics
        else:
            metrics = pathfinder.run_with_metrics(algo)
            results[algo] = metrics

    return results 