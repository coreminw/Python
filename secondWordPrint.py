def word(str):
    s = str.strip()
    if s.find(' ') == -1:
        print('빈 문자열이 출력되었습니다.')
        return ' '
    idx = s.find(' ')
    second = s[idx+1:].strip()
    return second

print(word("hello    "))
print(word("hello world"), len(word("hello world")))
print(word("hello     world"), len(word("hello     world")))
print(word("hello     world         "), len(word("hello     world         ")))