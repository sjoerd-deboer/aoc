def exercise_one(*rules):
    start = [x for x in rules]
    spoken = dict([[x, 0] for x in rules])

    turn = 1
    for s in start:
        spoken[s] = [turn, turn]
        turn += 1
    last_spoken = start[-1]

    difference = 0
    while turn <= 30000000:
        difference = max(spoken[last_spoken]) - min(spoken[last_spoken])
        temp = spoken.get(difference, [turn, turn])
        spoken[difference] = [turn, max(temp)]
        last_spoken = difference
        turn += 1
    return difference


import time

start = time.time()
print(exercise_one(6, 3, 15, 13, 1, 0))
print(time.time() - start)
