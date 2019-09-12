def error(arg):
    if len(arg) is not 7:
        return (84)
    for i in arg:
        if i.isnumeric() is False or i[0] is '-':
            return (84)
    for i, j in enumerate(arg):
        arg[i] = int(j)
    if arg[0] < 1 or arg[0] > 3 or arg[6] < 0:
        return (84)
    return (0)
