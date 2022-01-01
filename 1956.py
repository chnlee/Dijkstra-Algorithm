# 최솟값을 설정하는 거리를 정의하는 것이 이 문제의 핵심이다.
import sys
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int,input().split())

graph = [[INF] * (V+1) for _ in range(V+1)]
distance = INF
for i in range(1,V+1):
  for j in range(1,V+1):
    if i == j:
      graph[i][j] = 0

for _ in range(E):
  a,b,c = map(int,input().split())
  graph[a][b] = c

for k in range(1,V+1):
  for a in range(1,V+1):
    for b in range(1,V+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1,V+1):
  for b in range(1,V+1):
    if a != b:
      distance = min(distance, graph[a][b] + graph[b][a])

if distance < INF :
  print(distance)
else:
  print(-1)