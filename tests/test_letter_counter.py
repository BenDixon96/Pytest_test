from lib.letter_counter import *

def test_letter_count():
    letters = LetterCounter("bagee&&r")
    assert letters.calculate_most_common() == ["e", 2]

    