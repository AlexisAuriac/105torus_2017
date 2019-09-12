def error(arg, nb_arg):
    if len(arg) is not nb_arg:
        return (84)
    for i in arg:
        if i.isnumeric() is False and i[0] is not '-':
            return (84)
    for i, j in enumerate(arg):
        arg[i] = int(j)
    return (0)
