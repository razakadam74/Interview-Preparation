import heapq

h= [12,32,1,24,5,2,6,7]

heapq.heapify(h)

while len(h) >= 1:
    print(heapq.heappop(h))



