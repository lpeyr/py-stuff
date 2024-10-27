def f(a, b):
    a = a + b
    b = b - a
    c = b - a
    return (a, c)

print(f(5, 4))