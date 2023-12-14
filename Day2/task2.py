import math
import re
from collections import defaultdict

game_sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        colours_dict = defaultdict(int)

        line = line.replace(" ", "")
        line = line.split(":")
        game_result = re.findall(r"(\d+)(\w+)", line[1])

        for value, colour in game_result:
            value = int(value)
            if colour in colours_dict.keys():
                if colours_dict[colour] < value:
                    colours_dict[colour] = value
            else:
                colours_dict[colour] = value

        line_prod = math.prod(colours_dict.values())
        game_sum += line_prod

print(game_sum)
