def dec_to_hex(n):
    h = ""
    nm = ["0", "1", "2", "3", "4", "5", "6", "7",
          "8", "9", "A", "B", "C", "D", "E", "F"]
    while n > 0:
        h = nm[n % 16] + h
        n = n // 16
    return h


print(dec_to_hex(15))
print(dec_to_hex(21))
print(dec_to_hex(115))
