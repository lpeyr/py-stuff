def f(x):
    return 2 * x - 4

def signe(x):
    y = f(x)
    if y < 0:
        return f"négatif (x = {x}) (f(x) = {y})"
    else:
        return f"positif (x = {x}) (f(x) = {y})"

# Tests
print(signe(10))
print(signe(-1))