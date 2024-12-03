def is_strictly_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_strictly_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def check_differences(lst):
    if len(lst) < 2:  # A list with less than 2 elements has no differences to check
        return True
    return all(1 <= abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1))


def parse_lines_to_lists(file_path):
    all_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = list(map(int, line.split()))
                all_lines.append(numbers)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ValueError as e:
        print(f"Error parsing a line: {e}")
    return all_lines

file_path = "input.txt"
parsed_data = parse_lines_to_lists(file_path)
total = 0
for line in parsed_data:
    if check_differences(line) and (is_strictly_decreasing(line) or is_strictly_increasing(line)):
        total += 1

print(total)
        