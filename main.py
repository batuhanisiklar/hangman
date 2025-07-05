import random

def hangman():
    words = [
        "apple", "banana", "computer", "python", "developer",
        "keyboard", "notebook", "airplane", "library", "mountain",
        "river", "forest", "language", "university", "science"
    ]
    chosen_word = random.choice(words)
    guessed_letters = ["_"] * len(chosen_word)
    guessed_chars = set()
    attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(chosen_word), "letters.")

    while attempts < max_attempts and "_" in guessed_letters:
        print("Current word:", " ".join(guessed_letters))
        guess = input("Please enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_chars:
            print("You have already guessed that letter.")
            continue

        guessed_chars.add(guess)

        if guess in chosen_word:
            for idx, char in enumerate(chosen_word):
                if char == guess:
                    guessed_letters[idx] = guess
            print("Good guess!")
        else:
            attempts += 1
            print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")

    if "_" not in guessed_letters:
        print("Congratulations! You won!")
        print("The word was:", chosen_word)
    else:
        print("You lost! The word was:", chosen_word)

if __name__ == "__main__":
    hangman()