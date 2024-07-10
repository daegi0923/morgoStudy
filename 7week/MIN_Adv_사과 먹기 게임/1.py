import sys
sys.stdin = open('1.txt', 'r')

from collections import deque

t = int(input())

# 오른쪽 방향으로 직진이 초기값임
# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, ix):
    global apple, si, sj, idx
    q = deque([[i, j, ix, 0]])

    while q:
        ci, cj, cidx, cnt = q.popleft()

        # 기저조건
        # 사과 찾으면 cnt 리턴해서 answer에 합함
        if MAP[ci][cj] == apple:
            apple += 1  # 다음 사과 번호로 갱신
            si = ci
            sj = cj
            idx = cidx
            return cnt

        ni, nj = ci + di[cidx % 4], cj + dj[cidx % 4]  # 직진
        ni2, nj2 = ci + di[(cidx+1) % 4], cj + dj[(cidx+1) % 4]  # 턴

        if 0 <= ni < n and 0 <= nj < n:
            q.append([ni, nj, cidx, cnt])
        if 0 <= ni2 < n and 0 <= nj2 < n:
            q.append([ni2, nj2, cidx+1, cnt+1])

def solve():
    answer = 0  # 우회전 횟수
    for _ in range(1, m+1):  # 사과의 갯수만큼 반복
        answer += bfs(si, sj, idx)
    print(f"#{tc+1} {answer}")

for tc in range(t):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    m = apple = 1  # 사과의 번호 초기값
    si = sj = idx = 0  # 시작 위치, 방향키 초기값
    for i in range(n):  # 사과의 갯수를 파악하고 m 갱신
        m = max(m, max(MAP[i]))

    solve()
