def solution(dirs):
    answer = 0
    
    comd_dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}   # 커멘드 이동 정보
    comd_reverse_dir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
    visited = [[{'U': 0, 'D': 0, 'L': 0, 'R': 0} for _ in range(11)] for _ in range(11)]                             # 방문 배열
    
    r, c = 5, 5         # 시작지점
    
    for comd in dirs:
        dr, dc = comd_dir[comd]
        nr, nc = r + dr, c + dc
        
        # 범위 벗어나면 해당 커멘드 무시
        if nr < 0 or nr > 10 or nc < 0 or nc > 10: continue
        visited[r][c][comd_reverse_dir[comd]] += 1
        if visited[nr][nc][comd] == 0:
            visited[nr][nc][comd] = 1
            answer += 1
        r, c = nr, nc
        
    
    return answer