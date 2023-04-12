## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size, adjMat) :
		self.SIZE = size
		self.weight = [[adjMat[i][j] for j in range(size)] for i in range(size)]

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
			print("%2d" % g.weight[row][col], end = ' ')
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

def get_min_node(visit,dist):
	min_value=INF
	min_index=0
	for i in range(gSize):
		if not visit[i] and dist[i]<min_value:
			min_value=dist[i]
			min_index=i

	return min_index

# 방문노드 visited와 Distance 배열생성
visited = [ False for i in range(gSize)]
distance = [INF for i in range(gSize)]

u,v=0,0  #u = start, v= end

edge_result=[i for i in range(gSize)]
#시작노드 선택
distance[u]=0

for i in range(gSize):
	u=get_min_node(visited,distance)
	visited[u]=True
	for v in range(gSize):
		if not visited[v] and G1.weight[u][v]<distance[v]:
			distance[v]=G1.weight[u][v]
			edge_result[v]=u
    
print("Total cost : ", sum(distance))
for i in range(1,len(edge_result)):
    print("[{}, {}]".format(i, edge_result[i]), end=' ')