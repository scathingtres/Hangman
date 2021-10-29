from english_words import english_words_lower_set as words
import random as rand
from draw import Draw
import curses
word = rand.choice(list(words))
guess = ['_' for _ in word]
lives = 6
hangman = Draw()
hangman.draw()
print(word)
while True:
    letter = str(input('Select a letter \n'))
    while(not letter.isalpha()):
        print('this is not a letter \n')
        letter = str(input('Select a letter \n'))
    if letter in word:
       for ind in [i for i, x in enumerate(word) if x == letter]:
           guess[ind] = letter
       print(guess)
       if guess == word:
           print(hangman)
           print('WON!')
           break
    else:
        hangman.draw()
        print(hangman)
        lives -= 1
        print(f'Lives left {lives}')
        if lives == 0:

            print('LOSE!')
            break
