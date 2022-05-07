# Problem Set 4C
# Name: <your name here> b******* w***
# Collaborators:
# Time Spent: 1hr 2/10/22

import string
from ps4a import get_permutations
import random

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    \>>> is_word(word_list, 'bat') returns
    True
    \>>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'
words_all = load_words(WORDLIST_FILENAME)

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = str(text)
        self.valid_words = words_all
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy() #delete this line and replace with your code here
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''


        cipherdict = {}
        permuted_vowels_lower = list(vowels_permutation.lower())
        permuted_vowels_upper = list(vowels_permutation.upper())

        for letter in CONSONANTS_LOWER:
            cipherdict[letter] = letter
        for letter in CONSONANTS_UPPER:
            cipherdict[letter] = letter
        #print(cipherdict)

        for idx, vowel in enumerate(VOWELS_LOWER):
            cipherdict[vowel] = permuted_vowels_lower[idx]
        for idx, vowel in enumerate(VOWELS_UPPER):
            cipherdict[vowel] = permuted_vowels_upper[idx]
        #print(cipherdict)

        return cipherdict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        messagetextlist = list(self.message_text)

        for idx, character in enumerate(messagetextlist):
            if character in transpose_dict:
                messagetextlist[idx] = transpose_dict[character]

        return "".join(messagetextlist)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''

        vowel_permutations = get_permutations(VOWELS_LOWER)
        message_text_list = list(self.message_text.lower())
        lowertext = self.message_text.lower()
        vowel_permutation_goodness = {}


        def replace_vowels(text, permutation):
            """

            Args:
                text: str to be decrypted
                permutation: permutation of vowels to try to decrypt with

            Returns: the text decrypted with the permutation as key

            """
            decryptiondict = {}
            messagetextlist = list(text)

            for idx, vowel in enumerate(permutation):
                decryptiondict[vowel] = VOWELS_LOWER[idx]
            #print(decryptiondict)

            for idx, character in enumerate(messagetextlist):
                if character in decryptiondict:
                    messagetextlist[idx] = decryptiondict[character]

            return "".join(messagetextlist)

        for permutation in vowel_permutations:
            vowel_permutation_goodness[permutation] = 0
            deciphered_text = replace_vowels(lowertext, permutation)
            split_text = deciphered_text.split()
            for word in split_text:
                if is_word(self.valid_words, word):
                    vowel_permutation_goodness[permutation] += 1

        best_permutation = max(vowel_permutation_goodness, key=lambda k: vowel_permutation_goodness[k])

        return replace_vowels(self.message_text, best_permutation)



    

if __name__ == '__main__':

    testmessage = SubMessage("Hello World")
    dicts = testmessage.build_transpose_dict("eioua")
    print(testmessage.apply_transpose(dicts))


    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()

     
    #TODO: WRITE YOUR TEST CASES HERE
    message2 = SubMessage("!!! You am a blue dog")
    permutation2 = "ioeau"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "!!! Yau im i bluo dag")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
