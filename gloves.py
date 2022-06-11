def pair_of_gloves(gloves):
    """ Calculate how many pair of gloves we have

    Args:
        gloves (list): A list of colors of gloves

    Returns:
        int: Number of pairs we have
    """
    number = 0
    colors = {}

    for glove in gloves:
        if glove not in colors:
            colors[glove] = 1
        else:
            colors[glove] += 1

    for value in colors.values():
        number += value // 2

    return number

if __name__ == "__main__":
    assert pair_of_gloves(['red', 'red', 'green', 'blue', 'blue']) == 2
