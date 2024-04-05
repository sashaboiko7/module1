def filter_lines(lines, keyword):
    filtered_lines = [line for line in lines if keyword in line]
    return filtered_lines