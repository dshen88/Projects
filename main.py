import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

display = []
chosen_list = []
game_over = False
lives = 6

    #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
def hangman():
    print(logo)
    chosen_word = random.choice(word_list)
    for char in chosen_word:
        chosen_list.append(char)

    for char in chosen_list:
        display.append('_')

    guessed_letters = set()

    def hp(guess):
        global lives
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])

    while lives > 0:
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        else:
            guessed_letters.add(guess)

        position = len(chosen_word) - 1

        for char in chosen_word:
            position -= 1
            if chosen_word[position] == guess:
                display[position] = guess

        hp(guess)

        joined_disp = ''.join(display)

        if joined_disp == chosen_word:
            print(f'{joined_disp} \nYou won!')
            break
        print(f'{joined_disp} \nYou have {lives} lives left. ')
        if lives == 0:
            print(chosen_word)
            print('Game over')
            break

hangman()
