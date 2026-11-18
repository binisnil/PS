from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        queue = deque() # bfs로 풀거라 큐 생성
        visited = [[False] * len(mat[0]) for _ in range(len(mat))]  # 방문 표시를 위한 2차원배열
        result = [[0] * len(mat[0]) for _ in range(len(mat))]
        # 상하좌우 이동 위한 좌표
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    queue.append((i, j))

        while queue: 
            x, y = queue.popleft()

            for i in range(4): #상하좌우 4번 돌거기 때문에
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    if not visited[nx][ny]:
                        result[nx][ny] = result[x][y] + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        return result
