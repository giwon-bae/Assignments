from collections import deque

def dfs(s, r, c):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]):
        return
    if maze[r][c] != '1' and maze[r][c] != '.':
        print("append ", [r,c])
        s.append([r,c])

def bfs(q, r, c):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]):
        return
    if maze[r][c] != '1' and maze[r][c] != '.':
        q.append([r,c])


maze = [[ '1', '1', '1', '1', '1', '1' ],
        [ 'e', '0', '1', '0', '0', '1' ],
        [ '1', '0', '0', '0', '1', '1' ],
        [ '1', '0', '1', '0', '1', '1' ],
        [ '1', '0', '1', '0', '0', 'x' ],
        [ '1', '1', '1', '1', '1', '1' ]]


stack = []
queue = deque()
start = [1,0]
here = start
r, c = here
fail = False

while maze[r][c] != 'x':
    maze[r][c]='.'
    dfs(queue, r-1, c)
    dfs(queue, r+1, c)
    dfs(queue, r, c-1)
    dfs(queue, r, c+1)

    print(queue)
    if len(queue) == 0:
        print("fail")
        fail = True
        break
    here = queue.popleft()
    r, c = here
#     dfs(stack,r-1,c)
#     dfs(stack,r+1,c)
#     dfs(stack,r,c-1)
#     dfs(stack,r,c+1)


#     print(stack)
#     if len(stack) == 0:
#         print("fail")
#         fail = True
#         break
#     here = stack.pop()
#     r, c = here

if fail == False:
     print("success")