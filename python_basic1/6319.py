def _reverse(word):
    r_word = ''
    for ch in word:
        r_word = ch + r_word
    return r_word

word = input()
r_word = _reverse(word)
print(r_word)
if word == r_word:
    print('입력하신 단어는 회문(Palindrome)입니다.')
