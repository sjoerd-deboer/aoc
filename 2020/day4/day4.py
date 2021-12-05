with open("input.txt", "r") as input:
    data = [x.replace("\n", " ") for x in input.read().split("\n\n")]

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def exercise_one():
    return sum([all([(x in passport) for x in required]) for passport in data])


def exercise_two():
    counter = 0
    for passport in data:
        present = all([(x in passport) for x in required])
        if present:
            values = dict([x.split(":") for x in passport.split()])
            byr = 1920 <= int(values["byr"]) <= 2002
            iyr = 2010 <= int(values["iyr"]) <= 2020
            eyr = 2020 <= int(values["eyr"]) <= 2030
            hgt = (("cm" in values["hgt"]) and 150 <= int(values["hgt"].replace("cm", "")) <= 193) or (
                    ("in" in values["hgt"]) and 59 <= int(values["hgt"].replace("in", "")) <= 76)
            hcl = (values["hcl"][0] == "#") and all([(x in "0123456789abcdef") for x in values["hcl"][1:]])
            ecl = values["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            pid = len(values["pid"]) == 9
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                counter += 1
    return counter


print(exercise_one())
print(exercise_two())
