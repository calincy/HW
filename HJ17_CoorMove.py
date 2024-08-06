'''
坐标移动
'''

location_list = input().split(";")
coordinate = [0,0]

for location in location_list:
    if not 2 <= len(location) <= 3:
        continue

    try:
        direction = location[0]
        step = int(location[1:])
        if direction in ["A","D","S","W"]:
            if 0 <= step <= 99:
                if direction == "A":
                    coordinate[0] -= step
                if direction == "D":
                    coordinate[0] += step
                if direction == "W":
                    coordinate[1] += step
                if direction == "S":
                    coordinate[1] -= step

    except:
        continue

print(str(coordinate[0]) + "," + str(coordinate[1]))