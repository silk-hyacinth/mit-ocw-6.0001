# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : B**** w**
# Collaborators : nobody lol
# Time spent    : 1/29 20min; 2/1 50min 2/2 150min 2/3 180min

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    wordlist = list(word.lower())
    scorelist = []
    for letter in wordlist:
        if letter != "*":
            scorelist.append(SCRABBLE_LETTER_VALUES[letter])

    component_1 = sum(scorelist)

    kjjk_temp_lol_icantthinkofvariablename = (7 * len(word)) - (3 * (n - len(word)))

    if kjjk_temp_lol_icantthinkofvariablename > 1:
        component_2 = kjjk_temp_lol_icantthinkofvariablename
    else:
        component_2 = 1

    return component_1 * component_2


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3) - 1)

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    assert isinstance(word, str), "word isnt a string"
    assert isinstance(hand, dict), "hand isnt a dict"

    lowerword = word.lower()
    Hand = hand.copy()  # fuck you and your "u cant modify hand" bull shit.

    for letter in lowerword:
        if letter in Hand:
            Hand[letter] -= 1

    newHand = {}

    for k in Hand:
        if Hand[k] != 0:
            newHand[k] = Hand[k]

    return newHand


#
# Problem #3: Test word validity
#
words = load_words()


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    lowerword = word.lower()

    # if lowerword not in word_list:
    #     return False

    # pseudo code

    # for every wildcard in word, we check if any one of the words when replaced w/ vowel is valid

    wildlist = []

    if "*" in lowerword:
        for letter in lowerword:
            if letter == "*":
                for vowel in VOWELS:
                    wildlist.append(lowerword.replace("*", vowel))

        validwild = False
        for possibility in wildlist:
            if possibility in words:
                validwild = True
        if not validwild:
            return False
    else:
        if lowerword not in word_list:
            return False

    handcopy = hand.copy()

    for letter in lowerword:  # checking to see if we've run out of letters
        try:
            if handcopy[letter] > 0:
                handcopy[letter] -= 1
                # print("updated hand copy is", handcopy)
            else:
                return False
        except KeyError:
            return False

    return True


#
# ------manual test for is_valid_word-------#
# print("start of manual test")
# word = "Evil"
# word2 = "bruh"
# hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
# word_list = load_words()
# print(is_valid_word(word, hand, word_list))
# print(is_valid_word(word2, hand, word_list))
# print(is_valid_word("evnil", hand, word_list))
# ------manual test for is_valid_word-------#
#


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    return len(hand)


# print(calculate_handlen({"a":5, "B":2}))

def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print("Current hand: ", end=' ')
        display_hand(hand)

        # Ask user for input
        user_word = input("If ur done enter \"!!\". Enter ur word: ")

        # If the input is two exclamation points:
        if user_word == "!!":
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                inputscore = get_word_score(user_word, calculate_handlen(hand))
                total_score += inputscore
                print("ur word is worth an ePIC", inputscore, "points.", end=' ')
                print("hand total: ", total_score)
                print()

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("your word is not valid!! haha!! and u still lose the letters u put in !!!! haha")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total
    if calculate_handlen(hand) == 0:
        print("ran out of letters.", end=' ')
    print("Total score for this hand is", total_score, "points")
    lines = "-------"
    print(lines)
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter not in hand:
        print("'thats' not in ur hand and u just wasted your substitution.")
        return hand
    letters = VOWELS + CONSONANTS
    # print("SUBSTITUTE HAND LETTER TEST", letters)
    possible_letters = list(letters)

    nowildhand = hand
    try:
        nowildhand.pop("*")
    except KeyError:
        print("no * in hand")

    for oletter in nowildhand:
        print(possible_letters)
        possible_letters.remove(oletter)

    # possible_letters = letters.replace(letter, "")

    new_letter = random.choice(possible_letters)
    # print(new_letter)
    hand[new_letter] = hand[letter]
    # print("new hand is", hand)
    # print("letter is", letter)
    del hand[letter]
    hand["*"] = 1
    return hand


# print(substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l'))

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    print()

    series_score = 0
    substituted = False
    replayed = False

    try:
        num_hands = int(input("input total number of hands you wanna play: "))
    except TypeError:
        print("Idiot. Input a number.")

    # initial game bc different formatting or something
    # does the game while the number of hands played is above 0
    # did the pseudocode for this on paper, would have been completely impossible without it
    for i in range(num_hands):
        #player_hand = deal_hand(HAND_SIZE)
        #print("first print, Current hand:", end=' ')
        #display_hand(player_hand)

        if not substituted:
            # only needs initial display when asking to sub since it prints before and after asking
            player_hand = deal_hand(HAND_SIZE)
            print("first print, Current hand:", end=' ')
            display_hand(player_hand)

            subchoice = input("would you like to sub a letter? ")
            if subchoice.lower() == "yes":
                choiceletter = input("which letter would you like to substitute? ")
                print()
                player_hand = substitute_hand(player_hand, choiceletter)
                added = play_hand(player_hand, word_list)  # i wonder if this works
                series_score += added
                substituted = True
                # replay option for subs
                if not replayed:
                    # replays if you choose to
                    repchoice = input("Would you like to replay the hand? ")
                    if repchoice.lower() == "yes":  # replay
                        series_score -= added
                        series_score += play_hand(player_hand, word_list)
                        replayed = True
            else:
                print()
                added = play_hand(player_hand, word_list)
                series_score += added
                if not replayed:
                    # replays if you choose to
                    repchoice = input("Would you like to replay the hand? ")
                    if repchoice.lower() == "yes":  # replay
                        series_score -= added
                        series_score += play_hand(player_hand, word_list)
                        replayed = True
        else:
            print()
            added = play_hand(player_hand, word_list)
            series_score += added
            if not replayed:
                # replays if you choose to
                repchoice = input("Would you like to replay the hand? ")
                if repchoice.lower() == "yes":  # replay
                    series_score -= added
                    series_score += play_hand(player_hand, word_list)
                    replayed = True
    print("Total score for all hands:", series_score)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    # play_hand(deal_hand(7), word_list)

# OLD CODE WITH BAD LOGIC

# for i in range(num_hands):
#    # check if replayed
#    if not replayed:
#        # replays if you choose to
#        repchoice = input("Would you like to replay the hand? ")
#        if repchoice.lower() == "yes" and not replayed:  # replay
#            series_score += play_hand(player_hand, word_list)
#            replayed = True
#        else:  # no replay
#            player_hand = deal_hand(HAND_SIZE)
#            display_hand(player_hand)
#            # check if subbed
#            if not substituted:
#                subchoice = input("would you like to sub a letter? ")
#                # subs if you want to
#                if subchoice.lower() == "yes":
#                    choiceletter = input("which letter would you like to substitute? ")
#                    player_hand = substitute_hand(player_hand, choiceletter)
#                    series_score += play_hand(player_hand, word_list)  # i wonder if this works
#                    substituted = True
#                    # num_hands -= 1
#                else:
#                    series_score += play_hand(player_hand, word_list)
#                    # num_hands -= 1
#    else:
#        player_hand = deal_hand(HAND_SIZE)
#        display_hand(player_hand)
#        # check if subbed
#        if not substituted:
#            subchoice = input("would you like to sub a letter? ")
#            # subs if you want to
#            if subchoice.lower() == "yes":
#                choiceletter = input("which letter would you like to substitute? ")
#                player_hand = substitute_hand(player_hand, choiceletter)
#                series_score += play_hand(player_hand, word_list)  # i wonder if this works
#                substituted = True
#                # num_hands -= 1
#            else:
#                series_score += play_hand(player_hand, word_list)
#                # num_hands -= 1
