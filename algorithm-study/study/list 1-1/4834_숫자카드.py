T = int(input())

for t in range(T):
    N = int(input())

    number = []
    ex = input()
    #받은 문자열 요소 int로 변환해서 추가
    for z in ex:
        number.append(int(z))

    #0~9까지의 리스트
    number_list = [i for i in range(10)]
    #0~9의 개수 카운트 리스트
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #number 리스트를 하나씩 돌면서 j 숫자의 카운트 리스트를 1씩 증가
    for j in number:
        idx = number_list.index(j)
        count_list[idx] += 1

    #최대 카운트, 최대 카운트에 해당되는 값
    max_count = 0
    max_value = 0

    #카운트 리스트를 돌면서 이전의 값보다 큰 카운트 값일때마다 값 갱신
    for idx, m in enumerate(count_list):
        if m > max_count:
            max_count = m
            max_value = number_list[idx]
        #카운트 개수가 같다면 더 큰 숫자를 선택
        elif m == max_count:
            if max_value < number_list[idx]:
                max_count = m
                max_value = number_list[idx]
            else:
                continue
        else:
            continue

    print(f'#{t+1}', max_value, max_count)
