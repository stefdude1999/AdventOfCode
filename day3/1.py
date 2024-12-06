import re

file_path = 'input.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, file_content)

results = sum([int(x) * int(y) for x, y in matches])

print(results)