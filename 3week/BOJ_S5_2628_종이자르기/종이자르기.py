import sys
sys.stdin = open('종이자르기.txt')

N, M = map(int, input().split())
T = int(input())
MAP = [list(map(int, input().split())) for _ in range(T)]
# print(N, M)
# print(MAP)

row_cut = []
col_cut = []
max_area = 0

for i in range(T):
    if not MAP[i][0]:
        row_cut.append(MAP[i][1])
        # print(row_cut)
    else:
        col_cut.append(MAP[i][1])
        # print(col_cut)

row_cut.sort()
col_cut.sort()
area = 0

for i in range((len(row_cut)+1)*(len(col_cut)+1)):
    area = (M-row_cut[1])*(N-col_cut[0])
# print(area)
# print((len(row_cut)+1)*(len(col_cut)+1))