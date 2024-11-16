# Maze fastest path finder. Upon watching his video after finding my solution, I realise I did it very differently to how he did it. He used queue, which I has never heard of, and I chose recursion.
# I realise that instead of using curses I could have just used coloured text, as my solution didnt actually use curses to do anything interesting, but regardless this works.
# I also appreciate what he did with queue/curses with the continuously forming solution.

import curses
from curses import wrapper


def pathfind(path, row, col, maze, visited):
    # Base case: Check if the current cell is out of bounds, a wall, or visited
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == "#" or (row, col) in visited:
        return None

    # If the finish is found
    if maze[row][col] == "X":
        return path

    # Mark the cell as visited
    visited.add((row, col))

    # Explore adjacent cells
    adjacent = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
    all_paths = []
    for cell in adjacent:
        next_row, next_col = cell
        result = pathfind(path + [(next_row, next_col)], next_row, next_col, maze, visited)
        if result:  # If a valid path is found, add it to the list of all paths
            all_paths.append(result)

    # Unmark the cell (backtrack)
    visited.remove((row, col))

    # Return the shortest path among all valid paths
    if all_paths:
        return min(all_paths, key=len)  # Find the shortest path
    return None


def main(stdscr):
    maze = [
    ["O", " ", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", " "],
    ["#", " ", " ", " ", " ", "#", " ", " ", "#", " "],
    ["#", " ", "#", "#", " ", " ", "#", "#", " ", " "],
    [" ", " ", "#", "#", "#", " ", " ", " ", " ", "#"],
    [" ", "#", " ", " ", " ", "#", " ", "#", " ", "#"],
    [" ", "#", " ", "#", " ", " ", "#", "#", "#", "#"],
    [" ", "#", " ", "#", "#", "", " ", " ", " ", "#"],
    [" ", " ", " ", "#", "#", "#", "#", "#", " ", "X"]
]

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Maze
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Route

    # Finding start
    for row_index, row in enumerate(maze): 
        if "O" in row: 
            col_index = row.index("O")  
            r, c = row_index, col_index  

    path = pathfind([r, c], 0, 0, maze, set())
        
    # Drawing each cell
    for i in range(0, len(maze)):
        for x in range(0, len(maze[i])):
            if (i, x) not in path:
                stdscr.addstr(i, x, maze[i][x], curses.color_pair(1))  
            else:
                stdscr.addstr(i, x, "@", curses.color_pair(2))  

    # Refresh screen
    stdscr.refresh()
    smth = input()


wrapper(main)
