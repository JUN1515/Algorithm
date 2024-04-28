while True:
    num = int(input())
    if num == 0: break
    
    temp = 0
    for i in range(1, num + 1):
        temp += i
    print(temp) 