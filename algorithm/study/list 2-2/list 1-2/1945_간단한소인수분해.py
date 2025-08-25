T = int(input())

for i in range(1, T+1):
    N = int(input())
    anw = []

    for j in [2, 3, 5, 7, 11]:
        cnt = 0
        #j로 소인수분해가 가능할 때까지 몫으로 N값 갱신
        while N % j == 0:
            N = N // j
            cnt += 1

        anw.append(str(cnt))

    print(f"#{i}", ' '.join(anw))