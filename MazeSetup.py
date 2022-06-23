import sys
import random
import time
from colorama import init
from colorama import Fore, Back, Style

# Init variables
wall = 'H'
cell = 'O'
unvisited = 'u'
height = 0
width = 0
maze = []
startPos = (0, 0)
endPos = (0, 0)

# Initialize colorama
init()
random.seed(time.time())
# Print Maze


def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (i == startPos[0] and j == startPos[1]):
                print(Fore.YELLOW + "S", end=" ")
            elif (i == endPos[0] and j == endPos[1]):
                print(Fore.YELLOW + "G", end=" ")
            elif (maze[i][j] == unvisited):
                print(Fore.WHITE + str(maze[i][j]), end=" ")
            elif (maze[i][j] == cell):
                print(Fore.GREEN + str(maze[i][j]), end=" ")
            else:
                print(Fore.RED + str(maze[i][j]), end=" ")
        print()
    print("\nStart Pos: (" + str(startPos[0]) + " " + str(startPos[1]) + ")\n")

# Find number of surrounding cells


def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == cell):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == cell):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == cell):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1] == cell):
        s_cells += 1

    return s_cells


def initMaze():
    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Randomize starting point and set it a cell
    starting_height = int(random.randrange(height))
    starting_width = int(random.randrange(width))
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height-1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width-1):
        starting_width -= 1

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height-1][starting_width] = wall
    maze[starting_height][starting_width - 1] = wall
    maze[starting_height][starting_width + 1] = wall
    maze[starting_height + 1][starting_width] = wall
    return walls


def dfs(walls):
    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1]-1] == unvisited and maze[rand_wall[0]][rand_wall[1]+1] == cell):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                # Delete wall
                for w in walls:
                    if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                        walls.remove(w)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == unvisited and maze[rand_wall[0]+1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for w in walls:
                    if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                        walls.remove(w)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == unvisited and maze[rand_wall[0]-1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for w in walls:
                    if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                        walls.remove(w)

                continue

        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == unvisited and maze[rand_wall[0]][rand_wall[1]-1] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for w in walls:
                    if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                        walls.remove(w)

                continue

        # Delete the wall from the list anyway
        for w in walls:
            if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                walls.remove(w)


def finishMaze():
    global startPos, endPos
    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == unvisited):
                maze[i][j] = wall
 
    # Set entrance
    pos = [0,0]
   
    positions = []

    for i in range(0, height):
        if (maze[i][1] == cell):
            pos = [i, 1]
            positions.append(pos)
    startPos = random.choice(positions)
    maze[startPos[0]][startPos[1]] = cell    

    #set goal to be a 2N-1 random walk from start
    pos = list(startPos)
    visited = [] #prefer to not revisit old paths but still might
    
    for i in range(4*len(maze)):
        choices = []
        x = pos[1]
        y = pos[0]
        if(x > 1 and maze[y][x-1] == cell):
            choices.append([y, x-1])
        if(maze[y][x+1] == cell):
            choices.append([y, x+1])
        if(maze[y-1][x] == cell):
            choices.append([y-1, x])
        if(maze[y+1][x] == cell):
            choices.append([y+1, x])

        c = random.choice(choices)
        if(c in visited):
            c = random.choice(choices)
        
        pos = c
        visited.append(pos)
        


    endPos = pos
    maze[endPos[0]][endPos[1]] = cell  

    print("Generated Maze with Start at ", startPos, " and goal at ", endPos)

    


def run(params):
    # Command line parameters
    global width, height
    if (len(params) < 3):
        print("Usage 'python GenerateMaze.py x y' (e.g. 'python GenerateMaze.py 10 10')")
        sys.exit()
    width = int(params[1])
    height = int(params[2])
    walls = initMaze()
    dfs(walls)
    finishMaze()
    # If maze is too big don't print
    if ((width * height) < 2000):
        printMaze(maze)
    return
