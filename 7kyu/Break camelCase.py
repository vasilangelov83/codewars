def solution(s):
    new_s = ""
    for index in range(len(s)):
        if s[index].isupper():
            new_s += " "
        new_s += s[index]
    return print(new_s)
solution("helloWorld")
solution("breakCamelCase")
