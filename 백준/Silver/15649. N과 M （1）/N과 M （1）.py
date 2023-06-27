def backtracking(N, M, selected, visited):
    # 수열의 길이가 M에 도달하면 출력
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            selected.append(i)
            backtracking(N, M, selected, visited)
            selected.pop()
            visited[i] = False

N, M = map(int, input().split())
visited = [False] * (N + 1)
backtracking(N, M, [], visited)
