from random import choice
from pprint import pprint

def word_chooser(path):
    word = choice(open(path,'r').readlines()).replace("\n",'')
    return {'name' : word,'guessed' : [' _ ']*len(word),"tries" : 3,'letters_guessed':0}

def checker(word,letter):
    return word['name'].count(letter)

def update(word,letter):
    number = checker(word,letter)
    
    if number != 0 and letter not in word['guessed']:
        print(f"There are {number} {letter}'s'")
        word['letters_guessed'] += number
        guess_detector(word,letter)
    elif number == 0 :
        print(f'Sorry there are no {letter}')
        word['tries'] -= 1
    elif letter in word['guessed']:
        print(f"You already guessed {letter}")

def position_detection(word,letter):
    return [counter for counter,item in enumerate(word['name']) if letter == item]

def guess_detector(word,letter):
    position = position_detection(word,letter)
    for item in position:
        word['guessed'][item] = letter


# logic

new_word = word_chooser("words.txt")

while new_word['letters_guessed'] != len(new_word['name']) or new_word['tries'] == 0:
    print(new_word['guessed'])
    user_input = input("\n ==>")
    update(new_word,user_input)

if new_word['tries'] == 0:
    print(f'You lost ! The word was {new_word["name"]}')
else:
    print('Congratulations')
