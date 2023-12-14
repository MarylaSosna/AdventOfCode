import re

limit_red = 12
limit_green = 13
limit_blue = 14
ids_sum = 0

with open("input.txt") as file:
    for line in file.readlines():
        g_helper = 0

        game = re.findall(r"(\d+):(.+)", line)
        game_id, values = game[0]
        values = values.replace(" ", "").replace(";", ",")
        game_results = re.findall(r"(\d+)(\w+)", values)
        games_in_line = len(game_results)

        for g in game_results:
            if int(g[0]) >= 15:
                break
            elif int(g[0]) > limit_red and g[1] == "red":
                break
            elif int(g[0]) > limit_blue and g[1] == "blue":
                break
            elif int(g[0]) > limit_green and g[1] == "green":
                break
            else:
                g_helper += 1

        if g_helper == games_in_line:
            ids_sum += int(game_id)

print(ids_sum)
