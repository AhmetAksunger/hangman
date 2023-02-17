import random
import string

words = open("C:/Users/90538/Desktop/PYTHON VISUAL CODE/Hangman/wordlist.txt","r")
iswin = False
word_list = []
for word in words:
    word_list.append(word)

def game(list):
    selected_word = random.choice(word_list)
    template_string = []
    for i in range(len(selected_word) - 1):
        template_string.append("-")
    playagain = ""
    iswin = False
    guess_chance = 6
    guessed_letter = ""
    guessed_letter_set = set()
    while guess_chance > 0:
        if "-" not in template_string and "".join(template_string) == selected_word.upper().strip():
            iswin = True
            break
        print("You have " + str(guess_chance) + " lives left and the letters you have used are: " + " , ".join(guessed_letter_set) )
        print("Current word: " + "".join(template_string))
        guessed_letter = input("Enter your guess: ")
        isletter = True
        if len(guessed_letter) == 1:
            isletter = True
        else:
            isletter = False
        if guessed_letter.upper() in string.ascii_uppercase and isletter:
            if guessed_letter.upper() in guessed_letter_set:
                print("You have already guessed that letter, enter another guess!")
            elif guessed_letter.upper() in selected_word.upper():
                guess_chance -= 1
                guessed_letter_set.add(guessed_letter.upper())
                for i in range(len(selected_word) - 1):                         #TEMPLATE STRING CHANGER
                    if selected_word[i].upper() == guessed_letter.upper():      #TEMPLATE STRING CHANGER
                        template_string[i] = guessed_letter.upper()             #TEMPLATE STRING CHANGER
            else:
                guess_chance -= 1
                guessed_letter_set.add(guessed_letter.upper())

        elif guessed_letter.upper() not in string.ascii_uppercase and isletter:
            print("Enter a valid guess")

        
        if guessed_letter.upper() == selected_word.upper().strip() and not isletter:
                iswin = True
                break
        elif not isletter and guessed_letter.upper() != selected_word.upper().strip():
            guess_chance -= 1
    if not iswin:
        print("Out of guesses! " + "The word was " + selected_word)
    else:
        print("You have successfully guessed the word! Congrats!")
    playagain = input("Do you want to play again? (y/n): ")
    if playagain == "y":
        game(word_list)
    else:
        print("terminating...")
        quit()

game(word_list)


