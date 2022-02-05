with open("input-17.txt", "r") as f:
    x0, y0 = [a[2:].split("..") for a in f.readline().strip()[13:].split(", ")]
    x_min, x_max = int(x0[0]), int(x0[1])
    y_min, y_max = int(y0[0]), int(y0[1])


def in_target_area(x, y):
    if x_max >= x >= x_min:
        if y_max >= y >= y_min:
            return y
    return None


probes = []
max_y = -9999999999


def probe(x_velocity, y_velocity, find_y=False):
    global max_y
    i_x, i_y = x_velocity, y_velocity
    x, y = 0, 0
    while True:
        x += x_velocity
        y += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1
        y_velocity -= 1
        if x > x_max or y_min > y:
            break
        if find_y:
            if y > max_y:
                max_y = y
            if in_target_area(x, y):
                break
        else:
            z = in_target_area(x, y)
            if z:
                probes.append([i_x, i_y])
                if y_velocity < 0:
                    break


if __name__ == "__main__":
    r = 150
    for x in range(-r, r):
        for y in range(-r, r):
            if x or y:
                probe(x, y)
    for p in probes:
        probe(p[0], p[1], find_y=True)
    print("Part 1: %s" % max_y)
    print("Part 2: %s" % len(probes))
