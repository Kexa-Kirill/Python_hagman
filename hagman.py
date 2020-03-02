import random


HAGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
       |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /   |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''', '''       
''']

words = 'фист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк ' \
        'кит кобра коза козел  койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лягушка ' \
        'медведь молюск моль мул муравей мыш норка обезъяна овца окунь олень орел осел панда паук питон попугай пума ' \
        'семга скунс собака сова тигр тритон утра форель хорек черепаха ястреб ящерица'.split()


def getRandomWord(wordList):
    #  Эта функция возвращает случайную строку из списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HAGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Заменять пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    #  Возвращает букву, введенную игроком. Эта функция проверяет что игрок ввел только одну будкву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфччшщьъэюя':
            print('Пожалуйста введите БУКВУ.')
        else:
            return guess


def playАgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случает возвращает False.
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # проверяет выгирал ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #  Проверяет, превысил ли игрок ппопыток и проиграл.
        if len(missedLetters) == len(HAGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все поптыки! \nНеугаданно букв: ' + str(len(missedLetters)) + ' и угадав букв: ' + str(
                len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone = True
        #  запрашивает, хочет ли игрок играть зановов(только если игра завершина
    if gameIsDone:
        if playАgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break