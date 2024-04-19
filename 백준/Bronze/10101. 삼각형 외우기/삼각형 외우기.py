A = int(input())
B = int(input())
C = int(input())

answer = "Error"
if (A + B + C) == 180:
    if A == B == C:
        answer = "Equilateral"
    else:
        answer = "Isosceles" if A == B or A == C or B == C else "Scalene"
print(answer)