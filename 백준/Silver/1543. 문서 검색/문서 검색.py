def solution():
    string = input()
    word = input()

    result = 0

    while (after := string.replace(word, "!", 1)) != string:
        result += 1
        string = after

    print(result)


solution()