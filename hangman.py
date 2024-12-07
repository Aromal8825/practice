# hangman
from wonderwords import RandomWord
r = RandomWord()
word = r.word()
answer = word
blank = ["_"] * len(answer)
guessed_letters = []

def display_blanks():
   print("  ".join(blank))

def display_guessed_letters():
    if len(guessed_letters) >= 1:
        print("already guessed letters = ", end = " ")
        print(" ".join(guessed_letters))

def display_hangman(wrong_guess):
   hangman = {0:("\n""\n""\n"),
            1:(" O\n"" \n"" \n"),
            2:(" O\n""/ \n"" \n"),
            3:(" O\n""/""|\n"),
            4:(" O\n""/""|""\\\n"),
            5:(" O\n""/""|""\\\n""/\n"),
            6:(" O\n""/""|""\\\n""/"" \\\n")
            }
   print(hangman[wrong_guess])
   
def check():     
   win = 0
   for _ in range(len(answer)):
      if "_"  not in blank:
         win = 1
      else:
         break
   if win == 1: 
      print("\nyou win word = ", end= "") 
      display_blanks()
      return True

def start_game():
    wrong_guess = 0
    while True:
        display_guessed_letters()
        print("fill in the blanks :  ", end = "")
        display_blanks()
        guess = input("\nguess a letter : ").lower()
        guessed_letters.append(guess)
        if len(guess) != 1:
            print("invalid input \n")
            continue
        for i in range(len(answer)):
            if answer[i] in guess:
                blank[i] = guess
        if guess not in answer:
            wrong_guess += 1 
            if wrong_guess == 6:
                display_hangman(wrong_guess)
                print("\n you loose \n")
                print("corrrect answer = ", answer)
                break
        display_hangman(wrong_guess)
        if check() == True:
            break
start_game()
