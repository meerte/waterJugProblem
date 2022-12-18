from simpleai.search import *

import jugs_problem

max_capacity_list = []
target_volume_list = []
for i in range(3):
    max_capacity = input(f"Enter max capacity for Jug{i + 1}: ")
    max_capacity = int(max_capacity)
    max_capacity_list.append(max_capacity)

for i in range(3):
    target_volume = input(f"Enter target volume for Jug{i + 1}: ")
    target_volume = int(target_volume)
    target_volume_list.append(target_volume)

problem = jugs_problem.JugsProblem(max_capacity=(max_capacity_list[0], max_capacity_list[1], max_capacity_list[2]),
                                   target_volume=(target_volume_list[0], target_volume_list[1], target_volume_list[2]))

result = breadth_first(problem, graph_search=True, viewer=jugs_problem.my_viewer)
# result = depth_first(problem, graph_search=True, viewer=jugs_problem.my_viewer)
# result = iterative_limited_depth_first(problem, graph_search=True, viewer=jugs_problem.my_viewer)
# result = limited_depth_first(problem, graph_search=True, viewer=jugs_problem.my_viewer, depth_limit=10)
# result = limited_depth_first(problem, graph_search=True, viewer=jugs_problem.my_viewer, depth_limit=10)
# result = uniform_cost(problem, graph_search=True, viewer=jugs_problem.my_viewer)

i = 1
for path in result.path():
    print(f"{i}- {path}")
    i += 1

print(f"Total cost: {result.cost}")
print(jugs_problem.my_viewer.stats)
