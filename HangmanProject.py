from words import words # imports a list of common words I found from 
https://github.com/kying18/hangman/blob/master/words.py

import random 
import os

"""gets a random word from the imported list, then to make sure its valid, it checks if there 
is a 
space or a dash in the word, and if there is it gets a new word. Returns an uppercase word so 
it can match with the input of the user """
def get_a_word(words):
    word = (random.choice(words)).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

"""This function gets the players letter and returns it, the function checks if the players 
guess isnt a letter, if they already guessed it,
or if it is multiple letters, and if its is it makes them guess again, once it gets a valid 
letter it appends it to a list of every guessed 
letter"""
def player_input(guessed_letters):
    player_guess = (input("Enter A Letter: ")).upper()
    while not player_guess.isalpha() or player_guess in guessed_letters or len(player_guess) > 1:
        if player_guess in guessed_letters:
            print("You Already Guessed That")
        else:
            print("Not a Valid Guess")
        player_guess = (input("Enter a Guess: ")).upper()
    guessed_letters.append(player_guess)

    return player_guess

"""The "dashed list" is initalized in another function, it is a list of dashes in the length 
of the word, where each dash corisponds to one
letter of the word. This function sees if the players guess is correct and then replaces the 
dash from its list with the correct letter, in 
the correct position. If the player has not won already, get another letter. Then if the 
letter is correct append the index(s) of the correct
letter(s) into a list. Then using that list of indexes, it changes the dash list with that 
index with the list of the word letters of the 
same index. If the guess is incorrect, it appends it to a list of every incorrect guess."""

def hangman(word_list, dashed_list, guessed_letters, wrong_guess):
    indexes = []
    if dashed_list != word_list:
        player_guess = player_input(guessed_letters)

        if player_guess in word_list:

            for i in range(len(word_list)): 
                if word_list[i] == player_guess: 
                    indexes.append(i)
            for element in indexes: 
                dashed_list[element] = word_list[element] 

        else:
            wrong_guess.append(player_guess) 

        return dashed_list 
    
"""this function prints the handman board by looking at the ammount of incorrect guesses 
since 1 wrong guess is a life lost. 
' '.join(dashed_list) seperates each item in the list with a space so it doesnt display the 
brackets and commas in the list. Inthe main 
function if i run win as true then it prints the win board, otherwise if i dont put anthing 
then win automatically = false"""
def board(dashed_list, word_list, guessed_letters, wrong_guess, win = False):
    turns = len(wrong_guess)
    if win == True:
        os.system('cls')
        print(f"""

    ____
   |    |        YOU WIN!
   |         
   |    
   |   
   | 
  _|_                0    yay!
 |   |______        \|/
 |          |        |
 |__________|       / \\
 
 phrase: {' '.join(word_list)}""")
    else: 
        if turns == 0:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   6
      |             Guessed : {wrong_guess}
      |        
      |    
      |  
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)
        
        elif turns == 1:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   5
      |    0        Guessed : {wrong_guess} 
      |        
      |    
      |  
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)
        
        elif turns == 2:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   4
      |    0        Guessed : {wrong_guess}
      |    |    
      |    |
      |  
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)

        elif turns == 3:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   3
      |    0        Guessed : {wrong_guess}
      |    |    
      |    |
      |   / 
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)
        
        elif turns == 4:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   2
      |    0        Guessed : {wrong_guess}
      |    |    
      |    |
      |   / \\
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)
        
        
        elif turns == 5:
            os.system('cls')
            print(f"""

       ____
      |    |        lives :   1
      |    0         Guessed : {wrong_guess}
      |   \|    
      |    |
      |   / \\
     _|_
    |   |______
    |          |
    |__________|

    phrase: {' '.join(dashed_list)}""")
            hangman(word_list, dashed_list, guessed_letters, wrong_guess)
        
        else:
            os.system('cls')
            print(f"""

       ____
      |    |        YOU LOOSE!
      |    0         
      |   \|/   
      |    |
      |   / \\
     _|_
    |   |______
    |          |
    |__________|
 
    phrase: {' '.join(dashed_list)}""")
        
"""This is the function where everything is run. It has a while loop that keeps going until 
they either guess it or loose. Inside the loop
it checks if the player won. Since the word list stays the same, and every correct letter 
guessed replaces the dash at its corrisponding index,
if you guess every letter in the word, the dashed list will only be letters while the word 
list is the same. """
def main():
    word = get_a_word(words)
    word_list = list(word) 
    dashed_list = list('-' * len(word)) 
    guessed_letters = [] 
    wrong_guess = []

    while True:
        if dashed_list == word_list:
            board(dashed_list, word_list, guessed_letters, wrong_guess, True)
            print(f"You Won With {6 - (len(wrong_guess)) } Lives Left") 
            break
        elif len(wrong_guess) > 5:
            board(word_list, word_list, guessed_letters, wrong_guess)
            break
        else:
            board(dashed_list, word_list, guessed_letters, wrong_guess)           
 
main()
