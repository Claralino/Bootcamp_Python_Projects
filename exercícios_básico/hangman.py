from pickle import FALSE
import random
import hangman_words
import hangman_stages

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

display = []

lives = 6

letters_repeat = []

print(hangman_stages.logo)

chosen_word = random.choice(hangman_words.word_list)


for letter in chosen_word:
    display.append("_")


end_of_game = False
while not end_of_game:

    chosen_letter = input("guess a letter: ").lower()

    if chosen_letter not in letters_repeat:
        letters_repeat.append(chosen_letter)
    else:
        print(f"you alredy guessed that letter: {chosen_letter}")
    
    if chosen_letter not in chosen_word:
        lives -= 1
        print(f"{chosen_letter} is not in the word, you lose a life")
        if lives == 0:
            end_of_game = True
            print("you lose")
        

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == chosen_letter:
            display[position] = letter

    
        
    print(display)
    print(stages[lives])
    

    if "_" not in display:   
        end_of_game = True
        print("you win!")






