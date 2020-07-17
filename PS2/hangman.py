# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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

abc = "abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"




def is_word_guessed(letters_guessed, secret_word):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word,letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    '''
    letters_guessed_with_spaces = ""
    for char in secret_word:
        if char not in letters_guessed:
            letters_guessed_with_spaces += "_ "
        else:
            letters_guessed_with_spaces += char
    return letters_guessed_with_spaces



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
    '''
    available_letters = ""
    for char in abc:
        if char in letters_guessed:
            available_letters += "_ "
        else:
            available_letters += char + " "
    return available_letters
    
    

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
    warnings_left = 3
    letters_guessed = []
    number_of_guesses_left = 7

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("-------------")


    for i in range(7):
        number_of_guesses_left -= 1
        print("You have " + str(number_of_guesses_left) + " guesses left")
        print("Available letters:" + get_available_letters(letters_guessed))


        letter_guessed = input("Enter your guess: ")       # letter guessed
        lowercase_letter_guessed = letter_guessed.lower()  # makeing sure letter guessed is lowercase

        while True:
            if lowercase_letter_guessed in letters_guessed:
                warnings_left -= 1
                print("You have already entered {} you have {} warning's left".format(lowercase_letter_guessed,
                                                                                      warnings_left))
                letter_guessed = input("Enter a different letter ")
                lowercase_letter_guessed = letter_guessed.lower()
                if warnings_left <= 0:
                    print("You have run out of warnings"
                          " Game OVER!")
                    return

            elif lowercase_letter_guessed.isalpha() == "False":
                warnings_left -= 1  # Is not a letter and minuses warnings
                print("You did not enter a character, you have {} warnings left".format(warnings_left))
                letter_guessed = input("Enter a character: ")
                lowercase_letter_guessed = letter_guessed.lower()

                if warnings_left <= 0:
                    print("You have run out of warnings"
                          " Game OVER!")
                    return
            elif lowercase_letter_guessed not in letters_guessed and str(lowercase_letter_guessed.isalpha()) != "False":
                break


        letters_guessed.append(lowercase_letter_guessed)  # letter added to list


        #This code will return good guess if letter is in the secret word and bad guess if the letter is not in
        #the secret word. it also applys an additional penalty for choosing a vowel if not correct guess.
        if lowercase_letter_guessed in secret_word:
            print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
        elif lowercase_letter_guessed not in secret_word:
            print("Bad luck {}".format(get_guessed_word(secret_word, letters_guessed)))
            if lowercase_letter_guessed in vowel:
                number_of_guesses_left -= 1
        print("-------------")


        if is_word_guessed(letters_guessed, secret_word) == True:
            print("Congratulations you won!"
                  " your total score for this game is {}".format(number_of_guesses_left*len(letters_guessed)))
            return
        elif number_of_guesses_left <= 0:
            print("sorry you ran out of guesses"
                  "You lose!")
            return



hangman("apple")





if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
