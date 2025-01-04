from pathfinding import PathFinding
from visualization import visualize_path

def main():
    start = (0, 0)  # Example starting point
    goal = (0, 4)   # Example goal point
    grid = [
        ['S', '.', '.', 'X', 'G'],
        ['.', 'X', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', '.', '.']
    ]
    pathfinder = PathFinding(start, goal, grid)

    # Test BFS
    bfs_metrics = pathfinder.run_with_metrics('bfs')
    if bfs_metrics['path']:
        visualize_path(grid, bfs_metrics['path'], "BFS")
    else:
        print("No path found using BFS")

    # Test DFS
    dfs_metrics = pathfinder.run_with_metrics('dfs')
    if dfs_metrics['path']:
        visualize_path(grid, dfs_metrics['path'], "DFS")
    else:
        print("No path found using DFS")

    # Test A*
    astar_metrics = pathfinder.run_with_metrics('astar')
    if astar_metrics['path']:
        visualize_path(grid, astar_metrics['path'], "A*")
    else:
        print("No path found using A*")

    # Print metrics
    print("\nMetrics Summary:")
    for algo, metrics in [("BFS", bfs_metrics), ("DFS", dfs_metrics), ("A*", astar_metrics)]:
        print(f"\nAlgorithm: {algo}")
        print(f"  Execution Time: {metrics['execution_time']:.6f} seconds")
        print(f"  Memory Usage: {metrics['memory_usage']:.2f} MB")
        print(f"  Nodes Expanded: {metrics['nodes_expanded']}")
        print(f"  Path: {metrics['path']}")

if __name__ == "__main__":
    main() 