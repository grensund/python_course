# -*- coding: utf-8 -*-

import csv

in_file = open("unemployment.csv", "rb")
csv_file = csv.DictReader(in_file, delimiter=',')

""" Det här programmet ska göra samma sak som det förra.
    Återanvänd kod därifrån!
"""
<<<<<<< HEAD
def write_sentence(municipality, unemployment2014, unemployment2013):
	mening = "Arbetslösheten i %s var för förra året %s procent, jämför med %s procent år 2013." % ( municipality, unemployment2014, unemployment2013)
	return(mening)

#def get_text(kommundata):
#	mening = "Arbetslösheten i %s var för förra året %s procent, jämför med %s procent år 2013." % ( kommundata["Kommun"], kommundata["2014"], kommundata["2013"])
#	return(mening)

for row in csv_file:
	print write_sentence(row["Kommun"], row["2014"], row["2013"])


	# Skriv kod här!
#	print("En dynamisk mening")
=======

>>>>>>> 293335bd6b16692b999171b28bef9710632e446a

def write_sentence(municipality, unemployment2014, unemployment2013):
    # Skriv kod här!
    print("En dynamisk mening")

for row in csv_file:
    # Skriv kod här!
    print(line)
