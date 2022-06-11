def pair_of_gloves(gloves):
    number = 0
    colors = {}

    for glove in gloves:
        if glove not in colors:
            colors[glove] = 1
        else:
            colors[glove] += 1

    for key, value in colors.items():
        number += value // 2

    return number

if __name__ == "__main__":
    print(pair_of_gloves(['red', 'red', 'green', 'blue', 'blue']))
