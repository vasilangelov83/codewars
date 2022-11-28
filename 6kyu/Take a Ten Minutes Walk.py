def is_valid_walk(walk):
    n = 0
    s = 0
    e = 0
    w = 0
    minutes = 10
    for char in walk:
        if char == "n":
            n += 1
        elif char == "s":
            s += 1
        elif char == "w":
            w += 1
        else:
            e += 1
        minutes -= 1

    return print(minutes == 0 and (e - w) == 0 and n - s == 0)
is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
