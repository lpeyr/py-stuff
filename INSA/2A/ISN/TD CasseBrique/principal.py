from Brique import *
from brique_speciale import *
from casse_briques import *
from CasseBriquesGUI import *

a = Brique("red", 60, 20, 50, 25, 3, 10)
b = BriqueSpeciale("red", 60, 20, 50, 25, 3, 10, "Double Score")

print(b.is_hit((65, 25)))
casse = CasseBriques()
casse.construire_rangee_briques("red", 2, 2, 10)
casse.construire_rangee_briques("yellow", 1, 1, 5, 5, 2)
casse.construire_rangee_briques("green", 1, 1, 2, 5, 3)
casse.construire_rangee_briques("blue", 1, 1, 3, 5, 4)
a = CasseBriquesGUI(casse)

a.demarrer()
