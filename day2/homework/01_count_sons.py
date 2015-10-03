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

counter_fp, counter_c, counter_kd, counter_mp, \
counter_v, counter_m, counter_sd, counter_s \
= 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

total_fp, total_c, total_kd, total_mp, \
total_v, total_m, total_sd, total_s \
= 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

counter_son_names = 0.0
total_number_of_mps = len(data)

# Loop för att plocka ut antal förekomster av respektive parti.
for row in data:
	if "FP" in row["party"]:
		total_fp = total_fp + 1
	if "SD" in row["party"]:
		total_sd = total_sd + 1
	if "C" in row["party"]:
		total_c = total_c + 1
	if "KD" in row["party"]:
		total_kd = total_kd + 1
	if "S" in row["party"]:
		total_s = total_s + 1
	if "MP" in row["party"]:
		total_mp = total_mp + 1
	if "V" in row["party"]:
		total_v = total_v + 1
	if "M" in row["party"]:
		total_m = total_m + 1
total_m = total_m - total_mp
total_s = total_s - total_sd
	
# Här har jag använt "or" i if-satsen för att kombinera två stycken villkor.
for row in data:
	if "son," in row["name"] or "son ," in row["name"]:
		counter_son_names = counter_son_names + 1
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
counter_m = counter_m - counter_mp
counter_s = counter_s - counter_sd

# Dubbelräkningen av mp och sd subtraherade från m respektive s.
# Använde %d för att slippa decimaler
print("Av %d ledamöter har %d son-namn" % (total_number_of_mps, counter_son_names))
print("Antal moderater: %d (%d procent).\nAntal liberaler: %d (%d procent).\
	\nAntal centerpartister: %d (%d procent).\nAntal kristdemokrater: %d (%d procent).\
	\nAntal sossar: %d (%d procent).\nAntal miljömuppar: %d (%d procent).\
	\nAntal vpk:are: %d (%d procent).\nAntal sd:are: %d (%d procent).")\
% (counter_m, counter_m / total_m * 100, counter_fp, counter_fp / total_fp * 100, \
	counter_c, counter_c / total_c * 100, counter_kd, counter_kd / total_kd * 100, \
	counter_s, counter_s / total_s * 100, counter_mp, counter_mp / total_mp * 100, \
	counter_v, counter_v / total_v * 100, counter_sd, counter_sd / total_sd * 100)
