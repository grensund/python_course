# coding: utf-8
# Här hämtar jag in filen miljopartiet.py i samma mapp
import miljopartiet
import requests # <--  Verktyg för att hämta webbsidor
import BeautifulSoup # <-- Innehåller funktioner för att tolka html

# from bs4 import BeautifulSoup <-- Variant på att importera bs4 enligt dokumentationen

# Här hittar jag på en funktion som gör gement och englifierat. Notera det fina return!
def slugify(name):
	text = name.lower()\
	.replace(" ", "-")\
	.replace("å", "a")\
	.replace("ä", "a")\
	.replace("ö", "o")\
	.replace("Å", "a")\
	.replace("Ä", "a")\
	.replace("Ö", "o")\
	.replace("é", "e")\
	.replace("É", "e")\
	.replace("ü", "u")\
	.replace("Ü", "u")
	return(text)

# Här loopar jag igenom listan mps i miljopartiet.py och kör funktionen. Å printar resultatet.
for mp in miljopartiet.mps:
	mp = slugify(mp)

# Här sparar jag ner en url för varje rad till en ny variabel!
	url = "http://www.mp.se/om/" + mp

# Å här sparar jag ner hela (svars)resultatet från url till en variabel jag kallar response
	response = requests.get(url)

# Sätt all url i en variabel med ett namn jag begriper. OBS notera (response.text)!!!
	html_kod = response.text

# Ladda in html-koden i BeautifulSoup - som ju kommer laddat med ett antal funktioner
	soup = BeautifulSoup.BeautifulSoup(html_kod)

# Här använder vi medföljande funktionen .find för att hitta ex <hi>-taggen
	mp_name = soup.find("h1")
# Å här hämtar vi mejladressen
	mp_mail = soup.find("a", {'class': "email"})
# Å här tar vi telefonnumret
	mp_tel = soup.find("a", {'class': "tel"})

	div_tagg = soup.find("div", {'class': "lead"})
	if div_tagg:
		mp_uppdrag = div_tagg.find("p")
	else:
		mp_uppdrag = ""
	
	print(mp_name, mp_mail, mp_tel, mp_uppdrag)



"""
print(response.text)
"""