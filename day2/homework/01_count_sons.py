# coding: utf-8
from riksdagsledamoter import data

"""
HEMUPPGIFT 1
============
Hur många riksdagsledamöter har ett son-namn?

1) Loopa listan med riksdagsledamöter
2) Kolla om personen har ett "son"-namn
3) Räkna många riksdagsledamöter som har son-namn.

Bonus:
 Räkna hur stor andel av ledamöterna i varje parti som har son-namn.

Den översta raden (from ... import ...) hämtar en lista med riksdagsledamöter
från riksdagsledamoter.py.


OBS: HEMUPPGIFT EXTENDED
========================
Räkna ut hur många riksdagsledamöter som har ett son-namn per parti!


"""

counter_son_names = 0
total_number_of_mps = len(data)

# Här har jag använt "or" i if-satsen för att kombinera två stycken villkor.
for row in data:
    if "son," in row["name"] or "son ," in row["name"]:
    	counter_son_names = counter_son_names + 1

print("Av %s ledamöter har %s son-namn" %(total_number_of_mps, counter_son_names))

