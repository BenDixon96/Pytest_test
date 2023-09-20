from lib.some_functions import * 
def test_hello():
    assert say_hello("ben") == "hello ben"


def test_cipher():
    assert encode("theswiftfoxjumpedoverthelazydog", "secretkey") == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"


def test_get_common_letter():
    assert get_most_common_letter("the roof, the roof, the roof is on fire!") == "o"
    
def test_diary_parm():
    diary = DiaryEntry("notebook", "it was the best of times")
    assert diary.title == "notebook"
    assert diary.contents == "it was the best of times"

def test_diary_format():
    diary = DiaryEntry("notebook", "it was the best of times")
    assert diary.format() == "My notebook: it was the best of times"
def test_count_words():
    diary = DiaryEntry("notebook", "it was the best of times")
    assert diary.count_words() == 6
def test_reading_time():
    diary = DiaryEntry("notebook", "it was the best of times")
    assert diary.reading_time(3) == 2    
def test_reading_chunk():
    diary = DiaryEntry("notebook", "it was the best of times")
    assert diary.reading_chunk(3, 1) == "it was the"
    assert diary.bookmark == 3
    assert diary.reading_chunk(3, 1) == "best of times"
def test_Grammar_stats():
    grammar = GrammarStats()
    assert grammar.check("This if good.") == True
    assert grammar.check("this not so much") == False
    assert grammar.percentage_good() == 50
    grammar.check("this not so much")
    grammar.check("this not so much")
    grammar.check("this not so much")
    grammar.check("this not so much")
    assert grammar.percentage_good() == 16.67

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."







