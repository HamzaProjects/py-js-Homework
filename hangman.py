import random
words = ["dog","cat","car", "apple"]

letters = []
word = words[random.randrange(len(words))]

print("Welcome to hangman")
life = 5
while life > 0:
    guess = input("Enter a Letter!")
    if word.__contains__(guess):
        print("Correct you guessed a letter!")
        letters.append(guess)
        if letters.__len__() == word.__len__():
            print("Congrats you win")
            break
        else:
            letter = word.__len__() - letters.__len__()
            print("You have", letter, "letters left")
    else:
        life -= 1
        if life == 0:
            print("Game Over! The word was (", word, ")")
        else:
            print("You guessed the wrong letter. You have", life, "lives left")