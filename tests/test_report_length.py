from lib.report_length import report_length

def test_report_length():
    assert report_length('word') == "This string was 4 characters long."