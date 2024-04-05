def filter_lines(lines, keyword):
    filtered_lines = [line for line in lines if f' {keyword} ' in line or line.startswith(f'{keyword} ') or line.endswith(f' {keyword}') or line == keyword]
    return filtered_lines