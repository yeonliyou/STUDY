import sys
sys.stdin = open('sample_in.txt')

T = int(input())

# 조건
# 1. 대, 중, 소로 구분하여 포장
# 2. 같은 크기의 당근은 무조건 같은 상자에
# 3. 비어 있는 상자는 없어야 함
# 4. 한 상자에 N/2 개 초과되면 안됨
# 5. 각 상자에 든 당근의 개수 차이가 최소가 되도록

# 당근 넣는 함수
def put_carrot(carr, box_dict):
    #  지금 넣고 있는 상자 or 다음 상자 중에 하나를 택해서 넣을 수 있음
    for curr_idx in [idx, idx + 1]:
        # 한 상자에 넣을 수 있는 당근 개수를 넘었다면
        if len(box_dict[curr_idx]) == N/2:
            continue

        # 만약 지금 확인하는 당근이 앞에 당근이랑 무게가 같다면
        if carr in box_dict[curr_idx]:
            box_dict[curr_idx].append(carr)

            break

        else:


for t in range(1, T+1):
    N = int(input())

    # 각 상자의 개수 임계점
    threshold = int(N/2)

    # 박스 정보 (작 1 -> 큰 3)
    box_dict = {1:[], 2:[], 3:[]}

    # 당근 리스트
    carrot_list = list(map(int, input().split()))

    # 종류별 당근 개수 저장 리스트
    cnt_list = [0 for _ in range(N+1)]

    # 답 초기화
    anw = -2

    # 1. 4번 조건 때문에 안되는 경우
    if N > int(N/2) * 3:
        anw = -1
        break

    else:
        # 2. 같은 크기의 당근은 무조건 같은 상자에 넣을 수 없는 경우 컷하기
        for num in range(1, N+1):
            if carrot_list.count(num) > int(N/2):
                anw = -1
                break
            else:
                # 해당 크기의 당근 개수 저장
               cnt_list[num] = carrot_list.count(num)

        # 3. 위에서 걸리는게 없으면 넣기 시작
        if anw != -1:
            # 현재 넣는 상자 번호
            idx = 1

            # 3. 그 외 배분해서 최솟값 찾기
            for carr in carrot_list:







    print(f"#{t}", anw)