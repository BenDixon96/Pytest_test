from lib.new_diary import *
import pytest


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

#'Exceptions
#1 if the entry is not of the correct class or not a Class'

fake_entry = "stop"
my_entry = DiaryEntry('chapter1', "I am going to write some text to test out if this works fifteen words")
my_second_entry = DiaryEntry('chapter2', 'some more text')
bad_pun = DiaryEntry('chapter3', "the fish was a big one !")
# my_entry 15 second 3 bad_pun = 6

def test_add_entries():
    my_diary = Diary()
    my_diary.add(my_entry)
    assert my_diary.entries == [my_entry]

def test_diary_all():
    my_diary = Diary()
    my_diary.add(my_entry)
    my_diary.add(my_second_entry)
    assert my_diary.all() == [my_entry, my_second_entry]

def test_one_entry():
    my_diary = Diary()
    my_diary.add(my_entry)
    assert my_diary.count_words() == 15

def test_mult_entries():
    my_diary = Diary()
    my_diary.add(my_entry)
    my_diary.add(my_second_entry)
    assert my_diary.count_words() == 18

def test_for_bad_punctation():
    my_diary = Diary()
    my_diary.add(bad_pun)
    assert my_diary.count_words() == 6

def test_reading_speed():
    my_diary = Diary()
    my_diary.add(my_entry)
    my_diary.add(my_second_entry)
    assert my_diary.reading_time(2) == 9

def test_if_division_no_good():
    my_diary = Diary()
    my_diary.add(my_entry)
    my_diary.add(my_second_entry)
    assert my_diary.reading_time(5) == 3.6

def test_the_best_entry():
    my_diary = Diary()
    my_diary.add(my_entry)
    my_diary.add(my_second_entry)
    my_diary.add(bad_pun)
    assert my_diary.find_best_entry_for_reading_time(3, 1) == my_second_entry

def test_if_no_time():
    my_diary = Diary()
    my_diary.add(my_entry)
    assert my_diary.find_best_entry_for_reading_time(5, 1) == "sorry no time"

def test_not_adding_class():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        my_diary.add(fake_entry)
    error_message = str(e.value)
    assert error_message == "Not a diary entry"

