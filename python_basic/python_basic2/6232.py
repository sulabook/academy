data_str = input()
palindrome = True
i = 0
while i < len(data_str) // 2 and palindrome:
    if len(data_str) <= 0:
        break
    if data_str[i] != data_str[-(i + 1)]:
        palindrome = False
    i += 1

print(data_str)
if palindrome:
    print('입력하신 단어는 회문(Palindrome)입니다.')
