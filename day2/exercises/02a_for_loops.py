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
Gör en for-loop som skriver ut en numrerad deltagarlista.
1. Joachim Kerpner
2. Nina Svanberg
o.s.v.
"""

counter = 0

for unicorn in unicorns:
    counter = counter + 1
    print "%s. %s" % (counter, unicorn)


