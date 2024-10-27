def reduction(p):
    if p >= 50:
        M = p *0.7
    else:
        M = p
    return M

print(reduction(50))