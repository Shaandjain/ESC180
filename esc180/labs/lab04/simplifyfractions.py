def simplify_fraction(n, m):
    n = int(n)
    m = int(m)
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(n, m)
    simplified_numerator = n // common_divisor
    simplified_denominator = m // common_divisor
    
    return f"{simplified_numerator}/{simplified_denominator}"

print(simplify_fraction(18, 4))


