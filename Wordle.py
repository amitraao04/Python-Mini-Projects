# How It Works
# In Wordle, your objective is to guess a secret five-letter word within six attempts. Here's how you play:

# Make a Guess: Start by typing in any five-letter word you think might be the secret word.

# Get Feedback: After each guess, you'll receive color-coded feedback:

# 🟩 Green: The letter is in the correct position.
# 🟨 Yellow: The letter is in the word but in the wrong position.
# ⬛ Black: The letter isn't in the word at all.
# Use the Clues: Use these clues to refine your next guesses. Keep guessing until you find the secret word or run out of attempts.

# 1) Import random.
# 2) Define a list of sample words.
# 3) Define the isword function to compare the guessed word with the target word and provide feedback.
# 4) Select a random word from the list of sample words.
# 5) Print a welcome message.
# 6) Define congratulatory messages for successful guesses and set attempts to 6.
# 7) Start a game loop that runs while attempts are greater than 0:
# 8) Prompt the user to enter a 5-letter word.
# 9) Validate the input and call the isword function if valid.
# 10) Print a congratulatory message and break the loop if the word is correct.
# 11) Print an error message if the input is invalid.
# 12) Print the correct word if all attempts are exhausted.
# ⬛ 🟩 🟨



import random

# Sample word list
words = ["apple", "grape", "mango", "berry", "lemon",
    "peach", "melon", "plumb", "guava", "zebra",
    "tiger", "panda", "horse", "eagle", "shark",
    "whale", "snake", "crane", "robin", "broom",
    "grass", "cloud", "stone", "dream", "ocean"]

def isword(user_word, wordly_word):
    for x in user_word:
        print(x, end="  ")
    print()
    
    feedback = ['⬛'] * len(user_word)  # Initialize feedback list with black squares
    wordly_word_remaining = list(wordly_word)  # Keep track of remaining letters to match
    
    # First pass: Check for correct letters in correct positions (green)
    for i in range(len(user_word)):
        if user_word[i] == wordly_word[i]:
            feedback[i] = '🟩'
            wordly_word_remaining[i] = None  # Mark this letter as matched
    
    # Second pass: Check for correct letters in incorrect positions (yellow)
    for i in range(len(user_word)):
        if feedback[i] == '⬛' and user_word[i] in wordly_word_remaining:
            feedback[i] = '🟨'
            wordly_word_remaining[wordly_word_remaining.index(user_word[i])] = None  # Mark this letter as matched
    
    # Print feedback
    for f in feedback:
        print(f, end="")
    print()
    
    # Return true if the guessed word matches the target word
    return user_word == wordly_word

random_word = random.choice(words)
# print(random_word)  # For testing purposes, remove this line in the actual game
print("Let's Play Wordle")

# Messages for successful guesses
messages = {0: "Marvellous", 1: "Excellent", 2: "Very good", 3: "Nice", 4: "Good", 5: "Ok"}
attempts = 0

while attempts < 6:
    user_word = input("\nEnter word: ").lower()
    if len(user_word) == 5 and user_word.isalpha():
        attempts += 1
        print("Number of attempts left = ",6-attempts)
        if isword(user_word, random_word):
            print("\n", messages[attempts-1])
            break
    else:
        print("Please enter a valid word")
print("End of Game, the correct word is:", random_word)
