T = int(input())

# 문자열 하나씩 받기
for t in range(1, T+1):
    input_str = input()

    # 뒤집은 문자열 저장
    reversed_str = input_str[::-1]

    # 원래 문자열, 뒤집은 문자열이 같은지 비교
    if input_str == reversed_str:   #같은 경우
        print(f"#{t}", 1)
    else:   #다른 경우
        print(f"#{t}", 0)