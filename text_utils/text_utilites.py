def read_file(input_file):
    """
    function attempts to open and read the contents of a specified file.
    If the file is found and read successfully, it returns a list of lines from
    the file. If the file is not found, it prints an error message and returns None.
    """
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
        return None


def write_to_file(output_file, filtered_lines):
    """
    function attempts to write the contents of a list of lines to a specified file.
    If the write operation is successful, it prints a success message. If an error
    occurs while writing to the file, it prints an error message
    """

    try:
        with open(output_file, 'w') as f:
            f.writelines(filtered_lines)
        print(f"Результат фільтрації був записаний у файл '{output_file}'.")
    except IOError:
        print(f"Помилка при записі у файл '{output_file}'.")