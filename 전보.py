# 전보
import heapq
INF = float('inf')
n, m, C = map(int,input().split())

graph = [[] for _ in range(n+1)]

distance =[INF] * (n+1)

for _ in range(m):
  X,Y,Z = map(int,input().split())
  graph[X].append((Y,Z))
def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  # 처음 시작을 0이라고 정의하는 것이 중요하다.
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist < distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(C)
count = -1
value = 0
for i in range(1,n+1):
  if distance[i] != INF:
    count += 1
  value = max(value, distance[i])

print(count, value)



