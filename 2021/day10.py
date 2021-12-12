with open("input-10.txt", "r") as f:
    p = [x.strip() for x in f.readlines()]
    correct_lines = []


def one():
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    wrong = []
    for line in p:
        o = []
        incorrect_line = False
        for char in line:
            opening = {")": "(", "]": "[", "}": "{", ">": "<"}
            if char in "([{<":
                o.append(char)
            else:
                if opening[char] == o[-1]:
                    del o[-1]
                else:
                    wrong.append(char)
                    incorrect_line = True
                    break
        if not incorrect_line:
            correct_lines.append(line)
    return sum([score[x] for x in wrong])


def two():
    closing = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in correct_lines:
        opening = []
        for char in line:
            if char in "({[<":
                opening.append(char)
            else:
                del opening[-1]
        score = 0
        for c in reversed(opening):
            score = (score * 5) + closing[c]
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    print(one())
    print(two())
