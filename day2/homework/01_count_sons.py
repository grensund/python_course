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

Idé: använd for-loop för varje parti tillsammans med if-sats


"""

counter_fp = 0
counter_m = 0
counter_c = 0
counter_kd = 0
counter_s = 0
counter_mp = 0
counter_v = 0
counter_sd = 0

counter_son_names = 0
total_number_of_mps = len(data)

# Här har jag använt "or" i if-satsen för att kombinera två stycken villkor.
for row in data:
    if "son," in row["name"] or "son ," in row["name"]:
    	counter_son_names = counter_son_names + 1

	if "son," in row["name"] or "son ," in row["name"]:
		if "FP" in row["party"]:
			counter_fp = counter_fp + 1
		if "SD" in row["party"]:
			counter_sd = counter_sd + 1
		if "C" in row["party"]:
			counter_c = counter_c + 1
		if "KD" in row["party"]:
			counter_kd = counter_kd + 1
		if "S" in row["party"]:
			counter_s = counter_s + 1
		if "MP" in row["party"]:
			counter_mp = counter_mp + 1
		if "V" in row["party"]:
			counter_v = counter_v + 1
		if "M" in row["party"]:
			counter_m = counter_m + 1
	
print("Av %s ledamöter har %s son-namn" % (total_number_of_mps, counter_son_names))
print("Antal moderater: %s.\
	\nAntal liberaler: %s.\
	\nAntal centerpartister: %s\
	\nAntal kristdemokrater: %s\
	\nAntal sossar: %s.\
	\nAntal miljömuppar: %s\
	\nAntal vpk:are: %s.\
	\nAntal sd:are: %s") % (counter_m, counter_fp, counter_c, counter_kd, counter_s, counter_mp, counter_v, counter_sd)

