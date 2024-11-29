fibonacci = [0, 1]

for i in range(1, 99):
    fibonacci.append(fibonacci[i-1] + fibonacci[i])

print(fibonacci)
