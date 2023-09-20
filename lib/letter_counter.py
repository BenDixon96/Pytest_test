# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        
        self.text = text
        self.counter = {}

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        
        for char in self.text:
            if  char.isalpha() == True and char not in counter.keys():
                
                counter[char] = 1
            elif char.isalpha() == True:
                counter[char] = counter[char] + 1
        most_common = None
        most_common_count = 0
        for x, i in counter.items():
            if i > most_common_count:
                most_common = x
                most_common_count = i        
            
        print(counter)        
        print([most_common_count, most_common])
        return [most_common, most_common_count]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())


# Intended output:
# [2, "i"]