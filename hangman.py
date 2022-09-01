import random
from words import words
from manhang import stages

def get_word(): 
    word = random.choice(words) #randomly chooses something from that list
    while '-' in word or ' ' in word:
        word = random.choice(words) #we will get a word without a space or a dash
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print("Let's play Hangman!")
    print(manhang(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter. Try another letter.", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word! Good to go.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            print("You have guessed these letters: ", " ".join(guessed_letters))
        else:
            print("Not a valid guess.")
        print(manhang(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulation, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def manhang(tries):
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()