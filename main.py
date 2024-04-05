from services.text_filter import filter_lines
from text_utils.text_utilites import read_file, write_to_file

if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "filtered.txt"
    keyword = input("Введіть ключове слово для фільтрації: ")

    lines = read_file(input_file)
    if lines is not None:
        filtered_lines = filter_lines(lines, keyword)
        if filtered_lines:
            write_to_file(output_file, filtered_lines)
        else:
            print(f"Не було знайдено рядків, що містять ключове слово '{keyword}'.")