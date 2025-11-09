from collections import deque

queue = deque()  # work faster than with list, don't use index, work left and right
print(f"Created {queue}")
queue.append("a")  # deque(['a'])
queue.append("t")  # deque(['a', 't'])
queue.append("b")  # deque(['a', 't', 'b'])
print(f"Filled: {list(queue)}")  # Filled: ['a', 't', 'b']
queue.appendleft("b1")
queue.appendleft("b2")
print(f"Filled: {list(queue)}")  # Filled: ['b2', 'b1', 'a', 't', 'b']
print(queue.pop())  # b
print(f"Filled: {list(queue)}")  # Filled: ['b2', 'b1', 'a', 't']
print(queue.popleft())  # b2
print(f"Filled: {list(queue)}")  # Filled: ['b1', 'a', 't']

# Deque
# pop appendleft - queue
# popleft append - queue in other side
# pop append - stack
# popleft appendleft - left stack
# pop in empty queue - Index Error
