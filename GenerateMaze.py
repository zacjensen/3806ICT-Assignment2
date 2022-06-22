import sys
import MazeSetup


def printTxt(maze):
    fileName = "Maze_" + str(MazeSetup.width) + "x" + \
        str(MazeSetup.height) + ".txt"
    sourceFile = open(fileName, 'w')
    row = ""
    # Print the maze as a .txt file
    for i in range(0, MazeSetup.height):
        for j in range(0, MazeSetup.width):
            if (i == MazeSetup.startPos[0] and j == MazeSetup.startPos[1]):
                row += "S"
            elif (i == MazeSetup.endPos[0] and j == MazeSetup.endPos[1]):
                row += "G"
            elif (maze[i][j] == MazeSetup.cell):
                row += "O"
            else:
                row += "H"
        print(row, file=sourceFile)
        row = ""
    sourceFile.close()
    print("Maze .txt outputted as", fileName)


def printCSP(maze):
    # Open files
    outputfileName = "Maze_" + \
        str(MazeSetup.width) + "x" + str(MazeSetup.height) + ".csp"
    mazefileName = "Maze_" + str(MazeSetup.width) + \
        "x" + str(MazeSetup.height) + ".txt"
    outputFile = open(outputfileName, 'w')
    templateFile = open('template.csp', 'r')
    mazeFile = open(mazefileName, 'r')

    for line in templateFile.readlines():
        items = line.split()
        if items:
            for item in items:
                outputFile.write(item + ' ')

                # Replaces the #define values for height and width
                if item == 'M':
                    if items[0] == '#define':
                        outputFile.write(str(MazeSetup.width))
                elif item == 'N':
                    if items[0] == '#define':
                        outputFile.write(str(MazeSetup.height))

                # Replaces the values for starting pos and for the maze
                if item == '=':
                    # Replace starting pos values
                    if items[1] == 'r:{0..N-1}':
                        outputFile.write(str(MazeSetup.startPos[0]))
                    elif items[1] == 'c:{0..M-1}':
                        outputFile.write(str(MazeSetup.startPos[1]))

                    # Insert the maze into the .csp
                    elif items[1] == 'maze[N][M]':
                        outputFile.write('[')
                        pos = 0
                        for mazeline in mazeFile.readlines():
                            mazeitems = [char for char in mazeline]
                            for mazeitem in mazeitems:
                                pos += 1
                                # Get rid of S for starting pos
                                if mazeitem == 'S':
                                    mazeitem = 'O'
                                outputFile.write(mazeitem)
                                # Add the ]; at the end and make sure the correct number of ,'s are being added
                                if (mazeitem != '\n' and pos != ((MazeSetup.width + 1) * (MazeSetup.height)) - 1):
                                    outputFile.write(',')
                                if pos == ((MazeSetup.width + 1) * (MazeSetup.height)) - 1:
                                    outputFile.write('];')
                            # Add spaces to make it easier to read
                            outputFile.write('                  ')
        outputFile.write('\n')
    outputFile.close()
    templateFile.close()
    print("Maze .csp outputted as", outputfileName)


def main(params):
    MazeSetup.run(params)
    printTxt(MazeSetup.maze)


if __name__ == '__main__':
    main(sys.argv)
    # printCSP(MazeSetup.maze)
