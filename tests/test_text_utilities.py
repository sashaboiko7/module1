import pytest
from text_utils.text_utilites import read_file, write_to_file

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
        f.write("Test line 1\n")
        f.write("Test line 2\n")
        f.write("Test line 3\n")
    return file_path