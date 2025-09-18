import sys
import heapq

sys.stdin = open('input.txt')


def prim_mst(num_vertices, adj_list, start=1):
    """
    Prim 알고리즘으로 MST를 구하는 함수.
    """
    # 방문 여부를 알 수 있는 리스트
    visited = [False] * (num_vertices + 1)  # 정점의 방문(MST 포함) 여부
    # 큐
    priority_queue = []  # (가중치, 시작점, 도착점)을 담을 최소 힙

    mst_cost = 0  # MST의 총 가중치
    edges_count = 0  # MST에 포함된 간선의 수

    # 1. 시작 정점과 연결된 모든 간선을 우선순위 큐에 넣음
    for cost, next_node in adj_list[start]:
        heapq.heappush(priority_queue, (cost, start, next_node))

    # 시작 지점은 방문처리
    visited[start] = True

    # 2. 큐가 비거나, MST가 완성될 때까지 반복
    while priority_queue and edges_count < num_vertices - 1:
        # 3. 현재 MST 집합과 연결된 간선 중, 가장 가중치가 낮은 간선을 꺼냄
        cost, _, end = heapq.heappop(priority_queue)

        # 4. 도착 정점이 이미 MST에 포함된 경우, 이 간선은 사이클을 유발하므로 무시
        if visited[end]:
            continue

        # 5. 새로운 정점을 MST에 포
        # 지금까지 가중치 얼마 썼냐
        mst_cost += cost
        # 지금까지 간선 몇개 지났냐 (거리)
        edges_count += 1

        # 6. 새로 추가된 정점과 연결된, 아직 방문 안 한 정점으로 가는 간선들을 큐에 추가
        for next_cost, next_node in adj_list[end]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_cost, end, next_node))

    return mst_cost


# --- 실행 로직 ---
V, E = map(int, input().split())
# 프림은 인접 리스트를 사용
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    s, e, cost = map(int, input().split())
    # (가중치, 연결된 정점) 형태로 저장
    adj_list[s].append((cost, e))
    adj_list[e].append((cost, s))

print("인접리스트", adj_list)

# 인자 : 노드 개수, 인접행렬, 시작 노드 번호
result_cost = prim_mst(V, adj_list, start=1)
print(f"Prim MST 총 비용: {result_cost}")
