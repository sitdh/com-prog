road_levels = [int(i) for i in input().strip().split(', ')]

road_level = 0

number_of_hole = 0

start_hole = road_levels[0]

for i, v in enumerate(road_levels):
    if v < road_levels[0]:
        start_hole = i if start_hole == 0 else start_hole

    if v >= 0 and start_hole >= 1:
        number_of_hole += 1
        start_hole = 0

print(number_of_hole)
