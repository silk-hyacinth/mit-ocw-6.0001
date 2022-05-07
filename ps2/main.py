# Problem Set 2, hangman.py
# Name: b*********************************************** *************** edited for github again
# Collaborators: noo one
# Time spent: 2hr 12/27 2.5hr 12/30

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_list = list(secret_word)
    for i in word_list:
        if i not in letters_guessed:
            return False
    return True

#secret_word = 'apple'
#letters_guessed = ['a', 'p', 'l', 'e', 'e']
#print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_list = list(secret_word)
    for i in secret_list:
        if i not in letters_guessed:
            num = secret_list.index(i)
            secret_list[num] = "_ "
    guessed_word = "".join(secret_list)

    return guessed_word

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase

    letterlist = list(letters)

    temp = ""

    for i in letterlist:
        if i not in letters_guessed:
            temp += i

    return temp

#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (get_available_letters(letters_guessed))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    #initialization


    lines = "=-=-=-=-=-=-="
    num_guesses = 8 #guesses remaining
    num_warnings = 3
    guessedLetters = []
    secret_list = list(secret_word)
    vowels = ["a", "e", "i", "o", "u"]

    print("Whale cum to hanging man!!!")
    print("I'm thinking of a word that's", len(secret_word), "letters long")
    print(lines)

    #each round
    while num_guesses > 0:
        print("You have", num_guesses, "guesses left.")
        print("Available letters: ", get_available_letters(guessedLetters))

        #storing letters guessed
        raw = input("Please guess a letter: ")
        guessedLetter = str.lower(raw)

        if guessedLetter in guessedLetters: #repeat letter check
            print("bruh u already guessed that")
            print(get_guessed_word(secret_word, guessedLetters))    
            print(lines)
            #raw = input("Please guess a letter: ")
            #guessedLetter = str.lower(raw)
            continue
        else:
            guessedLetters += guessedLetter #update list of guessed letters

        #guessing
        if not guessedLetter.isalnum(): #check if input is a letter
            num_warnings -= 1
            print("type a letter idiot")
            if num_warnings < 1: #warning update
                num_warnings = 3
                num_guesses -= 1
                print("cgrts u just lost a guess")
        elif guessedLetter not in secret_list and guessedLetter not in vowels: #consonant, not in word
            print("bad guess...")
            print(get_guessed_word(secret_word, guessedLetters))
            num_guesses -= 1
        elif guessedLetter not in secret_list and guessedLetter in vowels: #vowel, not in word
            print("horrible guess...")
            print(get_guessed_word(secret_word, guessedLetters))
            num_guesses -= 2
        else: #guessed letter is in word
            print("Good guess")
            print(get_guessed_word(secret_word, guessedLetters))
            if is_word_guessed(secret_word, guessedLetters): #check if user has won
                total_score = num_guesses * len(secret_word)
                print("you won!")
                print("ur score this game is ", total_score)
                break
        print(lines)

    if num_guesses < 1: #lose
        print("u lost lol gg")
        print("the word was", secret_word)








# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    my_list = []
    stripped_list = list(my_word.replace(" ", ""))
    #print(stripped_list)
    other_list = list(other_word)
    if len(stripped_list) != len(other_word):
        return False

    mytemp = ''
    othertemp = ''
    for i in other_list:
        if i in stripped_list:
            othertemp += i
    for i in stripped_list:
        if i != "_":
            mytemp += i

    if not mytemp == othertemp:
        return False

    for idx in range(len(stripped_list)):
        if other_list[idx] != stripped_list[idx] and stripped_list[idx] != "_":
            return False
    return True





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    temp = []

    for i in wordlist:
        if match_with_gaps(my_word, i):
            temp.append(i)

    if len(temp) > 0:
        print(" ".join(temp)    )
    else:
        print("No matches found")


#show_possible_matches("a_ pl_ ")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # initialization
    lines = "=-=-=-=-=-=-="
    num_guesses = 8  # guesses remaining
    num_warnings = 3
    guessedLetters = []
    secret_list = list(secret_word)
    vowels = ["a", "e", "i", "o", "u"]

    print("Whale cum to hanging man!!!")
    print("Type * for hints")
    print("I'm thinking of a word that's", len(secret_word), "letters long")
    print(lines)

    # each round
    while num_guesses > 0:
        if is_word_guessed(secret_word, guessedLetters):  # check if user has won
            total_score = num_guesses * len(secret_word)
            print("you won!")
            print("ur score this game is ", total_score)
            break
        print("You have", num_guesses, "guesses left.")
        print("Available letters: ", get_available_letters(guessedLetters))

        # storing letters guessed
        raw = input("Please guess a letter: ")
        guessedLetter = str.lower(raw)

        if guessedLetter in guessedLetters and guessedLetter != "*":  # repeat letter check
            print("bruh u already guessed that")
            print(get_guessed_word(secret_word, guessedLetters))
            print(lines)
            # raw = input("Please guess a letter: ")
            # guessedLetter = str.lower(raw)
            continue
        else:
            if guessedLetter != "*":
                guessedLetters += guessedLetter  # update list of guessed letters

        # guessing
        if guessedLetter == "*":
            print("Possible word matches are: ")
            show_possible_matches(get_guessed_word(secret_word, guessedLetters))

        elif not guessedLetter.isalnum():  # check if input is a letter
            num_warnings -= 1
            print("type a letter idiot")
            if num_warnings < 1:  # warning update
                num_warnings = 3
                num_guesses -= 1
                print("cgrts u just lost a guess")
        elif guessedLetter not in secret_list and guessedLetter not in vowels:  # consonant, not in word
            print("bad guess...")
            print(get_guessed_word(secret_word, guessedLetters))
            num_guesses -= 1
        elif guessedLetter not in secret_list and guessedLetter in vowels:  # vowel, not in word
            print("horrible guess...")
            print(get_guessed_word(secret_word, guessedLetters))
            num_guesses -= 2
        else:  # guessed letter is in word
            print("Good guess")
            print(get_guessed_word(secret_word, guessedLetters))
            print(guessedLetters)
            if is_word_guessed(secret_word, guessedLetters):  # check if user has won
                total_score = num_guesses * len(secret_word)
                print("you won!")
                print("ur score this game is ", total_score)
                break
        print(lines)

    if num_guesses < 1:  # lose
        print("u lost lol gg")
        print("the word was", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #commented out for manual testing later
    #print(secret_word)
    #secret_word = input("Input secret word:")
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.


