# -*- coding: utf-8 -*-

""" ÖVNING
"""

stockholm = {
    'unemployment_2009': 4.0,
    'unemployment_2014': 5.1
}

solna = {
    'unemployment_2009': 2.7,
    'unemployment_2014': 4.1
}


""" Hur många procentenheter har arbetslösheten stigit i Stockholm?
"""
sthlm_diff = (stockholm["unemployment_2014"]) - (stockholm["unemployment_2009"]) # Skriv kod här!
print "Arbetslösheten i Stockholm har stigit med %s procentenheter." % (sthlm_diff)

# print (stockholm[unemployment_2014 - unemployment_2009]) # Skriv kod här!


""" Hur många procentenheter har arbetslösheten stigit i Solna?
"""
solna_diff = (solna["unemployment_2014"]) - (solna["unemployment_2009"]) # Skriv kod här!
print "Arbetslösheten i Solna har stigit med %s procentenheter." % (solna_diff)

# print (solna[unemployment_2014 - unemployment_2009]) # Skriv kod här!


""" Hur mycket högra arbetslöshet hade Stockholm än Solna 2014?
"""
diff = (stockholm["unemployment_2014"]) - (solna["unemployment_2014"]) # Skriv kod här!
print "Arbetslösheten i Stockholm var %d procent större 2014." % (diff / solna["unemployment_2014"] * 100)
