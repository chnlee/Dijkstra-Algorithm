import heapq
INF = float('inf')
n, m, r = map(int,input().split())
item = list(map(int,input().split()))
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(r):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))


def djikstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
    

djikstra(r)

result = 0
for i in range(1,n+1):
  print(distance[i])
  if distance[i] < m:
    result += item[i-1]
  

print(result)
  