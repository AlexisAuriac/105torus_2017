def stripn0(string, n):
    i = 0
    while string.endswith("0") and i < n:
        string = string[:-1]
        i += 1
    return string, i
