
def say_hello(name):
    return f"hello {name}"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"

def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(-1, 26)]
    cipher_with_duplicates = list(key) + alphabet
    
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    
    return cipher


def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))

        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        
        plaintext_chars.append(plain_char)
    

    return "".join(plaintext_chars)

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.


def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha() == True:
            counter[char] = counter.get(char, 0) + 1 
    value = 0
    letter = ''
    for x, i in counter.items():
        if i > value:
            value = i
            letter = x        
    return letter


class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        self.title = title
        self.contents = contents
        self.bookmark = 0

        

    def format(self):
        return f'My {self.title}: {self.contents}'

        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        return len(self.contents.split())
        # Returns:
        #   int: the number of words in the diary entry
    

    def reading_time(self, wpm):
        return self.count_words() / wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        count = wpm * minutes + self.bookmark
        res = " ".join(self.contents.split()[self.bookmark:count])
        self.bookmark += count
        print(self.bookmark)
        return res


        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
class GrammarStats:
    def __init__(self):
        self.good_g = 0
        self.total_g = 0
  
    def check(self, text):
        if text[0].isupper() == True and text[-1] =='.':
            self.total_g += 1
            self.good_g += 1
            return True
        else:
            self.total_g += 1
            return False    
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
  
    def percentage_good(self):
        return round(self.good_g / self.total_g * 100, 2)
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.


    # File: lib/factorial.py

def factorial(n):
    product = 1
    while n > 0:
        n -= 1
        product *= n
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24      

# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = "aioueAIOUE"
        

    def remove_vowels(self):
        res = ''
        for i in self.text:
            if i not in self.vowels:
                res += i

        return res        


       
                
            
         

# File: tests/test_vowel_remover.py


# File: lib/diary.py

