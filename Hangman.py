import random
import requests
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
word_list = response.content.splitlines()

stages = ["O", "I", "II", "III", "IIII", "IIIII", "IIIIII"]
word = random.choice(word_list)
display = ["_"] * len(word)
end = False
lives = 6

while end == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"Letter {guess} has already been guessed.")
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
    print(display)
    if guess not in word:
        lives -= 1
        if lives == 0:
            end = True
            print("You lose")
    if "_" not in display:
        print("You win")
    print(stages[lives])
