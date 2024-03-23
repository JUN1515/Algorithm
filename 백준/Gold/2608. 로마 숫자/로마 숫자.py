def romaToArabia(s):
    roma = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
    roma2 = {"IV": 4, "IX": 9, "XL": 40, "XC":90, "CD":400, "CM":900}
    romaArr = [1, 5, 10, 50, 100, 500, 1000]
    result = 0
    i = 1
    while (i < len(s)):
        if roma[s[i-1]] >= roma[s[i]]:
            result += romaArr[roma[s[i-1]]]
            i += 1
        else:
            result += roma2[s[i-1: i+1]]
            i += 2

    if i == len(s):
        result += romaArr[roma[s[i-1]]]
    return result

def arabiaToRoma(num):
    roma_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roma_str = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    s = ""
    top = 0
    while num > 0:
        while num >= roma_num[top]:
            s += roma_str[top]
            num -= roma_num[top]
        top += 1
    return s


def solution():
    s1 = input().strip()
    s2 = input().strip()

    num = romaToArabia(s1) + romaToArabia(s2)
    print(num)

    str = arabiaToRoma(num)
    print(str)


solution()