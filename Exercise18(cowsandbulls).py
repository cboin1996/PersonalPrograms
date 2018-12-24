#Digit in right place: cow
#digit in worng place: bull


import random

def inputLogic(): #makes sure inputs are valid
	userIn = input("Enter a 4 digit number: ")
	if userIn == "quit":
		return userIn
	
	elif userIn.isdigit() and len(userIn) == 4:
		return userIn 
	else:
		print("Unknown input. Type 'quit' or a 4 digit number")
		return "unknown"

def gameLogic(randomNum, guessNum):
	cowBullCount = [0,0] #cow is index 0, bull index 1
	guessNum = list(guessNum)  #converts the string to list
	randomNum = list(str(randomNum)) #converts integer to string then list
	index = 0		
	for i in guessNum:
		if i in randomNum[index]:
			cowBullCount[0] += 1
		elif i in randomNum:
			cowBullCount[1] += 1
		index += 1
	return cowBullCount
		
def cowsAndBulls():
	quitStr = ""
	randNum = random.randint(1000,9999)
	userGuess = ""
	cowbull = []
	guessCount = 0

	print("Welcome to 'Cows and Bulls'\nI have generated a number between 1000<=number<=9999, can you guess it?")
	print("At any time, type quit to stop playing")

	while quitStr != "quit" and userGuess != str(randNum): #userGuess will be a string.. so thats why randNum is conv to a string
		userGuess = inputLogic()

		if userGuess == "quit": 
			print("Thanks for playing.  Goodbye.")
			quitStr = userGuess
		
		if userGuess.isdigit() and userGuess != randNum: 
			
			#print(userGuess)
			#print(randNum) this is here for troubleshooting
			cowbull = gameLogic(randNum, userGuess)
			guessCount += 1
			print("You have {} cow(s) and {} bull(s)".format(cowbull[0], cowbull[1]))
			print("-----------------------------------")
			if cowbull[0] == 4 and guessCount > 10:
				print("You won, in {} guesses.  What, am I supposed to be impressed?".format(guessCount))
			elif cowbull[0] == 4 and guessCount <= 10:
				print("You won, in {} guesses.  Perhaps your not so bad after all".format(guessCount))
if __name__=="__main__":
	cowsAndBulls()