import pytest
from services.text_filter import filter_lines

@pytest.mark.parametrize("lines, keyword, expected_output", [
    (["apple banana orange", "apple", "banana", "orange"], "apple", ["apple banana orange", "apple"]),
    (["apple", "banana", "orange"], "apple", ["apple"]),
    (["apple banana orange", "apple", "banana", "orange"], "grape", [])
])
def test_filter_lines(lines, keyword, expected_output):
    filtered_lines = filter_lines(lines, keyword)
    assert filtered_lines == expected_output