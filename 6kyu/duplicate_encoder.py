def duplicate_encode(word):
    return print("".join([("(" if word.lower().count(x) == 1 else ")") for x in word.lower()]))
duplicate_encode("HlpUS")