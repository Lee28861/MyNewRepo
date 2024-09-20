def gcd(a, b): #Greatest Common Division algorithm
    while b:
        a, b = b, a % b
    return a

print(gcd(91, 35))
