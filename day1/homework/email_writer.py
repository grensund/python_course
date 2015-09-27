# -*- coding: utf-8 -*-
"""
Skriv en funktion som tar ett namn och en domän.
Gör namnet mejlkompatibelt och skriv ut en fullständig e-postadress.
"""


def emailify(name, domain):
	text = name.lower()\
		.replace("å", "a")\
		.replace("ä", "a")\
		.replace("ö", "o")\
		.replace("Å", "a")\
		.replace("Ä", "a")\
		.replace("Ö", "o")\
		.replace("é", "e")\
		.replace("É", "e")\
		.replace(" ",".")

	email = "%s@%s" % (text, domain.lower())
	print(email)

# VARIANT MED STEG FÖR STEG I VARIABLER
#    small_name = "%s@%s" % (name.lower(), domain.lower())
#    english_name = small_name.replace("é", "e").replace("å", "a").replace("ä", "a").replace("ö", "o").replace("Å", "a").replace("Ä", "a").replace("Ö", "o")
#    no_dot_name = english_name.replace(" ", ".")
#    print(no_dot_name)


emailify("Annie Lööf", "riksdagen.se")
emailify("David Lång", "riksdagen.se")
emailify("Emma Nohrén", "riksdagen.se")
emailify("阿部慎太郎", "asahi.co.jp")
emailify("Östen Rubin", "dn.se")
emailify("Örjan Stor-Knobben Larsson", "yahoo.nk")
emailify("Åke Grävare-Échelon", "gmail.com")
