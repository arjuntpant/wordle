import random
import tkinter as Tk

def clickButton():
  clickButton = Label(Tk,text="Welcome to Wordle! Guess a word with 5 letters. Then it will tell you what the letters are. If the letter is Green, that means the word has that letter in the same position. If it is yellow, that means that letter is in the word, but in a different position. If it is grey, that means the letter is not in the word. If the word is not in the dictionary, then don't guess it. if you guess the word in 6 tries or less, you win. If you guess the word in more tries, you lose. Press this text to start the game.")
  clickButton.pack()
StartButton = Button(text="Start Game", padx = 200, pady = 40)
StartButton.pack()
("Welcome to Wordle! Guess a word with 5 letters. Then it will tell you what the letters are. If the letter is Green, that means the word has that letter in the same position. If it is yellow, that means that letter is in the word, but in a different position. If it is grey, that means the letter is not in the word. If the word is not in the dictionary, then don't guess it. if you guess the word in 6 tries or less, you win. If you guess the word in more tries, you lose. Press this text to start the game.").replace(" ","\n")
wordbank = ["Thorn", "Sharp", "Tiger", "Slyly", "Gamer", "Bunny", "Happy" , "Pooly" , "Grunt", "Piggy"]
word = (random.choice (wordbank))


def letter_checker(guessletter, position, word):
  if guessletter == word[position]:
    print (guessletter, "= Green")
    return
  else:
    for i in range(0, 5):
      if i == position:
        break;
      if guessletter == word[i]:
        print (guessletter, "= Yellow")
        return
  print (guessletter, "= Grey")
    


def SC(Guess):
  for i in range(0, 5):
    letter_checker(Guess[i], i, word)
  

FirstWord = input("Enter the first word: ")
if FirstWord == word:
  print ("You chose the correct word! ")
else:
  print (SC(FirstWord))
  SecondWord = input("Enter the second word: ")
  if SecondWord == word:
    print ("You chose the correct word! ")
  else:
    print (SC(SecondWord))
    ThirdWord = input("Enter the third word: ")
    if ThirdWord == word:
      print ("You chose the correct word! ")
    else:
      print (SC(ThirdWord))
      FourthWord = input("Enter the fourth word: ")
      if FourthWord == word:
        print ("You chose the correct word! ")
      else:
        print (SC(FourthWord))
        FifthWord = input("Enter the fifth word: ")
        if FifthWord == word:
          print ("You chose the correct word! ")
        else:
          print (SC(FifthWord))
          SixthWord = input("Enter the sixth word: ")
          if SixthWord == word:
            print ("You chose the correct word! ")
          else:
            print ("The word was" + word)