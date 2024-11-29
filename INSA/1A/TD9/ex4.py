def table(n: int, m: int) -> str:
    s = ""
    for i in range(1, m+1):
        s += f"{i} x {n} = {i * n}\n"
    return s

for i in range(1, 10):
    print(table(i, 10))