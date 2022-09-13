import os
from tkinter import W

hangman_frame = [
	"""





	""",
	"""




	====== 
	""",
	"""

	|
	|
	|
	|
	|
	====== 
	""",
	"""
	-----
	|
	|
	|
	|
	|
	====== 
	""",
	"""
	-----
	|/
	|
	|
	|
	|
	====== 
	""",
	"""
	-----
	|/  |
	|
	|
	|
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|
	|
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|   X
	|
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|  /X
	|  
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|  /X\\
	|
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|  /X\\
	|  /
	|
	====== 
	""",
	"""
	-----
	|/  |
	|   o
	|  /X\\
	|  //
	|
	====== 
	"""
]

word = "tennisball" # should be a randomly generated sequence though

guesses = {"correct": [], "incorrect": []}

def print_hangman(level):
	print(hangman_frame[level])

def reveal_chars(word, matched_chars):
	for c in word:
		if c in matched_chars:
			print(f"{c} ", end='')
		else:
			print(f"_ ", end='')
	print("\n")

def evaluate_guess(guess, word):
	if (guess in guesses["correct"] or guess in guesses["incorrect"]):
		print(f"You already guessed '{guess}'")
	elif (guess in word):
		guesses["correct"].append(guess)
	else:
		print(f"'{guess}' is not in the word\n")
		guesses["incorrect"].append(guess)
	reveal_chars(word, guesses["correct"])
	print_hangman(len(guesses["incorrect"]))

reveal_chars(word, guesses["correct"])
while (1):
	guessed_letter = input("Please guess a letter: ")
	os.system('clear')
	evaluate_guess(guessed_letter, word)
	if len(guesses["correct"]) == len(word):
		print("Congratulations, you won the game!")
		break
	elif len(guesses["incorrect"]) == len(hangman_frame) - 1:
		print("Game over. :(")
		print(f"The solution is: {word}")
		break

