import sys
input = sys.stdin.readline

def solution():
    def check(px, py):
        if py < y or py > y + h: return 0
        if x <= px <= x + w:
            return 1
        elif px < x and (px - x)**2 + (py - (y + (h // 2)))**2 <= (h // 2)**2:
            return 1
        elif px > x + w and  (px - (x + w))**2 + (py - (y + (h // 2)))**2 <= (h // 2)**2:
            return 1
        return 0

    w, h, x, y, p = map(int, input().strip().split())
    answer = 0
    for _ in range(p):
        x1, y1 = map(int, input().strip().split())
        answer += check(x1, y1)
    print(answer)


solution()