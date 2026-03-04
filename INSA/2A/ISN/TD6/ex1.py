class Fraction:
    def __init__(self, n, d):
        self.numerateur = n
        if d == 0:
            raise ValueError("Le dénominateur")
        self.denominateur = d

    def valeur(self):
        return round(self.numerateur / self.denominateur, 2)

    def __str__(self):
        return (
            f"{self.numerateur}/{self.denominateur}"
            if self.numerateur % self.denominateur != 0
            else f"{self.numerateur//self.denominateur}"
        )

    def plus_grand_commun_diviseur(self):
        a = self.denominateur
        b = self.numerateur
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def reduire(self):
        return Fraction(
            self.numerateur // self.plus_grand_commun_diviseur(),
            self.denominateur // self.plus_grand_commun_diviseur(),
        )

    def addition(self, f):
        return Fraction(
            self.numerateur * f.denominateur + self.denominateur * f.numerateur,
            self.denominateur * f.denominateur,
        ).reduire()

    def soustraction(self, f):
        return self.addition(Fraction(-f.numerateur, f.denominateur))

    def multiplication(self, f):
        return Fraction(
            self.numerateur * f.numerateur, self.denominateur * f.denominateur
        ).reduire()

    def division(self, f):
        return Fraction(
            self.numerateur * f.denominateur, self.denominateur * f.numerateur
        ).reduire()

    def __eq__(self, f):
        # 1. réduire self et f
        f1 = self.reduire()
        f2 = f.reduire()
        return f1.numerateur == f2.numerateur and f1.denominateur == f2.denominateur

    def test():
        pass


f1 = Fraction(2, 5)
f2 = Fraction(20, 48)
f3 = Fraction(8, 1)

print(f3.multiplication(Fraction(9, 10)))
print(Fraction(2, 2) == Fraction(4, 4))
print(Fraction(1, 2))
