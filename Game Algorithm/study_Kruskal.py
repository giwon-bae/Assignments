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

# edgeAry = []

# for i in range(gSize):
#     for j in range(i+1, gSize):
# 	    if G1.graph[i][j] != INF:
# 		    edgeAry.append([i,j,G1.graph[i][j]])

# edgeAry.sort(key = lambda x:x[2])
# print(edgeAry)

# def find(parent, x):
# 	if parent[x] == x:
# 		return x
# 	else:
# 		parent[x] = find(parent, parent[x])
# 		return parent[x]

# def union(parent, a, b):
#     rootA = find(parent, a)
#     rootB = find(parent, b)
#     if rootA < rootB:
#         parent[rootB] = rootA
#     else:
#         parent[rootA] = rootB

# v, e = gSize, len(edgeAry)

# parent = [i for i in range(v)]
# total_cost = 0
# edge_result = []

# for edge in edgeAry:
#     a, b, cost = edge
#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#         total_cost += cost
#         edge_result.append([a,b])
	
# print(total_cost)
# print(edge_result)

	
	    
	
	    













# # 가중치와 간선 목록생성
# edgeAry = []

# for i in range(gSize) :
#     for j in range(i+1,gSize) :
#         if G1.graph[i][j] != INF :
#             edgeAry.append([i, j, G1.graph[i][j]])
            
# # 오름차순정렬 
# edgeAry.sort(key = lambda x:x[2])

# print(edgeAry)

# # 특정 원소가 속한 집합을 찾기
# def find(parent, x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent, parent[x])
#     return parent[x]


# # 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
# def union(parent, a, b):
#     rootA = find(parent, a)
#     rootB = find(parent, b)

#     if rootA < rootB:
#         parent[rootB] = rootA
#     else:
#         parent[rootA] = rootB


# # 노드의 개수와 간선(union 연산)의 개수 설정
# v, e = 6, len(edgeAry)

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# parent = [i for i in range(v)]
# total_cost = 0
# edge_result=[]

# for edge in edgeAry:
#     a, b, cost = edge
#     # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#         total_cost += cost
#         edge_result.append([a,b])

# print(edge_result)
# print(total_cost)