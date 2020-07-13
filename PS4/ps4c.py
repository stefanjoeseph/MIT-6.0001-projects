# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# # you may find these constants helpful
# VOWELS_LOWER = 'aeiou'
# VOWELS_UPPER = 'AEIOU'
# CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
# CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
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

    def transpose_flag(self, vowels_permutation):
        '''
        Used to check whether build transpose was input with the correct arguments

        Returns True if arguments are Valid
        Returns False if arguments aren't valid
        '''
        # Make sure that all vowels and only vowels are input
        transpose_flag = False
        if len(vowels_permutation) != 5:
            transpose_flag = True

        for char in vowels_permutation:
            if char not in 'aeiou':
                transpose_flag = True

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
        # Make sure method called with the correct arguments.
        while self.transpose_flag(vowels_permutation):
            vowels_permutation = input('Please re-input your vowel permutation. Remember that it must contain all the vowels and only vowels: ')

        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        ordered_vowels = ['a', 'e', 'i', 'o', 'u']
        dictionary = {}

        # Create a dictionary mapping all lowercase letters, apart from vowels, to themselves.
        for char in lowercase:
            if char not in ordered_vowels:
                dictionary[char] = char

        # Add to the dictionary all vowels mapped to their new values
        i = 0
        for char in vowels_permutation:
            dictionary[ordered_vowels[i]] = char
            i += 1

        # Build an uppercase version of the dictionary
        dictionary.items()
        upper_dictionary = {k.upper(): v.upper() for k, v in dictionary.items()}

        # Merge the two dictionaries
        dictionary.update(upper_dictionary)
        return dictionary




    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        punctuation = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        message = ''
        for char in self.get_message_text():
            if char in punctuation:
                message += char
            elif char in transpose_dict.keys():
                message += transpose_dict[char]

        return message






        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # The two instance variables are inherited from SubMessage
        SubMessage.__init__(self, text)

    def get_permutations(self, sequence):
        '''
        Enumerate all permutations of a given string

        sequence (string): an arbitrary string to permute. Assume that it is a
        non-empty string.

        You MUST use recursion for this part. Non-recursive solutions will not be
        accepted.

        Returns: a list of all permutations of sequence

        Example:
        >>> get_permutations('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

        Note: depending on your implementation, you may return the permutations in
        a different order than what is listed here.
        '''
        if len(sequence) == 1:
            return [sequence]

        else:
            first_letter = sequence[0]
            rest_of_letters = sequence[1:]
            list_of_perms = get_permutations(rest_of_letters)

            copy_of_list = list_of_perms.copy()
            list_of_perms = []

            for element in copy_of_list:
                for i in range(len(element) + 1):
                    new_element = element[:i] + first_letter + element[i:]
                    list_of_perms.append(new_element)

            return list_of_perms


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
        # Use answer to part a to get a list of all the permutations of the vowels
        list_of_vowel_perms = get_permutations(sequence='aeiou')

        # Use the inherited methods to get a list of possible versions of the message
        perm_messages = []
        for vowel_perm in list_of_vowel_perms:
            perm_messages.append(self.apply_transpose(transpose_dict=self.build_transpose_dict(vowel_perm)))


        # Create a dictionary with the keys being each variation of the message and the
        # values being the number of valid words in that message.
        valid_word_dict = {}
        for possible_message in perm_messages:
            no_valid_words = 0

            for word in possible_message.split():
                if is_word(self.get_valid_words(), word):
                    no_valid_words += 1
            valid_word_dict[possible_message] = no_valid_words


        # Return the message with the largest number of valid words.
        max_key = max(valid_word_dict, key=valid_word_dict.get)
        return max_key







if __name__ == '__main__':

    # Test for build_transpose_dict (note that this is not part of the exercise given by MIT)
    message = SubMessage('Hello World')
    test_dictionary = message.build_transpose_dict("eaiuo")
    expected_output = {'a': 'e', 'b': 'b', 'c': 'c', 'd': 'd', 'e':'a', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'u', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'o', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    print('Expected output: {}'.format(expected_output))
    print('Actual output: {}'.format(test_dictionary))
    for k, v in expected_output.items():
        flag = False
        if (k, v) not in test_dictionary.items():
            print('Build Transpose Dictionary Fail')
            flag = True
    if flag == False:
        print('Build Transpose Dictionary passed')
    print('\n-----------------------------------------------------\n')

    # test case 1
    message3 = SubMessage('Corona virus')
    permutation = 'aeiuo'
    expected_encryption = 'Curuna viros'
    enc_dict = message3.build_transpose_dict(permutation)
    print('Original message:', message3.get_message_text(), 'Permutation', permutation)
    print('Expected encryption ', expected_encryption)
    print('Actual encryption ', message3.apply_transpose(enc_dict))

    enc_message = EncryptedSubMessage(message3.apply_transpose(enc_dict))

    print("Decrypted message:", enc_message.decrypt_message())

    print('\n-----------------------------------------------------\n')

    # test case 2
    message4 = SubMessage('\'Hello World!\' he exclaimed.')
    permutation = 'eaiuo'
    expected_encryption = '\'Hallu Wurld\' ha axcleimad.'
    enc_dict = message4.build_transpose_dict(permutation)
    print('Original message:', message4.get_message_text(), 'Permutation', permutation)
    print('Expected encryption ', expected_encryption)
    print('Actual encryption ', message4.apply_transpose(enc_dict))

    enc_message = EncryptedSubMessage(message4.apply_transpose(enc_dict))

    print("Decrypted message:", enc_message.decrypt_message())

    print('\n-----------------------------------------------------\n')

    # Example test case
    message2 = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message2.build_transpose_dict(permutation)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message2.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message2.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    #
    #TODO: WRITE YOUR TEST CASES HERE
