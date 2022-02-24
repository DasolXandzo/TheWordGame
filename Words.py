# Игра в слова (планируется внесение улучшений, но это вопрос времени)
def Last_Letter(word):
    letter = word[len(word) - 1:len(word)]
    if letter == 'ь' or letter == 'ъ':
        letter = word[len(word) - 2:len(word) - 1]
    return letter

def First_Letter(word):
    first_letter = word[0:1]
    return first_letter


print('------------------------------------ \nДобро пожаловать в игру Слова! \nЧтобы начать игру, введите "start" и нажмите Enter. \nДля ознакомления с правилами игры введите "rules" и нажмите Enter. \nЧтобы закончить игру, введите "stop" и нажмите Enter. \n------------------------------------')
menu = str(input())
if menu == 'rules':
    print('------------------------------------ \nПравила: \n 1) Участники поочереди вводят слова имени существительное. \n 2) Каждое новое слово должно начинаться с буквы, на которую заканчиволось предыдущее (не считая "ь" и "ъ"). \n 3) Слова не могут повторяться. \n 4) В случае, если слово называлось, необходимо ввести другое. \n 5) Если игрок не может назвать слово, он выбывает из игры, передавая ход следующему игроку. \n 6) После ввода слова необходимо нажать Enter. \n 7) Для завершения игры введите "stop" и нажмите Enter. \nДля начала игры нажмите Enter. \n------------------------------------')
    start = str(input())
    print('Игра началась! Удачи!')
elif menu == 'start':
    print('Игра началась! Удачи!')
elif menu == 'stop':
    print('Игра завершена. \nSee a next time!')
    exit()
else:
    print('------------------------------------ \nКоманды "', menu, '" нет в списке команд. \nСписок команд: \n start - начало игры \n rules - правила \n stop - завершение игры \n------------------------------------ \nВведите команду из списка и нажмите Enter:')

words_list = []

print('Введите первое слово. Оно может быть любым.')
word = str(input())
words_list.append(word)
letter = Last_Letter(word)

while True:
    print('Тебе слово на букву "', letter, '".')
    word = str(input())
    if word == 'stop':
        print('Игра завершена. \nSee a next time!')
        exit()
    if First_Letter(word) == letter:
        if word in words_list:
            print('Слово', word, 'уже было. Попробуйте другое.')
        else:
            words_list.append(word)
            letter = Last_Letter(word)
    else:
        print('Первая буква твего слова не "', letter, '", напиши другое слово.')