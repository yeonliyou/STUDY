import sys
sys.stdin = open("input.txt")

T = int(input())

# 대각선 방향 (시계방향 순서)
# 0: ↘, 1: ↙, 2: ↖, 3: ↗
# 이렇게 정의해야 "같은 방향 유지 or 시계방향으로 꺾기" 규칙을 쉽게 적용할 수 있음
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()) ) for _ in range(N)]

    ans = -1   # 가능한 최대 디저트 개수, 없으면 -1

    # 범위 체크 함수
    def in_range(r, c):
        return 0 <= r < N and 0 <= c < N

    # 모든 좌표를 출발점으로 시도
    for sr in range(N):
        for sc in range(N):
            eaten = {arr[sr][sc]}     # 출발점 디저트는 이미 먹음
            visited = {(sr, sc)}      # 출발점 좌표도 방문 처리

            # DFS 함수
            # r, c: 현재 위치
            # dir_idx: 현재 진행 방향(0~3)
            # turns: 방향을 꺾은 횟수 (0~3)
            # steps: 이동한 칸 수 (출발점 제외)
            def dfs(r, c, dir_idx, turns, steps):
                global ans

                # 다음 이동 방향 후보: 현재 방향 그대로 가기 / 시계방향으로 한 칸 꺾기
                for nd in (dir_idx, (dir_idx + 1) % 4):
                    nr, nc = r + dr[nd], c + dc[nd]

                    # 1) 출발점으로 복귀한 경우
                    if (nr, nc) == (sr, sc):
                        # 사각형이 완성되려면 정확히 3번 꺾어야 함(turns == 3)
                        # 그리고 최소 4칸 이상 돌아야 의미 있음
                        if turns == 3 and steps >= 3:
                            # 출발점까지 포함해서 개수를 세어야 하므로 steps+1
                            ans = max(ans, steps + 1)
                        continue

                    # 2) 이동할 수 없는 경우들 필터링
                    if not in_range(nr, nc):   # 격자 밖
                        continue
                    if (nr, nc) in visited:    # 이미 방문한 좌표
                        continue
                    v = arr[nr][nc]
                    if v in eaten:             # 이미 먹은 디저트 종류
                        continue

                    # 3) 새로운 방향 꺾기 횟수 계산
                    new_turns = turns + (0 if nd == dir_idx else 1)
                    if new_turns > 3:          # 최대 3번까지만 허용
                        continue

                    # 4) 상태 업데이트 후 재귀 탐색
                    eaten.add(v)
                    visited.add((nr, nc))

                    dfs(nr, nc, nd, new_turns, steps + 1)

                    # 5) 백트래킹 (상태 원복)
                    visited.remove((nr, nc))
                    eaten.remove(v)

            # 출발점에서 4가지 방향 모두 시작해봄
            for first_dir in range(4):
                dfs(sr, sc, first_dir, 0, 0)

    print(f"#{t} {ans}")
