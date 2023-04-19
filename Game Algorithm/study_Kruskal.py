## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size, adjMat) :
		self.SIZE = size
		self.graph = [[adjMat[i][j] for j in range(size)] for i in range(size)]

## 전역 변수 선언 부분 ##

nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산' ]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

def printGraph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(nameAry[v], end = ' ')
	print()
	for row in range(g.SIZE) :
		print(nameAry[row], end = ' ')
		for col in range(g.SIZE) :
			print("%2d" % g.graph[row][col], end = ' ')
		print()
	print()

G1=None

INF=99999
## 메인 코드 부분 ##
adjMat = [[  0, 10, 15,INF,INF,INF],
	      [ 10,  0, 40, 11, 50,INF],
	      [ 15, 40,  0, 12,INF,INF],
	      [INF, 11, 12,  0, 20, 30],
          [INF, 50,INF, 20,  0, 25],
          [INF,INF,INF, 30, 25,  0]
	  ]

gSize=6
G1=Graph(gSize,adjMat)
print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(G1)

edgeAry = []

for i in range(gSize):
    for j in range(i+1, gSize):
        if G1.graph[i][j] != INF:
            edgeAry.append([i,j,G1.graph[i][j]])

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = x
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB