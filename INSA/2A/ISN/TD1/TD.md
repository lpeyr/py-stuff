# Ex 3

1.

```sql
SELECT * FROM etudiants WHERE ville = 'GRENOBLE'
```

| Numero | Nom      | Prénom  | Ville    |
| ------ | -------- | ------- | -------- |
| 12042  | MALRAUX  | André   | GRENOBLE |
| 12183  | COMTE    | Auguste | GRENOBLE |
| 12319  | BASTIE   | Maryse  | GRENOBLE |
| 12342  | VERLAINE | Paul    | GRENOBLE |

2.

```sql
SELECT * FROM etudiants WHERE Prenom = 'Louis' AND ville = 'PARIS'
```

| Numero | Nom     | Prénom | Ville |
| ------ | ------- | ------ | ----- |
| 12115  | ARAGON  | Louis  | PARIS |
| 12555  | BLERIOT | Louis  | PARIS |

3.

```sql
SELECT * FROM horaires WHERE jour = 'mardi' AND heure = 11
```

| Cours               | Jour  | Heure |
| ------------------- | ----- | ----- |
| anglais             | mardi | 11    |
| mécanique quantique | mardi | 11    |
| optique géométrique | mardi | 11    |

4.

```sql
SELECT * FROM horaires WHERE jour = 'lundi' AND heure > 8 AND heure < 12
```

| Cours              | Jour  | Heure |
| ------------------ | ----- | ----- |
| analyse 1          | lundi | 8     |
| analyse 2          | lundi | 11    |
| électrostatique    | lundi | 9     |
| théorie des champs | lundi | 10    |

5.

```sql
SELECT * FROM etudiants WHERE ville = 'LYON' OR ville = 'PARIS'
```

| Numero | Nom       | Prénom     | Ville |
| ------ | --------- | ---------- | ----- |
| 12057  | FRANK     | César      | PARIS |
| 12115  | ARAGON    | Louis      | PARIS |
| 12149  | COURBET   | Gustave    | LYON  |
| 12186  | ELUARD    | Paul       | PARIS |
| 12239  | BREL      | Jacques    | PARIS |
| 12245  | CAMUS     | Albert     | LYON  |
| 12284  | PROUST    | Marcel     | LYON  |
| 12291  | GALOIS    | Evariste   | LYON  |
| 12333  | GREEN     | Julien     | PARIS |
| 12335  | PAPIN     | Denis      | PARIS |
| 12351  | MALLARME  | Stéphane   | LYON  |
| 12407  | LUMIERE   | Auguste    | LYON  |
| 12417  | LALO      | Edouard    | PARIS |
| 12487  | SARTRE    | Jean Paul  | PARIS |
| 12541  | BERNARD   | Claude     | LYON  |
| 12544  | CURIE     | Marie      | PARIS |
| 12554  | YOURCENAR | Marguerite | PARIS |
| 12555  | BLERIOT   | Louis      | PARIS |
| 12609  | RENOIR    | Auguste    | LYON  |
| 12664  | GIDE      | André      | LYON  |
| 12713  | CURIE     | Irène      | PARIS |
| 12729  | MANET     | Edouard    | PARIS |
| 12849  | LUMIERE   | Louis      | LYON  |
| 12917  | DURAS     | Marguerite | PARIS |

6.

```sql
SELECT DISTINCT Prenom FROM etudiants ORDER BY Prenom ASC
```

_Résultats non affichés - Cette requête retournerait tous les prénoms distincts des étudiants triés par ordre alphabétique._

7.

```sql
SELECT DISTINCT cours FROM notes WHERE valeur IS NOT NULL
```

8.

```sql
SELECT adresse, NomCours from salles s, cours c WHERE c.NumSalle = s.NumSalle AND s.adresse = 'Ampère nord'
```

| Adresse     | NomCours             |
| ----------- | -------------------- |
| Ampère nord | électricité générale |
| Ampère nord | électrostatique      |
| Ampère nord | magnétostatique      |

9.

```sql
SELECT Prenom, Nom, Ville FROM notes n, etudiants e WHERE n.NumEtudiant = e.Numero AND n.cours = 'analyse 1' AND  n.valeur IS NOT NULL
```

10.

```sql
SELECT DISTINCT NumSalle FROM cours c, horaires h WHERE h.NomCours = c.NomCours AND h.jour = 'lundi'
```

| NumSalle |
| -------- |
| 1        |
| 2        |
| 3        |
| 4        |
| 12       |

11.

```sql
SELECT c.NomCours, NumSalle, heure FROM cours c, horaires h WHERE h.jour  = 'lundi' AND h.NomCours = c.NomCours
ORDER BY heure ASC
```

12.

```sql
SELECT Prenom FROM etudiants e, cours c, notes n WHERE c.Pre_requis IS NULL AND e.Numero = n.NumEtudiant
AND n.valeur >10 AND c.NomCours = n.cours
```

13.

```sql
SELECT DISTINCT s.NumSalle, adresse, h.heure  FROM salles s, horaires h, etudiants e, cours c, notes n
WHERE h.jour = 'mardi' AND h.NomCours = c.NomCours AND e.Nom = 'DEBUSSY'
AND c.NumSalle = s.NumSalle AND n.NumEtudiant = e.Numero  AND n.cours = c.NomCours
ORDER BY h.heure ASC
```

14.

```sql
SELECT DISTINCT Numero, Nom, Prenom, ville FROM etudiants e, notes n, cours c
WHERE e.Numero = n.NumEtudiant AND n.cours = c.NomCours AND c.NomCours LIKE '%ique'
```

15.

```sql
SELECT c2.NomCours FROM cours c1, cours c2 WHERE c1.NomCours = 'analyse 2'
AND c2.Pre_requis = c1.Pre_requis
```

16.

```sql
SELECT Nom, Prenom FROM etudiants e WHERE e.Numero
IN (SELECT NumEtudiant FROM notes n WHERE n.cours = 'Analyse 1' AND n.valeur IS NOT NULL)
```

17.

```sql
SELECT Nom, Prenom FROM etudiants e WHERE e.Numero
IN (SELECT NumEtudiant FROM notes n WHERE n.valeur > 10
AND n.cours
IN (SELECT NomCours FROM cours c WHERE c.Pre_requis IS NULL))
```

18.

```sql
SELECT Nom, Prenom from etudiants WHERE Numero
NOT IN (SELECT NumEtudiant from notes)
```

19.

```sql
SELECT NomCours FROM cours c WHERE c.NumSalle = '2' AND c.NomCours != 'Mécanique générale'
```

20.

```sql
SELECT NomCours, c.NumSalle, adresse FROM cours c, salles s
WHERE c.Pre_requis = 'Analyse 2' and c.NumSalle = s.NumSalle
```

21.

```sql
SELECT c.NomCours, heure FROM cours c, horaires h, salles s WHERE h.NomCours = c.NomCours AND h.jour = 'lundi'
AND s.NumSalle = c.NumSalle AND s.adresse = 'Ampère nord' ORDER BY heure ASC
```

22.

```sql
SELECT adresse FROM salles WHERE NumSalle IN (SELECT NumSalle FROM cours WHERE NomCours LIKE 'analyse%')
```
