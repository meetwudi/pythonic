from collections import deque

queue = deque(['Esther', 'Lee'])
queue.append('John')
queue.append('Wu')
print queue.popleft()
print queue.popleft()
print queue
