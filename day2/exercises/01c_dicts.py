# -*- coding: utf-8 -*-

""" ÖVNING:
"""

stockholm = {
    'unemployment_2009': 4.0,
    'unemployment_2014': 5.1
}

solna = {
    'unemployment_2009': 2.7,
    'unemployment_2014': 4.1
}

"""
STEG 1:
Ge stockholm och solna en ny egenskap som heter "change"
och som beskriver förändringen.
"""
stockholm ["change"] = stockholm["unemployment_2014"] - stockholm["unemployment_2009"] # Skriv kod här!
solna ["change"] = solna["unemployment_2014"] - solna["unemployment_2009"] # Skriv kod här!

"""
STEG 2:
Räkna ut hur mycket större ökningen i arbetslöshet var i Solna.
"""
proc_change = ((solna["change"]) - (stockholm["change"])) / (stockholm["change"]) * 100
procentenhter_change = ((solna["change"]) - (stockholm["change"]))
print "Ökningen i arbetslöshet i Solna jämfört med Stockholm var %s procentenheter, alltså %d procent, hahaha-HAAAHAAAHAHA." % (procentenhter_change, proc_change)

# Skriv kod här!
