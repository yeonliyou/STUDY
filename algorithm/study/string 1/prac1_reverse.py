T = int(input())

# 케이스 하나씩 받기
for t in range(1, T+1):
    curr_str = input()
    # 전체 슬라이싱을 뒤에서부터 슬라이싱
    print(f"#{t}", curr_str[::-1])