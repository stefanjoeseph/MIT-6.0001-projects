# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])

    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(file_name='words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
        another letter (string).
        '''
        # First make sure shift is in our allowed range
        assert 0 <= shift < 26, 'The shift must be in the range: 0<=shift<26'

        lowercase = string.ascii_lowercase
        list_lower = []
        list_upper = []
        dictionary = {}

        # Creates a list of tuples. Each tuple corresponds to 1 letter of the alphabet.
        # In each tuple the elements are (original letter, shifted letter)
        for char in lowercase:
            new_index = lowercase.find(char) + shift
            if new_index > 25:
                new_index -= 26
                list_lower.append((char, lowercase[new_index]))
            else:
                list_lower.append((char, lowercase[new_index]))

        # Makes a capitalised version of the list
        for x, y in list_lower:
            list_upper.append((x.upper(), y.upper()))

        # Concatenates the list
        concatenated_list = list_lower + list_upper

        # Converts list to dictionary
        for original_letter, shifted_letter in concatenated_list:
            dictionary[original_letter] = shifted_letter

        return dictionary

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # First we use the previously defined method to build our new dictionary
        dictionary = self.build_shift_dict(shift)
        shifted_message = ''
        punctuation = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""

        # We then loop over our message to find the shifted message
        # making sure to use the predefined access method.
        for char in self.get_message_text():
            if char in punctuation:
                shifted_message += char
            else:
                shifted_message += dictionary[char]

        return shifted_message


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, new_shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert 0 <= new_shift < 26, 'The shift must be in the range: 0<=shift<26'
        self.shift = new_shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shift_dictionary = {}
        message_variations = []

        # Establish a dictionary with all versions of the shifted message and a list of the
        # shifted messages
        for shift in range(0, 26):
            shift_dictionary[self.apply_shift(shift)] = shift
            message_variations.append(self.apply_shift(shift))

        # Create a dictionary with the keys being each variation of the shifted message and the
        # values being the number of valid words in that message
        word_match_dictionary = {}
        for variation in message_variations:
            no_valid_words = 0
            for word in variation.split():
                if is_word(self.get_valid_words(), word):
                    no_valid_words += 1

            word_match_dictionary[variation] = no_valid_words

        # Find the message variation with the max number of matching words using
        # word_match_dictionary and use this to find the optimal shift.
        max_key = max(word_match_dictionary, key=word_match_dictionary.get)
        return (shift_dictionary[max_key], max_key)









if __name__ == '__main__':

    print('PLAIN TEXT TESTS')
    print('--------------------------------------')
    # Plaintextmessage test case 1
    plaintext1 = PlaintextMessage('\'Hello world\'!', 5)
    print('Expected output: \'Mjqqt btwqi\'!')
    print('Actual output:', plaintext1.get_message_text_encrypted())
    if '\'Mjqqt btwqi\'!' == plaintext1.get_message_text_encrypted():
        print('Plaintextmessage test 1 passed')
    print('--------------------------------------')

    # Plaintextmessage test case 2
    plaintext2 = PlaintextMessage('car', 1)
    print('Expected Output: dbs')
    print('Actual output:', plaintext2.get_message_text_encrypted())
    if 'dbs' == plaintext2.get_message_text_encrypted():
        print('Plaintextmessage test 2 passed')
    print('--------------------------------------')

    # Plaintextmessage test case 3
    try:
        plaintext1 = PlaintextMessage('\'Hello world\'!', 27)
    except AssertionError:
        print('Plaintextmessage test 3 passed')
    print('--------------------------------------\n')

    print('CIPHER TEXT TESTS')
    print('--------------------------------------')
    # CiphertextMessage test case 1
    ciphertext1 = CiphertextMessage('dpme?')
    print('Expected Output:', (25,'cold?'),'or',(2, 'frog?'))
    print('Actual output:', ciphertext1.decrypt_message())
    if (25, 'cold?') or (2, 'frog?') == ciphertext1.decrypt_message():
        print('Ciphertextmessage test 1 passed')
    print('--------------------------------------')

    # CiphertextMessage test case 2
    ciphertext2 = CiphertextMessage('bgtq')
    print('Expected Output:', (24, 'zero'))
    print('Actual output:', ciphertext2.decrypt_message())
    if (24, 'zero') == ciphertext2.decrypt_message():
        print('Ciphertextmessage test 1 passed')
    print('--------------------------------------')

    #    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
