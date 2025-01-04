import matplotlib.pyplot as plt
import numpy as np

def visualize_path(grid, path, algorithm_name):
    # define colors using RGB tuples
    color_map = {
        'S': (0, 1, 0),    # start - green
        'G': (1, 0, 0),    # goal - red
        'X': (0, 0, 0),    # obstacle - black
        '.': (1, 1, 1),    # open path - white
        'P': (0, 0, 1)     # path found - blue
    }
    
    # create a color grid with RGB values
    color_grid = np.zeros((len(grid), len(grid[0]), 3))
    
    # set colors for start, goal, and obstacles
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                color_grid[i][j] = color_map['S']
            elif grid[i][j] == 'G':
                color_grid[i][j] = color_map['G']
            elif grid[i][j] == 'X':
                color_grid[i][j] = color_map['X']
            else:
                color_grid[i][j] = color_map['.']
    
    # set colors for the path found
    for pos in path:
        if grid[pos[0]][pos[1]] == '.':
            color_grid[pos[0]][pos[1]] = color_map['P']
    
    # plot the grid
    plt.figure(figsize=(8, 8))  # make the plot a square for better grid visualization
    plt.imshow(color_grid, interpolation='nearest')
    plt.title(f"Path found using {algorithm_name}")
    
    # add grid lines
    plt.grid(True, color='black', linewidth=0.5)
    plt.xticks(np.arange(-0.5, len(grid[0]), 1), [])
    plt.yticks(np.arange(-0.5, len(grid), 1), [])
    
    # ensure grid lines show up on top of the cells
    plt.gca().set_axisbelow(False)
    
    plt.show()

# demo / test path so this script can be run independently; the paths come from the pathfinding algorithm
if __name__ == "__main__":
    grid = [
        ['s', '.', '.', 'x', 'g'],
        ['.', 'x', '.', '.', '.'],
        ['.', 'x', 'x', 'x', '.'],
        ['.', '.', '.', '.', '.']
    ]
    path = [(0,0), (0,1), (0,2), (1,2), (1,3), (1,4), (0,4)]
    visualize_path(grid, path, "Example Algorithm") 