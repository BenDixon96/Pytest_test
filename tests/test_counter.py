from lib.counter import *



def test_report():
    test = counter()

    assert test.report() == "Counted to 0 so far."
def test_add():
    test = counter()
    test.add(5)
    test.add(5)
        
    assert test.report() == "Counted to 10 so far."    
