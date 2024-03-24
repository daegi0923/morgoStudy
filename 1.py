import sys
sys.stdin = open('1.txt', 'r')


풀이 1. DFS
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

def dfs(y, x):
    global cnt
    # 기저조건 없음

    for k in range(5):
        ny, nx = y + dy[k], x + dx[k]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if not graph[ny][nx]:
            continue
        if graph[ny][nx]:
            graph[ny][nx] = 0
            cnt += 1
            dfs(ny, nx)


N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
# print(graph)
result = []
cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for i in result:
    print(i)


# 풀이 2. BFS
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

from collections import deque

def bfs(y, x):
    global cnt

    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()

        for k in range(5):
            ny, nx = y + dy[k], x + dx[k]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not graph[ny][nx]:
                continue
            if graph[ny][nx]:
                graph[ny][nx] = 0
                cnt += 1
                bfs(ny, nx)


N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
# print(graph)
result = []
cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for i in result:
    print(i)
