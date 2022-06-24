import sys
import random
import time
from colorama import init
from colorama import Fore, Back, Style


# Init variables
wall = 'H'
cell = 'O'
unvisited = 'u'

#seed random generator and colorama
random.seed(time.time())
init()

#print maze using colours
def printMaze(maze, startPos, endPos):
    height = len(maze)
    width = len(maze[0])
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
    #print("\nStart Pos: (" + str(startPos[0]) + " " + str(startPos[1]) + ")\n")

# print maze to a txt file
def printTxt(maze, startPos, endPos):
    height = len(maze)
    width = len(maze[0])
    fileName = "Maze_" + str(width) + "x" + \
        str(height) + ".txt"
    sourceFile = open(fileName, 'w')
    row = ""
    # Print the maze as a .txt file
    for i in range(0, height):
        for j in range(0, width):
            if (i == startPos[0] and j == startPos[1]):
                row += "S"
            elif (i == endPos[0] and j == endPos[1]):
                row += "G"
            elif (maze[i][j] == cell):
                row += "O"
            else:
                row += "H"
        print(row, file=sourceFile)
        row = ""
    sourceFile.close()
    #print("Maze .txt outputted as", fileName)


# Find number of surrounding cells
def surroundingCells(rand_wall, maze):
    
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == cell):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == cell):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == cell):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == cell):
		s_cells += 1

	return s_cells


#Depth First Search Maze Generation
def dfs(walls, maze):
    height = len(maze)
    width = len(maze[0])

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1]-1] == unvisited and maze[rand_wall[0]][rand_wall[1]+1] == cell):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall, maze)

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
                
    

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == unvisited and maze[rand_wall[0]+1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall, maze)
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



        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == unvisited and maze[rand_wall[0]-1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall, maze)
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


        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == unvisited and maze[rand_wall[0]][rand_wall[1]-1] == cell):

                s_cells = surroundingCells(rand_wall, maze)
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

        # Delete the wall from the list
        for w in walls:
            if (w[0] == rand_wall[0] and w[1] == rand_wall[1]):
                walls.remove(w)

    return maze
	    

def initMazeMutate(steps, width, height, oldMaze):
    maze = []
    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    #add existing steps to maze
    walls = []
    for (i,j) in steps:

        # Mark it as cell and add surrounding walls to the list
        maze[i][j] = cell
        if (i-1, j) not in steps:
            walls.append([i - 1, j])
            maze[i-1][j] = wall
        if (i, j-1) not in steps:
            walls.append([i, j - 1])
            maze[i][j - 1] = wall
        if (i, j+1) not in steps:
            walls.append([i, j + 1])
            maze[i][j + 1] = wall
        if (i + 1, j) not in steps:
            walls.append([i + 1, j])
            maze[i + 1][j] = wall

    #perform some random walks around agent in old maze and keep the visited cells in the new maze
    #the maze surrounding the agent should mostly remain the same
    startPos = steps[-1]
    visited = steps.copy()
    for n in range(0,5):
        pos = list(startPos)
        for walk in range(20*width):
            choices = []
            x = pos[1]
            y = pos[0]
            if(oldMaze[y][x-1] == cell):
                choices.append([y, x-1])
            if(oldMaze[y][x+1] == cell):
                choices.append([y, x+1])
            if(oldMaze[y-1][x] == cell):
                choices.append([y-1, x])
            if(oldMaze[y+1][x] == cell):
                choices.append([y+1, x])

            c = random.choice(choices)
            pos = c
            visited.append(tuple(pos))

            # Mark it as cell and add surrounding walls to the list
            i = pos[0]
            j = pos[1]
            maze[i][j] = cell
            if (i-1, j) not in visited:
                walls.append([i - 1, j])
                maze[i-1][j] = wall
            if (i, j-1) not in visited:
                walls.append([i, j - 1])
                maze[i][j - 1] = wall
            if (i, j+1) not in visited:
                walls.append([i, j + 1])
                maze[i][j + 1] = wall
            if (i + 1, j) not in visited:
                walls.append([i + 1, j])
                maze[i + 1][j] = wall
 
    return walls, maze


def finishMazeMutate(steps, maze):

    global startPos, endPos
    height = len(maze)
    width = len(maze[0])
  
    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == unvisited):
                maze[i][j] = wall

    # Set start
    pos = (0,0)
    startPos = (steps[-1][0], steps[-1][1])
    maze[startPos[0]][startPos[1]] = cell  
 
    # Set goal to be a random walk from start
    pos = list(startPos)
    visited = []
    
    for i in range(2*(2*width - len(steps))):
        choices = []
        x = pos[1]
        y = pos[0]
        if(maze[y][x-1] == cell):
            choices.append([y, x-1])
        if(maze[y][x+1] == cell):
            choices.append([y, x+1])
        if(maze[y-1][x] == cell):
            choices.append([y-1, x])
        if(maze[y+1][x] == cell):
            choices.append([y+1, x])

        c = random.choice(choices)

        # if already visited c, try choosing once more
        if(c in visited):
            c = random.choice(choices)
        
        pos = c
        visited.append(pos)

    # Move once more to make sure goal is not at start
    choices = []
    x = pos[1]
    y = pos[0]
    if(maze[y][x-1] == cell and startPos != (y, x-1)):
        choices.append([y, x-1])
    if(maze[y][x+1] == cell and startPos != (y, x+1)):
        choices.append([y, x+1])
    if(maze[y-1][x] == cell and startPos != (y-1, x)):
        choices.append([y-1, x])
    if(maze[y+1][x] == cell and startPos != (y+1, x)):
        choices.append([y+1, x])

    c = random.choice(choices)       
    pos = c

    endPos = pos
    maze[endPos[0]][endPos[1]] = cell  

    #print("Mutated maze: currently at ", startPos, " and goal is now at ", endPos)
    return  startPos, endPos, maze
      
        
def mutate_maze(steps, width, height, oldMaze):
    
    walls, maze = initMazeMutate(steps, width, height, oldMaze)
    maze = dfs(walls, maze)
    (start, end, maze) = finishMazeMutate(steps, maze)
    printMaze(maze, start, end)
    printTxt(maze, start, end)

    return maze





