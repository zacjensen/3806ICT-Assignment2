import random
import GenerateMaze
import RLSolver
import sys
import MutateMaze


def traceToSteps(trace):
    """
    Converts RL Trace Coordinate System To Maze Coordinate System
    """
    steps = []
    for step in trace:
        steps.append((height - step[1] - 1, step[0]))
    return steps

if __name__ == '__main__':
    # Get the dimensions of the maze from the command line
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    N = int(width)

    # Check that the maze dimensions are square
    if width != height:
        print("Please specify maze dimensions that are square. e.g. (10x10, 50x50)")
        sys.exit()

    # Generate the initial maze
    maze = GenerateMaze.main(sys.argv)

    #get plan from RL Solver given initial state of maze
    taken_steps = []
    event_log = []
    goalFound = False
    trace = RLSolver.main(sys.argv, plot=False)
    planned_steps = traceToSteps(trace)
    taken_steps.append(planned_steps[0])
    event_log.append("Agent Moved to " + str(planned_steps[0]))

    #start executing steps in plan, after each step there is a 10% chance the maze mutates
    while(goalFound == False and len(taken_steps) < 2*width):
        mutation = False
        for step in planned_steps[1:]:
            event_log.append("Agent Moved to " + str(step))
            taken_steps.append(step)
            if(random.randint(0,9) == 0):
                #mutate maze
                maze = MutateMaze.mutate_maze(taken_steps, width, height)
                event_log.append("Mutation Event Discovered By Agent")
                #perform replanning
                trace = RLSolver.main(sys.argv, plot=False)
                planned_steps = traceToSteps(trace)
                mutation = True
                break

        if(mutation == False and len(taken_steps) < 2*width):
            goalFound = True
            

if(goalFound):
    print("\n\nFound Goal In ", len(taken_steps), "Steps, Event Log Below:")
    for event in event_log:
        print(event)
else:
    print("Goal Not Reached Within 2N Steps")


        

    


    