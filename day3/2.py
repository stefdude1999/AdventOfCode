import re

file_path = 'input.txt'

with open(file_path, 'r') as file:
    text = file.read()

do = r"do\(\)"
dont = r"don't\(\)"
mul = r"mul\((\d+),(\d+)\)"

pattern = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"

matches = re.findall(pattern, text)
enabled = True
total = 0

for match in matches:
    if (match[0] == 'do()'):
        enabled = True
    elif (match[1] == 'don\'t()'):
        enabled = False
    elif enabled and match[3] and match[4]:
        total += int(match[3]) * int(match[4])

print(total)