def read_file(input_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
        return None

def write_to_file(output_file, filtered_lines):
    try:
        with open(output_file, 'w') as f:
            f.writelines(filtered_lines)
        print(f"Результат фільтрації був записаний у файл '{output_file}'.")
    except IOError:
        print(f"Помилка при записі у файл '{output_file}'.")