S = input().strip()

l = r = 0
is_tag = False

result = ""

for i in range(len(S)):
    if is_tag:  #태그가 씌워진 경우
        if S[i] == '>':
            r = i
            result += S[l : i] + S[i]
            r = l = i + 1
            is_tag = False
        continue

    if S[i] == '<':
        result += S[l : i][::-1] + S[i]
        is_tag = True
        l = i + 1
        continue
    elif S[i] == ' ':
        result += S[l : i][::-1] + S[i]
        r = l = i + 1
    else:
        r = i
else:
    if l <= r:
        result += S[l: r + 1][::-1]
print(result)