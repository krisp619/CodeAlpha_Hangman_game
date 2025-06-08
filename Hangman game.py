import random

# List of words to choose from
word_list = ['python', 'developer', 'hangman', 'challenge', 'programming','simple']

# Choose a random word
word = random.choice(word_list)
word_letters = set(word)      # Letters in the word
guessed_letters = set()       # Letters guessed by the user
attempts = 6                  # Number of allowed wrong guesses

print("Welcome to Hangman!")  # No emoji


while attempts > 0 and word_letters:
    # Display the current state of the word
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("\nWord:", ' '.join(display_word))
    print("Guessed Letters:", ' '.join(sorted(guessed_letters)))
    print("Attempts Left:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

# Game over messages
if not word_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
