import GridWorldtask4
import sys
import time

min_path = float('inf')
max_path = -float('inf')
avg_path = 0

total_goals = 0
avg_time = 0
avg_mutations = 0

begin = time.time()

for i in range(10):

    goalFound, time_taken, taken_steps, num_mutations = GridWorldtask4.main(
        sys.argv)

    path_length = len(taken_steps)

    if path_length > max_path:
        max_path = path_length

    if path_length < min_path:
        min_path = path_length

    avg_path += path_length
    total_goals += int(goalFound)
    avg_time += time_taken
    avg_mutations += num_mutations

end = time.time()

avg_path /= 10
avg_time /= 10
avg_mutations /= 10


print(f"\n\nNumber of times goal reached: {total_goals}")
print(f"Minimum path length: {min_path}")
print(f"Maximum path length: {max_path}")
print(f"Average path length: {avg_path}")
print(f"Average time taken: {avg_time}")
print(f"Average mutations per maze: {avg_mutations}")
print(
    f"Total time taken to generate 10 {sys.argv[1]}x{sys.argv[2]} mazes: {round(end-begin, 2)}s")
