"""
HHEK
AWE: Python
IS119
VRW
Übung Prof. Ungerechtmann
"""

"""
import random
import math
"""

print("Herzlich willkommen bei der automatisierten Abschlussnotenvergabe von Prof. Ungerechtmann:")
print("Sie können folgende Noten eingeben:\n"
      "Sehr gut +: 0.7 \t Sehr gut: 1 \t Sehr gut -: 1.3\n"
      "Gut +: 1.7 \t Gut: 2 \t Gut -: 2.3\n"
      "Befriedigend +: 2.7 \t Befriedigend: 3 \t Befriedigend -: 3.3\n"
      "Ausreichend +: 3.7 \t Ausreichend: 4 \t Ausreichend -: 4.3\n"
      "Mangelhaft +: 4.7 \t Mangehalft: 5 \t Mangehalft -: 5.3\n"
      "Ungenügend: 6\n")

pruefungsnote = float(input("Geben sie bitte eine Note nach dem obigen Schema ein:\n"))

augenfarbe = int(input("Hat der Prüfling dunkle [1] oder helle [0] Augen?\n"))

frisur = int(input("Hat der Prüfling kurze [1] oder lange [0] Haare?\n"))

wetter = int(input("Ist das Wetter schön? Ja [1] Nein [0]\n"))

if augenfarbe == 1:
    if frisur == 1:
        abschlussnote = pruefungsnote * 1.1
    else:
        abschlussnote = pruefungsnote * 0.9
else:
    if frisur == 1:
        abschlussnote = pruefungsnote * 0.9
    else:
        abschlussnote = pruefungsnote * 1.1

if wetter == 1:
    abschlussnote = abschlussnote - 1

abschlussnote = abschlussnote * 3
abschlussnote = round(abschlussnote)
abschlussnote = abschlussnote / 3
abschlussnote = round(abschlussnote, 1)

print("Die Abschlussnote des Prüflings ist:", abschlussnote)
