from pyfiglet import Figlet

title = Figlet(font='pebbles').renderText('Hangman\n Game')

with open('hangman_logo.txt') as f:
    logo = f.read()
logo = logo +'\n'+ title

print(logo)