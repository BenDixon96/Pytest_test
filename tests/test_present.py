from lib.present import *
import pytest

def test_if_not_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)

    assert error_message == "No contents have been wrapped."

    def test_present_wrapped():
        present = Present()
        present.wrap("toy")
        with pytest.raises(Exception) as i:
            present.wrap("doll")
        error_message = str(i.value)
        assert error_message == "A contents has already been wrapped."    
