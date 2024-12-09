#if both page number X and Y in X|Y are to be produced as part of an update, then X must be printed at some point before Y

# Read the text from the file
with open('input.txt', 'r') as file:
    input_text = file.read()

# Split the input into sections
sections = input_text.strip().split("\n\n")

# Process the first section into a dictionary
first_section = sections[0].splitlines()
dictionary = []
for line in first_section:
    key, value = map(int, line.split('|'))
    dictionary.append((key, value))


# Process the second section into a 2D grid
second_section = sections[1].splitlines()
grid = [list(map(int, row.split(','))) for row in second_section]
count = 0
for row in grid:
    valid = True
    for i in range (0, len(row)):
        #get all to check
        array_before = []
        to_check = row[i]
        #check numbers behind

        for pair in dictionary:
            if pair[0] == to_check:
                array_before.append(pair[1])

        for j in range(0, i):
            if row[j] in array_before:
                valid = False
    
    if valid:
        row_length = len(row)
        middle = row_length // 2
        count += row[middle]

print(count)


    

