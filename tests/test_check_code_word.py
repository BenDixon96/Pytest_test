from lib.check_code_word import *

def test_check_code_word():
    assert check_code_word("horse") == "Correct! Come in."
    assert check_code_word("hoooe") == "Close, but nope."
    assert check_code_word("butter") == "WRONG!"