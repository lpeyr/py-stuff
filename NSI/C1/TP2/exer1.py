def f(x):
    if x >= 2:
        y = 3 * x - 4
    elif -1 < x < 2:
        y = x + 4
    else:
        y = 2 * x + 7
    return y

print(f(0))
print(f(5))
print(f(-3))
print(f(2))