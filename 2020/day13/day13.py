def exercise_one():
    with open("input.txt") as input:
        departTime = int(input.readline())
        ids = [int(x.strip()) for x in input.readline().split(",") if x != "x"]
        busses = [x - (departTime % x) for x in ids]
    indx = busses.index(min(busses))
    return busses[indx] * ids[indx]


def exercise_two():
    with open("input.txt") as input:
        ids = [(x if x == "x" else int(x)) for x in input.readlines()[1].split(",")]
        ids2 = [int(x) for x in ids if x != "x"]
    time = 0
    stepSize = ids2[0]
    for bus in range(1, len(ids2)):
        while (time + ids.index(ids2[bus])) % ids2[bus] != 0:
            time += stepSize
        stepSize *= ids2[bus]
    return time


print(exercise_one())
print(exercise_two())
