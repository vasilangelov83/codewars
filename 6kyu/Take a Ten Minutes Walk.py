def is_valid_walk(walk):
    n_s = 0
    e_w = 0
    minutes = 10
    for char in walk:
        if char == "n":
            n_s += 1
        else:
            if n_s > 0:
                n_s -= 1
        if char == "w":
            e_w += 1
        else:
            if e_w > 0:
                e_w -= 1
        minutes -= 1

    return print(minutes == 0 and n_s == 0 and e_w == 0)
is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
