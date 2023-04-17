from collections import deque

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
queue = deque()
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
queue.append(current)
visited.append(current)

while queue:
    current = queue.popleft()
    print("current: ", current)

    for v in range(6):
        if G1.graph[current][v] == 1:
            if v in visited:
                pass
            else:
                queue.append(v)
                visited.append(v)

print('방문 순서 -->', end='')
for i in visited :
	print(chr(ord('A')+i), end='   ')