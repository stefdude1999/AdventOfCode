def is_strictly_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_strictly_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def check_differences(lst):
    if len(lst) < 2:
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
    # Flag to avoid double counting
    counted = False

    # Check the original list
    if check_differences(line) and (is_strictly_decreasing(line) or is_strictly_increasing(line)):
        total += 1
        print(f"Counted original list: {line}")
        counted = True  # Mark as counted

    # Check sublists by removing one element
    if not counted:  # Only check sublists if the original wasn't counted
        for j in range(len(line)):
            sublist = line[:j] + line[j+1:]
            if check_differences(sublist) and (is_strictly_decreasing(sublist) or is_strictly_increasing(sublist)):
                total += 1
                print(f"Counted sublist: {sublist} (removed {line[j]} at index {j})")
                break  # Stop after finding one valid sublist

print(f"Total safe reports: {total}")