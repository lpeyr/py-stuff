def surchage(nbr_paquets, pds_unit):
    if nbr_paquets * pds_unit > 105:
        return "Surcharge"

    else:
        return "Tout est OK"

# Tests
print(surchage(10, 5))
print(surchage(4, 12))
print(surchage(120, 2))