import random

def hangMan(guessCount):
	if guessCount == 0:
		print("|----|")
		print("|     ")
		print("|")
		print("|")
		print("|______")
		print("|______|")
	
	elif guessCount == 1:
		print("|----|")
		print("|    O")
		print("|")
		print("|")
		print("|______")
		print("|______|")	
	
	elif guessCount == 2:
		print("|----|")
		print("|    O")	
		print("|    |")
		print("|")
		print("|______")
		print("|______|")	
		
	elif guessCount == 3:
		print("|----|")
		print("|    O")	
		print("|   /|")
		print("|")
		print("|______")
		print("|______|")
	
	
	elif guessCount == 4:
		print("|----|")
		print("|    O")	
		print("|   /|l")
		print("|")
		print("|______")
		print("|______|")	
	
	elif guessCount == 5:
		print("|----|")
		print("|    O")	
		print("|   /|l")
		print("|   /  ")
		print("|______")
		print("|______|")
		
	elif guessCount == 6:
		print("|----|")
		print("|    O")	
		print("|   /|l")
		print("|   / \ ")
		print("|______")
		print("|______|")		
	

def randWord():
	fileArr = []
	for line in open('SOWPODS.txt', 'r'): #this code is faster than the while alternative.
		fileArr.append(line.strip().lower())
		
	return random.choice(fileArr)

def gameLogic(word):
	guessCount = 0
	guessLog = []
	guessWord = ["_" for elem in word]
	print("------------------------------------------------------------------------")
	print("Welcome to Hangman.  Here is your word to guess: ", " ".join(guessWord))
	
	while "".join(guessWord) != word and guessCount < 6: #loop breaks if user guesses word, or if guess count is reached.
		print("----------------------------")
		userGuess = input("Guess a letter: ")
		
		if userGuess not in guessWord and len(userGuess) == 1 and userGuess not in guessLog:    #checks to see if user already guessed.. if false see else below.
			
			if userGuess not in word:           
				print("Uh oh. Wrong letter.")
				guessCount += 1
				hangMan(guessCount)
				
			else:
				
				hangMan(guessCount)
			
			for i in range(0, len(word)):
				if userGuess == word[i] and len(userGuess) == 1:
					guessWord[i] = userGuess
			guessLog.append(userGuess)
			print("Heres the word: ", " ".join(guessWord))
			print("Your guesses are: ", ",".join(guessLog))
		
		elif len(userGuess) != 1:
			print("Try a guess with one letter please.")
								
		elif userGuess in guessLog:
			print("Oops! You already guessed that, try a different letter!")
			
	
	if guessCount == 6:
		print("Ah. Too bad, this man got hanged.")
		return "loss"
	else:
		print("You won!! Congrats")
		return "win"
	
	
if __name__=="__main__":
	winCount = 0
	loseCount = 0
	playAgain = "yes"
	while playAgain == "yes":
		word = randWord()
		winOrLose = gameLogic(word)
		print("The word was: ", word)
		if winOrLose == "win":
			winCount += 1
		else: 
			loseCount += 1
		playAgain = input("Play Again (yes/no)? ")
	
	print("Thanks for playing. You won {} times and lost {} times.".format(winCount, loseCount))
			
		
	
	