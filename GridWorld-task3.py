import GenerateMaze
import RLSolver
import sys
import MutateMaze


    

if __name__ == '__main__':
    # Get the dimensions of the maze from the command line
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    N = int(width)

    # Check that the maze dimensions are square
    if width != height:
        print("Please specify maze dimensions that are square. e.g. (10x10, 50x50)")
        sys.exit()

    # Generate the maze
    maze = GenerateMaze.main(sys.argv)

    # Get the optimal path and length
    # This calls the test method of the trained RL agent.
    trace = RLSolver.main(sys.argv, plot=False)
    trace_len = len(trace)

    #convert coordinate sytem
    steps = []
    for step in trace:
        steps.append((height - step[1] - 1, step[0]))
    
    for step in steps:
        print(step)

    #Mutate Maze
    maze = MutateMaze.mutate_maze(steps, width, height)