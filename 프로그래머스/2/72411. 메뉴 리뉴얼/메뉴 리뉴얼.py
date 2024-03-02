from itertools import combinations

def solution(orders, course):
    answer = []
    for num in course:
        dic = {}
        for order in orders:
            for menus in combinations(order, num):
                menus = ''.join(sorted(list(menus)))
                dic[menus] = dic.get(menus, 0) + 1
            
        lst = [(key, val) for key, val in dic.items() if val > 1]
        if lst:
            lst.sort(key=lambda x: -x[1])
            temp = [key for key, val in lst if val == lst[0][1]]
            answer.extend(temp)
    
    answer.sort()
    return answer