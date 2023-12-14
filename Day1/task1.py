import re

num_sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        numbers = re.findall(r"[a-z]*(\d)?[a-z\d]*(\d)", line)
        if numbers[0][0] != "" and numbers[0][1] != "":
            num_sum += int(numbers[0][0] + numbers[0][1])
        if numbers[0][0] == "" and numbers[0][1] != "":
            num_sum += int(numbers[0][1] + numbers[0][1])

print(num_sum)
