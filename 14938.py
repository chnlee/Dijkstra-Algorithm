import heapq
INF = float('inf')
n, m, r = map(int,input().split())
item = list(map(int,input().split()))
graph = [[] for i in range(n+1)]

for i in range(r):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))


def djikstra(start):
  result = 0
  distance = [INF] * (n+1)
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
  for i in range(1,n+1):
    if distance[i] <= m:
      result += item[i-1]
  return result 

value = 0
for k in range(1, n+1):   
  value = max(value, djikstra(k))
  


print(value)
  