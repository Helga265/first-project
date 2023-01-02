def cile(a, b, c) -> tuple:
    if a > 0 and b > 0 and c > 0:
        return a, b, c
    else:
        print('Значення повинні бути більше 0!')

def trik(a, b, c) -> bool:
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

def perimt(a, b, c) -> float:
    p = (a + b + c) / 2
    return p

def plosh(p, a, b, c) -> float:
    s = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)
    return round(s, 2)
