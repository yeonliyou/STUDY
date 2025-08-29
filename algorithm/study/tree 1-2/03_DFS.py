import sys
sys.stdin = open('input.txt')


def dfs(start):

    visited = [False] * (V + 1)  # 방문 여부 리스트
    stack = [start]  # 방문할 노드를 저장
    # 최종 탐색 경로
    path = []

    # 스택이 빌때까지 반복
    while stack:
        # 1. 스택에서 노드를 pop하여 경로에 추가
        curr_node = stack.pop()

        # 2. 만약 방문했었다면 다음꺼 체크하기 위해 반복문 돌아가기
        if visited[curr_node]:
            continue

        #3.  방문한 적 없다면 추가해주기
        visited[curr_node] = True
        path.append(curr_node)

        # 4. 현재 노드의 인접 노드들을 확인
        # 작은 번호부터 확인(내림차순 정렬 했기 때문)
        for next_node in adj_list[curr_node]:
            # 아직 방문하지 않은 노드를 발견하면,
            if visited[next_node] == False:
                # 스택에 push
                stack.append(next_node)

    return path


V, E = map(int, input().split())
graph = list(map(int, input().split()))

# 인접 리스트 생성
adj_list = [[] for _ in range(V + 1)]

# 간선 정보 입력 (양방향)
for i in range(E):
    n1, n2 = graph[2 * i], graph[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 인접 리스트의 각 요소를 내림차순 정렬
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)


result = dfs(1)

print(''.join(map(str, result)))
