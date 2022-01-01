# 이코테 - 미래 도시
# 양쪽 다 거리가 1이라는 사실을 알고 있자
# 거리를 설정하고, 거리 이상이면 -1 을 설정하자는 것도 알고 있자.
INF = int(1e9)

n, m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] =0 

for i in range(m):
  a, b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1
x, k = map(int,input().split())

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x] 

if distance >= INF:
  print(-1)
else:
  print(distance)