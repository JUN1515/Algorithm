def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    result = []
    
    for i in range(row_begin, row_end + 1):
        temp = 0
        for j in range(len(data[i - 1])):
             temp += data[i - 1][j] % i
        result.append(temp)
    
    answer = result[0]
    for i in range(1, len(result)):
        answer = answer ^ result[i]
    return answer