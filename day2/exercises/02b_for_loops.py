# -*- coding: utf-8 -*-


unicorns = [
    "Joachim Kerpner",
    "Nina Svanberg",
    "Johan Ronge",
    "Christian Holmén",
    "Fredrik Laurin",
    "Olle Carlsson",
    "Lolo Tode Palm",
    "Martin Jönsson"
]

"""
ÖVNING:
Använd funktionen len(), som funkar på både strängar och listor,
och räkna ut hur många deltagare som har långa respektive korta namn.
"""

long_names = 0
short_names = 0
total_unicorns = len(unicorns)

print("Nu börjar programmet! Låt oss räkna långa och korta namn.")

for unicorn in unicorns:
    if len(unicorn) > 15:
    	long_names = long_names + 1
    else:
		short_names = short_names + 1

    """ Skriv kod med en IF-sats här!"""

print("%s av %s enhörningar har långa namn." % (long_names, total_unicorns))
print("%s av %s enhörningar har korta namn" % (short_names, total_unicorns))
