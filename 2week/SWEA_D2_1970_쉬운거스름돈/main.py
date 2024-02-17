import sys
sys.stdin = open('main.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    # 돈의 종류를 리스트로 만듬
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 돈의 종류에 대입시킬 잔돈 개수 리스트도 만듬
    cnt_lst = [0] * len(money_lst)
    # print(N, cnt_lst)

    # 돈의 종류 개수만큼 반복
    for i in range(len(money_lst)):
        cnt_lst[i] = N // money_lst[i]  # 잔돈 개수 저장
        N = N % money_lst[i]            # 금액 갱신


    print(f'#{tc+1}')
    print(*cnt_lst)




