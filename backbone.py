userinput = input("Guess a letter")
print(userinput)
listofwords = [tree, car, nickel, hangman]
selectedword = random.choice(listofwords)
if userinput in selectedword:
  print("You guessed a letter correctly!")
else:
  print(Yyou've guessed a letter incorrectly!")
