import sys

sys.stdin = open('input.txt')

INF = float('inf')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    E = float(input())

    # 각 섬의 좌표를 (x, y) 튜플 리스트로 저장합니다.
    islands = list(zip(x_coords, y_coords))

    # MST에 포함되었는지 여부를 기록합니다.
    visited = [False] * N
    # 각 섬에서 현재 MST까지의 최소 연결 비용을 저장합니다.
    min_costs = [INF] * N
    # 0번 섬에서 시작하므로, 0번 섬의 비용은 0입니다.
    min_costs[0] = 0

    mst_total_cost = 0

    # N개의 섬을 모두 MST에 포함시킬 때까지 반복합니다.
    for _ in range(N):
        # 1. MST에 포함되지 않은 섬 중, 가장 연결 비용이 적은 섬(min_node)을 찾습니다.
        min_cost = INF
        min_node = -1
        for i in range(N):
            if not visited[i] and min_costs[i] < min_cost:
                min_cost = min_costs[i]
                min_node = i

        # 2. 찾은 섬을 MST에 포함시키고, 비용을 누적합니다.
        visited[min_node] = True
        mst_total_cost += min_cost

        # 3. 새로 추가된 섬(min_node)을 기준으로,
        #    MST에 없는 다른 섬들까지의 최소 연결 비용을 갱신합니다.
        for i in range(N):
            if not visited[i]:
                # min_node와 i번 섬 사이의 비용을 계산합니다.
                cost = E * (
                    (islands[min_node][0] - islands[i][0]) ** 2
                    + (islands[min_node][1] - islands[i][1]) ** 2
                )
                # 기존에 알려진 비용보다 더 저렴한 경로가 발견되면 갱신합니다.
                min_costs[i] = min(min_costs[i], cost)

    print(f'#{tc} {round(mst_total_cost)}')

