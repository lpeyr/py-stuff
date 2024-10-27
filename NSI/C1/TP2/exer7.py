def imc(masse, taille):
    return masse / taille ** 2


t = input("Quel est votre taille (m) ?\n>  ")
m = input("Quel est votre poids (kg) ?\n> ")
imc_user = imc(float(m), float(t))

if imc_user < 18.5:
    print(f"Vous êtes en sous-poids (IMC: {imc_user})")
elif imc_user <= 24.9:
    print(f"Vous êtes normal (IMC: {imc_user})")
elif imc_user <= 29.9:
    print(f"Vous êtes en sur-poids (IMC: {imc_user})")
elif imc_user <= 34.9:
    print(f"Vous êtes en obesité (IMC: {imc_user})")
elif imc_user >= 35:
    print(f"Vous êtes en obésité sévère (IMC: {imc_user})")