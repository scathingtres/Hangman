from english_words import english_words_lower_set as words
import random as rand
from draw import Draw


class Game:

    def __init__(self, lives=6):
        self.word = [i for i in rand.choice(list(words))]
        self.hangman_drawing = Draw()
        self.hangman_drawing.draw()
        self.guess = ['_' for _ in self.word]
        self.lives = lives
        self.state = 3  # game state 0  -lost 1 -won

    def check(self, selected):
        if not selected.isalpha() or selected.isupper():
            return 'Only lowercase letters are allowed'
        if selected in self.word:
            for ind in [i for i, x in enumerate(self.word) if x == selected]:
                self.guess[ind] = selected

        else:
            self.hangman_drawing.draw()
            self.lives -= 1

        return

    def update_state(self):
        if self.guess == self.word:
            self.state = 1
        if self.lives == 0:
            self.state = 0





if __name__ =='__main__':
    while True:
        gam = Game()
       # h, w = stdscr.getmaxyx()
        print(''.join(gam.word))
        while True:

            selected = input('<<')
            gam.check(selected)
            gam.update_state()
            print(''.join(gam.guess))
            if gam.state == 0:
                break
        break


