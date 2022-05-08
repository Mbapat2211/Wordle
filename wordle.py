import random

# the given dataset is copied into a text from where data is collected
with open('dataSet.txt') as f:
    data = f.read()

# selecting the word to be guessed
words = data.split('\n')
wordSelect = random.choice(words)

# start of the game
print('WORDLE')
print('------')
print('(@- Correct letter, #- Correct letter but wrong position, $- Incorrect letter)\n')

attempts = 1

while attempts <= 6:    
    inputWord = input('Attemps ' + str(attempts) + ': Enter a 5 letter word: \n')
    inputWord = inputWord.lower()

    if len(inputWord) != 5:
        print('Word is not 5 lettered. Try again!\n')  
    elif inputWord in words:
        answer = '\0'
        for index in range(0,5):
            if inputWord[index] == wordSelect[index]:
                answer = answer + '@'
            elif inputWord[index] in wordSelect:
                answer = answer + '#'
            else:
                answer = answer + '$'
        print(answer + '\n')
                
        if answer == '\0@@@@@':
            print('You have guessed the word correctly!!!')
            break
        
        attempts = attempts + 1
    else:
        print('Word not in list. Try again!\n')
               
if answer != '\0@@@@@':
    print('Sorry, you are out of attempts!')
    print('The word is: ' + wordSelect)
