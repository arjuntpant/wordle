import random
from tkinter import *

root = Tk()
root.geometry("1600x1200")

def clickButton():
  clickButton = Label(root, text="Welcome to Wordle! Guess a word with 5 letters. Then it will tell you what the letters are. If the letter is Green, that means the word has that letter in the same position. If it is yellow, that means that letter is in the word, but in a different position. If it is grey, that means the letter is not in the word. If the word is not in the dictionary, then don't guess it. if you guess the word in 6 tries or less, you win. If you guess the word in more tries, you lose. Press this text to start the game.")
  clickButton.pack()


wordbank = ["Bunny" , "Thorn" , "Share" , "Spare" , "Stare", "Stair", "Snair", "Scare" , "Stain", "Spank", "Shank", "Shard"]

word = (random.choice (wordbank))


def letter_checker(guessletter, position, word):
  if guessletter == word[position]:
    #Label(root, text=guessletter+" = Green")
    return "Green"
  else:
    for i in range(0, 5):
      if i == position:
        break;
      if guessletter == word[i]:
        #Label(root, text=guessletter+ " = Yellow")
        return "Yellow"
  #Label(root, text=guessletter+ " = Grey")
  return "Grey"
    


def SC(Guess):
  for i in range(0, 5):
    letter_checker(Guess[i], i, word)

def pri():
  e = Entry(root)
  e.pack()
  user = e.get()
  myButton = Button(root, user, text="Submit") 
  myButton.pack()
  myButton.focus()

FirstWord = pri()
if FirstWord == word:
  Label(root, text="You chose the correct word! ")
else:
  Label(root, text=SC(FirstWord))
  SecondWord = pri()
  if SecondWord == word:
    Label(root, text="You chose the correct word! ")
  else:
    Label(root, text=SC(SecondWord))
    ThirdWord = pri()
    if ThirdWord == word:
      Label(root, text="You chose the correct word! ")
    else:
      (SC(ThirdWord))
      FourthWord = pri()
      if FourthWord == word:
        Label(root, text="You chose the correct word! ")
      else:
        print (SC(FourthWord))
        FifthWord = pri()
        if FifthWord == word:
          Label(root, text="You chose the correct word! ")
        else:
          print (SC(FifthWord))
          SixthWord = pri()
          if SixthWord == word:
            Label(root, text="You chose the correct word! ")
          else:
            Label(root, text="The word was" + word)

root.mainloop()
