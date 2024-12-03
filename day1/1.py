file_path = "input.txt"

list1 = []
list2 = []

with open(file_path, "r") as file:
    for line in file:
        columns = line.split()
        if len(columns) > 1:
            list1.append(columns[0])
            list2.append(columns[1])

list1.sort()
list2.sort()

total = 0

for i in range(0, len(list1)):
    total += abs(int(list1[i]) - int(list2[i]))

print(total)