#Код был взят из интернета, мы проставили комментарии, и дополнили код выбором темы. Задание делалось совместно с Василисой Осиповой.  
import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'муравей бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()
words1 = 'отец сын бабушка мать тётя племянница кузен сваха зять тёща тесть дочь сестра брат'.split()
words2 = 'торт хлеб молоко сметана помидор огурец авокадо банан яблоко маслины оливки макароны греча киноа кисель компот оливье  '.split()
words3 = '1)животные 2)семья 3)продукты'.split()
def getRandomWord(wordList):
    #Эта функция возвращает случайное слово, которое выбирает из заранее созданного списка
    wordIndex = random.randint(0, len(wordList) - 1) #для каждого слова из списка генерируется свой индекс
    return wordList[wordIndex] #происходит возврат случайного слова из списка, соответствующему случайному индексу 

def displayBoard(HANGMANPICS, missedletters, correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)]) #рисует виселицу в соотвествии с количеством допущенных ошибок ( пропущенных букв)
    print()

    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '*'*len(secretWord) #определяет длину загаданного слова и выставляет соответствующее количество звездочек 

    for i in  range(len(secretWord)):#Заменяем звездочки на правильно угаданные буквы
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Показываем загаданное слово с пробелами между буквами
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Возвращает букву, которую ввел игрок. Эта функция проверяет, что введена буква, а не какой-то другой символ
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print ('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

def playAgain():
    #Эта функция возвращает True если игрок решит сыграть еще раз. В противном случае возвращается False
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''

print('Привет! Давай поиграем в "Виселицу"! Выбери тему: 1)животные 2)семья 3)продукты. Введи, пожалуйста, цифру 1,2 или 3 в зависимости от выбранной темы. ')
a = input()
if a == '1':
    secretWord = getRandomWord(words)
elif a == '2':
    secretWord = getRandomWord(words1)
elif a == '3':
    secretWord = getRandomWord(words2)
else:
    print ('Чтобы играть, нужно ввести цифру 1,2 или 3.')

gameIsDone = False
    
    
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord) #вызов функции, которая позволяет играть и рисует виселицу 

    #Вычисляем количество букв, которые ввел игрок
	
    guess = getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Проверка условия победы игрока
        foundAllLetters = True #означает, что все буквы угаданы, однако нужно удостовериться, что они стоят в нужном порядке, т.е сравнить каждую с каждой 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters: 
                foundAllLetters = False
                break 
        if foundAllLetters:
            print('Превосходно! Было загадано слово "'+secretWord+'"! Вы победили!')

            gameIsDone = True
    else:
        missedLetters = missedLetters+guess

        #Проверка условия проигрыша игрока
        if len(missedLetters) == len(HANGMANPICS) - 1: # после 6ой попытки (len - 1)  у игрока кончаются попытки 
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('У вас не осталось попыток!\nПосле '+str(len(missedLetters))+' ошибок и '+str(len(correctLetters))+'угаданных букв. Загаданное слово:'+secretWord+'"')
            gameIsDone = True

        
        
            

            
      
