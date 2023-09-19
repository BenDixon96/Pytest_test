from lib.string_builder import *



class Test_StringBuilder():
    def test_output(self):
        test = StringBuilder()
        
        assert test.output() == ''
    def test_add(self):
        test = StringBuilder()
        test.add("b")
        assert test.output() == 'b'
    def test_size(self):
        test = StringBuilder()
        test.add("b")
        assert test.size() == 1        


