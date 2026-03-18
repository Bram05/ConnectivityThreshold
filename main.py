# The code in this file was first written, but turned out to be incredibly slow. I then rewrote it in C++ and got the results much faster.
# This code was not used in the generation of the graphs.
#
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
# import math
#
# mpl.rc("axes", labelsize=14)
# mpl.rc("xtick", labelsize=12)
# mpl.rc("ytick", labelsize=12)
#
#
# def dist2(a, b):
#     (x1, y1), (x2, y2) = a, b
#     return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
#
#
# def ConstructRRG(n, r):
#     # points = [(random.random(), random.random()) for i in range(n)]
#     xcoords = [random.random() for i in range(n)]
#     ycoords = [random.random() for i in range(n)]
#     # plt.plot(xcoords, ycoords, "o")
#     # xcoords = [0, 0.05]
#     # ycoords = [0.5, 0.5]
#
#     adjacency_list = [[] for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if dist2((xcoords[i], ycoords[i]), (xcoords[j], ycoords[j])) <= r * r:
#                 adjacency_list[i].append(j)
#
#     return ((xcoords, ycoords), adjacency_list)
#
#
# def RenderGraph(graph):
#     ((xcoords, ycoords), adjacency_list) = graph
#     plt.plot(xcoords, ycoords, "o")
#     for i, v in enumerate(adjacency_list):
#         for j in v:
#             plt.plot([xcoords[i], xcoords[j]], [ycoords[i], ycoords[j]])
#     plt.show()
#
#
# def IsConnected(graph):
#     ((xcoords, ycoords), adjacency_list) = graph
#     n = len(adjacency_list)
#     visited = [False for _ in range(n)]
#     stack = [0]
#     found = 0
#     while len(stack) != 0:
#         pos = stack.pop()
#         if visited[pos]:
#             continue
#         visited[pos] = True
#         found += 1
#         for a in adjacency_list[pos]:
#             stack.append(a)
#     return found == n
#
#
# # while True:
# #     n = random.randint(50, 150)
# #     r = random.random()/4
# #     graph = ConstructRRG(n, r)
# #     print(f"Graph with n = {n}, r = {r} is connected={IsConnected(graph)}")
# #     RenderGraph(graph)
# output = []
# numTests = 100
# for r in [0.01 * x for x in range(143)]:
#     print(f"Now running test r={r}")
#     numConnected = 0
#     for i in range(numTests):
#         # print(i)
#         n = random.randint(100, 500)
#         graph = ConstructRRG(n, r / math.sqrt(n))
#         if IsConnected(graph):
#             numConnected += 1
#     output.append((r, numConnected / numTests))
# plt.plot(output)
# plt.show()
#
# # plt.figure()
# # plt.plot([1, 2, 3], [4, 6, 9])
# # plt.show()
