import GenerateMaze
import RLSolver
import sys

if __name__ == '__main__':
    # Get the dimensions of the maze from the command line
    width = sys.argv[1]
    height = sys.argv[2]
    N = int(width)

    # Check that the maze dimensions are square
    if width != height:
        print("Please specify maze dimensions that are square. e.g. (10x10, 50x50)")
        sys.exit()

    # Generate the maze
    GenerateMaze.main(sys.argv)

    # Get the optimal path and length
    # This calls the test method of the trained RL agent.
    trace = RLSolver.main(sys.argv, plot=False)
    trace_len = len(trace)

    # Check whether a path less than or equal to 2N was found
    if trace_len <= 2*N:
        print(f"Valid path of length {trace_len} found.")
        print(f"Maximum allowed path length for this maze is {2*N}")
