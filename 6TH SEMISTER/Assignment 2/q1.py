def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return x
    elif exponent < 0:
        return 1 / power(base, -exponent)
    elif exponent > 1:
        return base * power(base, exponent - 1)
    
x = 2
n = 5
result = power(x, n)
print(f"{x}^{n} = {result}")



