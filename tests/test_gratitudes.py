
from lib.gratitudes import * 

def test_add():
    test = Gratitudes()
    test.add("cake")
    assert test.format() == "Be grateful for: cake"