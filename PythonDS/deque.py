from collections import deque

d = deque([], 10)

d.append('Thur')
d.appendleft('Mon')
d.appendleft('Tues')

d.pop()


print(d)


