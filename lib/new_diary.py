# File: lib/diary.py
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.bookmark = 0

    def format(self):
        return f'My {self.title}: {self.contents}'
    
    def count_words(self):
        my_loop = self.contents.split()
        non_word = 0
        for i in my_loop:
            if i[0].isalpha() != True:
                non_word += 1
        return len(my_loop) - non_word        

    
    def reading_time(self, wpm):
        return self.count_words() / wpm
    
    def reading_chunk(self, wpm, minutes):
        count = wpm * minutes + self.bookmark
        res = " ".join(self.contents.split()[self.bookmark:count])
        self.bookmark += count
        return res


class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        if hasattr(entry, "contents"):
            self.entries.append(entry)
        else:
            raise Exception("Not a diary entry")   
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        

    def all(self):
        return self.entries

    def count_words(self):
        res = 0
        for i in self.entries:
            res += i.count_words()
        return res
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        

    def reading_time(self, wpm):
        return self.count_words() / wpm

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary. 

    def find_best_entry_for_reading_time(self, wpm, minutes):
        best_entry = None
        time = 0
        possible_words = minutes * wpm
        for i in self.entries:
            if i.count_words() > time and i.count_words() <= possible_words:
                print(i)
                best_entry = i
                print(i)
                time = i.count_words()
        if best_entry == None:
            return 'sorry no time'
        else:

            return best_entry        


        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
    


# File: lib/diary_entry.py

