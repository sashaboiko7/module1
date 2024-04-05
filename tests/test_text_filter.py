from services.text_filter import filter_lines

def test_filter_lines():
    lines = ["apple banana orange", "apple", "banana", "orange"]
    keyword = "apple"
    filtered_lines = filter_lines(lines, keyword)
    assert filtered_lines == ["apple banana orange", "apple"]
