#출력을 더 예쁘기 보기 위한
import pprint

T = int(input())

for i in range(T):
    #10x10 격자 만들기
    ''' 리스트 내부에 각각의 자리마다 리스트로 빈공간 만들기
    [[], [], [], ... [],
     [], [], [], ... [],
     .
     .
     [], [], [], ... []]
    '''
    # list comprehension시에 얕은 복사 주의하기
    base_matrix = [[[] for _ in range(10)] for _ in range(10)]

    N = int(input())

    #칠할 영역의 개수 하나씩 돌기
    for _ in range(N):
        #칠할 영역의 왼쪽 위 모서리 인덱스, 오른쪽 아래 모서리 인덱스, 컬러색상 받기
        r1, c1, r2, c2, color = map(int, input().split())
        #칠할 영역을 한칸씩 돌면서 칸마다 색상 숫자 넣기
        for a in range(r1, r2 + 1):
            for b in range(c1, c2 + 1):
                base_matrix[a][b].append(color)

    # pprint.pprint(base_matrix)
    purple_count = 0

    # 행렬 한칸씩 보라색인지 검사하기
    for x in range(10):
        for y in range(10):
            # 배열 칸마다 1,2가 같이 들어있는거 보라색으로 판단하여 purple_count 1씩 증가
            if 1 in base_matrix[x][y] and 2 in base_matrix[x][y]:
                purple_count += 1
            else:
                pass

    # pprint.pprint(base_matrix)
    print(f'#{i + 1}', purple_count)


