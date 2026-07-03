import random
stages = [
    # 0 lives left
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''',

    # 1 life left
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',

    # 2 lives left
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',

    # 3 lives left
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',

    # 4 lives left
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',

    # 5 lives left
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',

    # 6 lives left (start)
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

Word_list = ["apple", "banana" , "orange" , "guava", "pineapple"]
lives = 6

selected_word = random.choice(Word_list)
interger = int(len(selected_word))



placeholder = ""
for position in range(1,interger):
    position = "_"
    placeholder += position
print(placeholder)



game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a latter : ").lower()


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
          game_over == True
          print("You lose.")
          


    print(display)  
    if "_" not in display:
       game_over = True
       print("You win")

    print(stages[lives])   
             






