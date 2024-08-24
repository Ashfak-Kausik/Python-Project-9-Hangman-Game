import random

def hangman():
    # List of words to choose from
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'engineering', 'software', 'hardware', 'development']
    
    # Randomly select a word from the list
    word = random.choice(words)
    
    # Set of letters in the word
    word_letters = set(word)
    
    # Set to keep track of the guessed letters
    guessed_letters = set()
    
    # Number of allowed wrong guesses
    attempts = 6
    
    # Display initial game information
    print("Welcome to Hangman!")
    print("_ " * len(word))
    
    while attempts > 0:
        # Display the current state of the word
        current_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", " ".join(current_word))
        
        # Ask the player for a guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is in the word
        if guess in word_letters:
            word_letters.remove(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        
        # Check if the player has guessed the entire word
        if not word_letters:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was: {word}")

# Run the game
hangman()
