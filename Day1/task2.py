import re

num_sum = 0
values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
          "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("input.txt") as f:
    for line in f.readlines():
        first_value = re.findall(r"(one|two|three|four|five|six|seven|eight|nine|\d){1}[a-z|\d]*",
                                 line)
        second_value = re.findall(r"[a-z|\d]*(one|two|three|four|five|six|seven|eight|nine|\d){1}",
                                  line)

        try:
            int(first_value[0])
        except ValueError:
            first_str = values[first_value[0]]
        else:
            first_str = first_value[0]

        try:
            int(second_value[0])
        except ValueError:
            second_str = values[second_value[0]]
        else:
            second_str = second_value[0]

        num_sum += int(first_str + second_str)

print(num_sum)
