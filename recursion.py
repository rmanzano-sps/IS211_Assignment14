# Part 1
def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))


print(fibonnaci(8))


# Part 2
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(216, 594))
