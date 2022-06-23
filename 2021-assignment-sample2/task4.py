import sys
import task3


def printTxt(maze):
    fileName = "Maze_" + str(task3.width) + "x" + str(task3.height) + ".txt"
    sourceFile = open(fileName, 'w')
    row = ""
    # Print the maze as a .txt file
    for i in range(0, task3.height):
        for j in range(0, task3.width):
            if (i == task3.startPos[0] and j == task3.startPos[1]):
                row += "S"
            elif (i == task3.endPos[0] and j == task3.endPos[1]):
                row += "G"
            elif (maze[i][j] == task3.cell):
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
        str(task3.width) + "x" + str(task3.height) + ".csp"
    mazefileName = "Maze_" + str(task3.width) + \
        "x" + str(task3.height) + ".txt"
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
                        outputFile.write(str(task3.width))
                elif item == 'N':
                    if items[0] == '#define':
                        outputFile.write(str(task3.height))

                # Replaces the values for starting pos and for the maze
                if item == '=':
                    # Replace starting pos values
                    if items[1] == 'r:{0..N-1}':
                        outputFile.write(str(task3.startPos[0]))
                    elif items[1] == 'c:{0..M-1}':
                        outputFile.write(str(task3.startPos[1]))

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
                                if (mazeitem is not '\n' and pos != ((task3.width + 1) * (task3.height)) - 1):
                                    outputFile.write(',')
                                if pos == ((task3.width + 1) * (task3.height)) - 1:
                                    outputFile.write('];')
                            # Add spaces to make it easier to read
                            outputFile.write('                  ')
        outputFile.write('\n')
    outputFile.close()
    templateFile.close()
    print("Maze .csp outputted as", outputfileName)


def main(params):
    task3.run(params)
    printTxt(task3.maze)
    printCSP(task3.maze)
    return


if __name__ == '__main__':
    main(sys.argv)
