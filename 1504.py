# distance를 초기화하는 것이 중요한 알고리즘
# distance[now] 와 dist를 비교하는 것 또한 중요하다
import heapq
INF = float('inf')
n, m = map(int,input().split())
start = 1
graph = [[] for i in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1, v2 = map(int,input().split())

def djikstra(start,end):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
      continue
      
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))
  return distance[end]

result1 = djikstra(1,v1) + djikstra(v1,v2) + djikstra(v2,n)
result2 = djikstra(1,v2) + djikstra(v2,v1) + djikstra(v1,n)

result = min(result1,result2)
if result < INF:
  print(result)
else:
  print(-1)
