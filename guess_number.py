# Guess a random number with minimal attempts. File winners.txt saves the three best results.
#
import random
import pickle

def file_update():
    file = open("winners.txt", "wb")
    pickle.dump(top_score, file)
    file.close()

top_score = []
isEmpty = False
try:
    file = open("winners.txt", "rb")
    pickle.load(file)
    file.close()
except:
    print('FILE EMPTY.Restart programme')
    isEmpty = True
    top_score = ['no name', 6]
    file_update()
else:
    file = open("winners.txt", "rb")
    top_score = pickle.load(file)
    file.close()

if not isEmpty:
    rand_num = random.randint(1, 5)
    attempts = -1
    count = 0
    while attempts != 0:
        user_answer = int(input(f'best results:{top_score}\n\t\tEnter your number in range 1 - 5: '))
        if user_answer == rand_num:
            print('\n\t!!YOU GUESSED THE NUMBER!!\t\n')
            attempts = 0
            count += 1
        else:
            print('\n\tNUMBER IS WRONG. Try again\t\n')
            count += 1
    if len(top_score) < 6:
        print(f'Your count of attempts: {count}')
        new_user_name = input('Write your name: ')
        top_score.append(new_user_name)
        top_score.append(count)
        file_update()
    elif len(top_score) == 6:
        mx = max(top_score[1], top_score[3], top_score[5])
        if mx > count:
            ind = top_score.index(mx)
            top_score.pop(ind)
            top_score.pop(ind-1)
            top_score.append(input('Whoah u use less attempts than someone, write your name: '))
            top_score.append(count)
            file_update()
        else:
            print("But you couldn't beat someone from 'List winners':(")
    if top_score[1] == top_score[3] == top_score[5] == 1:
        print('There are no more places in the "List of winners".\n\tGAME ENDED.\n\t')