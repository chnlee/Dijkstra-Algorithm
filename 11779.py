# path라는 list를 만들고, 경로 상 향하는 지점을 따로 생성해줘야한다.
import heapq
INF = float('inf')
n = int(input())
m = int(input())
graph =  [[] for i in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

start, end = map(int,input().split())
path = [[] for _ in range(n+1)]
path[start].append(start)

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
        # 리스트를 초기화 하기 위해서 만든 것이다.
        path[i[0]] = []
        # 현재 path의 경로에서 다음 i[0]의 경로 상의 값을 입력한다.
        for p in path[now]:
          path[i[0]].append(p)
        path[i[0]].append(i[0])   

djikstra(start)
print(distance[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))