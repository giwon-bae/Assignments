#2
# n = int(input())
# result = 0

# for i in range(1, n+1):
#     result += i

# print(result)

#3
#data = [10,20,30,40,50]

#4
# list_a = []

# list_a.append(10)
# list_a.append(20)
# list_a.append(30)
# list_a.append(40)
# list_a.append(50)

# print(list_a.pop())
# print(list_a.pop())
# print(list_a.pop())

#5
# from collections import deque

# queue = deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)

# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())

#6
# class Graph():
#     def __init__(self, size):
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]

# graph1 = Graph(6)
# for i in range(graph1.SIZE):
#     for j in range(graph1.SIZE):
#         print(graph1.graph[i][j], end=' ')
#     print()

#7
# class Graph():
#     def __init__(self, size):
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]

# G1 = Graph(5)
# G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][4] = 1
# G1.graph[1][0] = 1; G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1; G1.graph[2][4] = 1
# G1.graph[3][2] = 1; G1.graph[3][4] = 1
# G1.graph[4][0] = 1; G1.graph[4][2] = 1; G1.graph[4][3] = 1

# for i in range(G1.SIZE):
#     for j in range(G1.SIZE):
#         print(G1.graph[i][j], end=' ')
#     print()

#8
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = Graph(5)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][4] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1; G1.graph[2][4] = 1
G1.graph[3][2] = 1; G1.graph[3][4] = 1
G1.graph[4][0] = 1; G1.graph[4][2] = 1; G1.graph[4][3] = 1
stack = []
visited = []

stack.append(0)
visited.append(0)

while stack:
    current = stack.pop()
    for i in range(G1.SIZE):
        if G1.graph[current][i] == 1 and i not in visited:
            stack.append(i)
            visited.append(i)
            break

for i in range(len(visited)):
    print(visited[i], end='->')
print('end')

# from collections import deque
# queue = deque()
# visited = []

# queue.append(0)
# visited.append(0)

# while queue:
#     current = queue.popleft()
#     for i in range(G1.SIZE):
#         if G1.graph[current][i] == 1 and i not in visited:
#             queue.append(i)
#             visited.append(i)

# for i in range(len(visited)):
#     print(visited[i], end="->")
# print('end')