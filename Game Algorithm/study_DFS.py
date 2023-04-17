class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    # def iterative_dfs(start_v):
    #     discoverd = []
    #     stack = [start_v]
    #     while stack:
    #         v = stack.pop()
    #         if not v in discoverd:
    #             discoverd.append(v)
    #             for w in G1[v]:
    #                 stack.append(w)
    #     return discoverd

G1 = None
stack = []
visited = []


G1 = Graph(6)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][4] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1; G1.graph[3][5] = 1
G1.graph[4][1] = 1
G1.graph[5][3] = 1

print('## G1 무방향 그래프 ##')
for row in range(6) :
	for col in range(6) :
		print(G1.graph[row][col], end = ' ')
	print()
        
        
current = 0
stack.append(current)
visited.append(current)

while stack:
    current = stack.pop()
    for v in range(6):
        if G1.graph[current][v] == 1:
            if v in visited:
                pass
            else:
                stack.append(v)
                visited.append(v)


# while stack:
#     next = None
#     for vertex in range(6):
#         if G1.graph[current][vertex] == 1:
#             if vertex in visited:
#                 pass
#             else:
#                 next = vertex
#                 break
#     if next != None:
#         current = next
#         stack.append(current)
#         visited.append(current)
#     else:
#         current = stack.pop()

print('방문 순서 -->', end='')
for i in visited :
	print(chr(ord('A')+i), end='   ')