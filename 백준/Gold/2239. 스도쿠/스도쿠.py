def solution():

    # 스도쿠에서 확실히 숫자를 채울 수 있는 부분 사전에 채워넣기
    def pre_fill():
        remain_case = True
        while remain_case:
            remain_case = False

            for r in range(0, 9, 3):
                for c in range(0, 9, 3):

                    # 각 3 x 3 부분에서, 행, 열, box를 확인해서 가능한 숫자를 확인
                    current_box = box_possible[(r // 3) * 3 + (c // 3)]
                    numbers = [[] for _ in range(10)]
                    for dr in range(3):
                        for dc in range(3):
                            nr, nc = r + dr, c + dc
                            num = arr[nr][nc]
                            if num == 0:
                                possible_nums = row_possible[nr] & col_possible[nc] & current_box
                                for num in possible_nums:
                                    numbers[num].append((nr, nc))

                    # 만약 해당 숫자가 가능한 곳이 한 곳 뿐이면 채워넣기
                    for num in range(1, 10):
                        if len(numbers[num]) == 1:
                            nr, nc = numbers[num][0]
                            arr[nr][nc] = num
                            row_possible[nr].remove(num)
                            col_possible[nc].remove(num)
                            current_box.remove(num)
                            remain_case = True

    def dfs(cnt, goal):
        if cnt == goal:
            return True

        r, c = q[cnt]
        current_box = box_possible[(r // 3) * 3 + (c // 3)]
        possible_num = row_possible[r] & col_possible[c] & current_box
        if not possible_num:
            return False

        for num in sorted(possible_num):
            arr[r][c] = num
            row_possible[r].remove(num)
            col_possible[c].remove(num)
            current_box.remove(num)
            if dfs(cnt + 1, goal):
                return True
            arr[r][c] = 0
            row_possible[r].add(num)
            col_possible[c].add(num)
            current_box.add(num)

    arr = [list(map(int, list(input().strip()))) for _ in range(9)]
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = arr[r][c]
            if num:
                row[r].add(num)
                col[c].add(num)
                box[(r // 3) * 3 + (c // 3)].add(num)

    full = set(range(1, 10))
    row_possible = [full - s for s in row]  # 각 행에서 0에 들어갈 수 있는 수
    col_possible = [full - s for s in col]  # 각 열에서 0에 들어갈 수 있는 수
    box_possible = [full - s for s in box]  # 각 3x3 에서 0에 들어갈 수 있는 수

    pre_fill()  # 사전에 확실히 채울 수 있는 부분 모두 채우기

    q = []      # 남아있는 빈칸의 좌표
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0:
                q.append((r, c))

    dfs(0, len(q))  # dfs로 가능한 경우 찾기

    for lst in arr:
        print(''.join(map(str, lst)))


solution()