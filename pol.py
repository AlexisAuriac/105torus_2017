def derive(coef):
    degree = len(coef)
    derived = list()

    i = 1
    while i < len(coef):
        derived.append(coef[i] * i)
        i += 1
    return derived

def compute(pol, x):
    result = 0

    for power, coef in enumerate(pol):
        result += coef * pow(x, power)
    return result
