import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n = int(input())
set_ = set(map(int, input().split()))
x = int(input())
# print(lst)
count = 0

for i in set_:
    # print(i)
    j = x - i
    if j in set_:
        count += 1

# (1, 3) (3, 1) 과 같이 두번씩 카운트 되므로 절반으로 나누어준다.
print(int(count/2))