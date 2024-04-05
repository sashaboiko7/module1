def read_file(input_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
        return None