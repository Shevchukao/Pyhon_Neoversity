from collections import deque

queue = deque()  # work faster for append
print(f"Created {queue}")
queue.append("a")  # deque(['a'])
print(queue)
queue.append("t")  # deque(['a', 't'])
print(queue)
queue.append("b")  # deque(['a', 't', 'b'])
print(queue)
print(f"Filled:{list(queue)}")  # created list
print(f"Top: {queue[0]}")  # Top: a
print(f"Stealin element {queue.popleft()}")  # start is up
print(f"Filled:{list(queue)}")  # Filled:['t', 'b']
print(f"Top: {queue[0]}")  # Top: t
print(f"Is it empty? {len(queue)==0}")  # Is it empty? False
print(f"Lenth: {len(queue)}")  # Lenth: 2
