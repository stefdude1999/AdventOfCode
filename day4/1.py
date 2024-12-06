def parse_paragraph_to_grid(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                grid.append(list(line.rstrip('\n')))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return grid

file_path = 'input.txt'

grid = parse_paragraph_to_grid(file_path)

count = 0
to_match = "XMAS"
match_backwards = "SAMX"

rows, cols = len(grid), len(grid[0])  # Grid dimensions

for i in range(rows):  # Loop through all rows
    for j in range(cols):  # Loop through all columns
        # Check forward (horizontal right)
        if j + 3 < cols:  # Ensure enough columns ahead
            if "".join(grid[i][j:j+4]) == to_match:
                count += 1

        # Check backward (horizontal left)
        if j - 3 >= 0:  # Ensure enough columns behind
            if "".join(grid[i][j-3:j+1][::-1]) == match_backwards:
                count += 1

        # Check down (vertical down)
        if i + 3 < rows:  # Ensure enough rows below
            if "".join(grid[i+k][j] for k in range(4)) == to_match:
                count += 1

        # Check up (vertical up)
        if i - 3 >= 0:  # Ensure enough rows above
            if "".join(grid[i-k][j] for k in range(4)) == match_backwards:
                count += 1

        # Check diagonal RD (down-right)
        if i + 3 < rows and j + 3 < cols:  # Ensure bounds for down-right diagonal
            if "".join(grid[i+k][j+k] for k in range(4)) == to_match:
                count += 1

        # Check diagonal LU (up-left)
        if i - 3 >= 0 and j - 3 >= 0:  # Ensure bounds for up-left diagonal
            if "".join(grid[i-k][j-k] for k in range(4)) == match_backwards:
                count += 1

        # Check diagonal RU (up-right)
        if i - 3 >= 0 and j + 3 < cols:  # Ensure bounds for up-right diagonal
            if "".join(grid[i-k][j+k] for k in range(4)) == to_match:
                count += 1

        # Check diagonal LD (down-left)
        if i + 3 < rows and j - 3 >= 0:  # Ensure bounds for down-left diagonal
            if "".join(grid[i+k][j-k] for k in range(4)) == match_backwards:
                count += 1

print(count)
