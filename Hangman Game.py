import random

words = ["python", "coding", "alpha", "intern", "project"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("Already used!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("You won! Word:", word)
else:
    print("You lost! Word was:", word)