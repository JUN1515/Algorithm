def string_split(arr, cnt):
    arr = arr.split(":")
    for i in range(len(arr)):
        arr[i] = "0" * (4 - len(arr[i])) + arr[i]
        cnt -= 1
    return ":".join(arr), cnt

def zero_string(cnt):
    arr = ["0000"] * cnt
    return ":".join(arr)

def solution():
    S = input().strip()
    answer = ""
    cnt = 8

    arr1 = S.split("::")
    if len(arr1) == 2:
        if arr1[0] == "":
            temp, cnt = string_split(arr1[1], cnt)
            answer = zero_string(cnt) + ":" + temp
        elif arr1[1] == "":
            temp, cnt = string_split(arr1[0], cnt)
            answer = temp + ":" + zero_string(cnt)
        else:
            left, cnt = string_split(arr1[0], cnt)
            right, cnt = string_split(arr1[1], cnt)
            answer = left + ":" + zero_string(cnt) + ":" + right
    else:
        temp, cnt = string_split(arr1[0], cnt)
        answer = temp
    print(answer)


solution()