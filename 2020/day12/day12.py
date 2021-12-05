with open("input.txt") as input:
    data = [[z[0], int(z[1:])] for z in [x.strip() for x in input]]


def exercise_one(instructions):
    position = [0, 0]
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direction = [1, 0]
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        if action == "L":
            direction = directions[(directions.index(direction) - int(1 * ((value % 360) / 90)))]
        elif action == "R":
            direction = directions[(directions.index(direction) + int(1 * ((value % 360) / 90))) % 4]
        elif action == "F":
            position = [position[0] + value * direction[0], position[1] + value * direction[1]]
        elif action == "N":
            position = [position[0], position[1] + value * 1]
        elif action == "E":
            position = [position[0] + value * 1, position[1]]
        elif action == "S":
            position = [position[0], position[1] - value * 1]
        elif action == "W":
            position = [position[0] - value * 1, position[1]]
        print(action, value, position)
    return int((position[0] ** 2) ** 0.5 + (position[1] ** 2) ** 0.5)


def exercise_two(instructions):
    position = [0, 0]
    waypoint = [10, 1]
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        if action == "L":
            for x in range(0, value // 90):
                waypoint = [-waypoint[1], waypoint[0]]
        elif action == "R":
            for x in range(0, value // 90):
                waypoint = [waypoint[1], -waypoint[0]]
        elif action == "F":
            position = [position[0] + value * waypoint[0], position[1] + value * waypoint[1]]
        elif action == "N":
            waypoint = [waypoint[0], waypoint[1] + value * 1]
        elif action == "E":
            waypoint = [waypoint[0] + value * 1, waypoint[1]]
        elif action == "S":
            waypoint = [waypoint[0], waypoint[1] - value * 1]
        elif action == "W":
            waypoint = [waypoint[0] - value * 1, waypoint[1]]
    return int((position[0] ** 2) ** 0.5 + (position[1] ** 2) ** 0.5)


print(data)
print(exercise_two(data))
