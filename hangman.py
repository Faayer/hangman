import random

from hangman_words import words

from hangman_art import stages

from logo import logor
print(logor)



lives = 6

selected_word = random.choice(words)
interger = (len(selected_word))



placeholder = ""
for _ in selected_word:
    placeholder += "_"
print(placeholder)



game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a latter : ").lower()

    if guess in correct_letters:
       print("you have already choosen this letter")


    display = ""

    for letter in selected_word:
        if letter == guess:
           display += letter
           correct_letters.append(letter)
        elif letter in correct_letters:
           display += letter   
        else:
          display +="_"
    
    if guess not in selected_word:
       lives -= 1
       if lives == 0:
          game_over = True
          print("------------------------You lose.---------------------")
          


    print(display)  
    if "_" not in display:
       game_over = True
       print("__________________You win________________________________")

    print(stages[lives])   
             







       




