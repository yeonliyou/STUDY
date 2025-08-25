# sol
## 1. 인접리스트
## 2. 인접행렬

# 이 풀이는 1. 인접리스트를 활용한 코드이다
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''
def bfs(s, V):
    # 초기화
    visited = [0] * (v+1)  # visited 생성
    q = [s]  # 큐 생성

    # 시작점 인큐 표시(시작점 인큐)
    visited[s] = 1

    # 탐색할 정점이 남아있는 동안 반복
    while q:
        # 디큐
        t = q.pop(0)
        # visit(), 방문정점 출력
        print(t)
        # 인접하고 미방문인 정점 인큐 (인큐표시)
        for w in adj_lst[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return


V, E = map(int, input().split())  # 마지막 정점, 간선 수
arr = list(map(int, input().split()))

# 인접리스트
adj_lst = [[] for _ in range(V+1)]  # V번행까지 준비
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)

bfs(4, v)