# 모든 유저는 유저 아이디로 구분 -> 유저 아이디를 키, 닉네임을 value로 해서 딕셔너리 자료구조로 관리

def solution(record):
    answer = []
    
    user_info = {}
    for content in record:
        contentArr = content.split()
        if contentArr[0] == "Leave":
            answer.append([contentArr[1], "님이 나갔습니다."])
        else:
            if contentArr[0] == "Enter":
                answer.append([contentArr[1], "님이 들어왔습니다."])
            user_info[contentArr[1]] = contentArr[2]
    
    for i in range(len(answer)):
        answer[i] = user_info[answer[i][0]] + answer[i][1]
    
    return answer