def to_weird_case(string):
    answer = ""
    j = 0
    for i in range(0, len(string)):
        answer += string[i].upper() if j % 2 == 0 else string[i].lower()
        j = 0 if answer[-1] == ' ' else j + 1

    return "".join(answer)
