import numpy as np

def not_valid_move(maze, position):
    nrows, ncols = maze.shape
    x, y = position
    return x < 0 or y < 0 or x > nrows-1 or y > ncols-1 or maze[(x, y)] == 1

def maze_runner(maze, directions):
    moves = {"N": (-1, 0), "E": (0, 1), "W": (0, -1), "S": (1, 0)}
    maze = np.array(maze)
    position = np.argwhere(maze == 2)[0]
    for direction in directions:
        position += moves[direction]
        if not_valid_move(maze, position):
            return "Dead"
        elif maze[tuple(position)] == 3:
            return 'Finish'
    return "Lost"