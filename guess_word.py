# classic game - guess the word - field of miracles
import random
word = random.choice(['hello', 'tree', 'keyboard', 'car'])
tmp=word
print(len(word)*'*')

while True:
    letter = input('You letter or answer: ')
    for i in range(len(word)):
        if word[i] == letter:
            tmp = tmp.replace(letter,'*')
    # print('tmp=',tmp)
    text = ''
    for i in range(len(word)):
        if tmp[i] != '*':
            text += '*'
        else:
            text += word[i]
    print(text)
    if letter == word or text == word:
        print('You win')
        break
