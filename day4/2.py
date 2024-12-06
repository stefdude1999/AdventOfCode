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

my_set = {"MAS", "SAM"}

total = 0

rows, cols = len(grid), len(grid[0])
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1] in my_set and grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] in my_set:
            total += 1

print(total)

            

