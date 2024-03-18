word = input().strip()

arr = [0] * 26
for ch in word:
    arr[ord(ch) - 97] += 1
print(*arr)