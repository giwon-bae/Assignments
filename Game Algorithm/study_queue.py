from queue import Queue

que = Queue()
que.put(4)
que.put(5)
que.put(6)
print(que.get())
print(que.get())
print(que)

# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.popleft()
# print(queue)