# 플로이드 워셜 알고리즘
# 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우
# 모든 지점에서 다른 모든 지점까지의 최단 경로룰 모두 구해야 하는 경우
# 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다.
# 2차원 리스트에 최단 거리 정보를 저장한다는 특징이 있다.

# 자기 자신한테 향하는 비용은 0 으로 초기화
# 각 간선에 대한 정보를 입력받기, 그리고 그 값으로 초기화
# 총 세번 for 문을 돌려 각 노드에 따른 최소 값을 구한다.
# 수행된 결과를 출력한다.

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화한다.
for a in range(1, n+1):
  for b in range(1,n+1):
    if a == b:
      graph[a][b] = 0 

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int,input().split())
  graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행한다.
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력한다.
for a in range(1,n+1):
  for b in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력한다.
    if graph[a][b] == INF:
      print("INFINITY",end = " ")
    # 도달할 수 있는 경우 거리를 출력한다.
    else:
      print(graph[a][b], end= " ")
  print()

