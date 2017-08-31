def gcd(a, b):
    if (b < a):
        a, b = b, a
    if (a == 0):
        return b
    else:
        c = b % a
        return gcd(c, a)
print(gcd(100, 36))