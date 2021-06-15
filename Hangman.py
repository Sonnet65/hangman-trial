import random
from wordslist import word_list
from images import *
import time

print(logo)
time.sleep(1)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
endgame = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not endgame:
    guess = input("Guess a letter: \n").lower()
    time.sleep(0.5)

    if guess in display:
        print(f"you already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        time.sleep(1)
        print(f"you guessed {guess}, that's not in the word. You lost a life")
        print("you have " + str(lives - 1) + " lives left...")
        lives -= 1
        if lives == 0:
            endgame = True
            print(f"You lose, the answer is {chosen_word}")

    if not "_" in display:
        endgame = True
        time.sleep(1)
        print("You won")

    print(stages[lives])
