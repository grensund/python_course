# coding: utf-8

total_unemployment_2009 = 8.6
total_unemployment_2014 = 15.0
total_diff = total_unemployment_2014 - total_unemployment_2009


def write_story(municipality, unemployment_2009, unemployment_2014):
	local_diff = unemployment_2014 - unemployment_2009
	text = "För %s låg arbetslösheten ifjol på %s procent." % (municipality, unemployment_2014)
	print(text)
	
	if local_diff > 0.0:
		print("Det var en ökning med %s procentenheter sedan 2009.") % (abs(local_diff))
	elif local_diff < 0.0:
	   	print("Det var en minskning med %s procentenheter sedan 2009.") % (abs(local_diff))
	elif local_diff == 0.0:
		print("Det var faktiskt ingen skillnad alls från 2009.")
	
	if total_diff > local_diff:
		print("Jämfört med resten av landet har %s klarat sig bättre.") % (municipality)
	elif total_diff < local_diff:
		print("Jämfört med resten av landet har %s klarat sig sämre.") % (municipality)
	elif total_diff == local_diff:
		print("Jämfört med resten av landet har %s klarat sig sämre.") % (municipality)

	if total_diff < 0.0:
		print("I riket föll arbetslösheten med %s procentenheter.") % (abs(total_diff))
	elif total_diff > 0.0:
		print("I riket steg arbetslösheten med %s procentenheter.") % (abs(total_diff))
	elif total_diff == 0.0:
		print("I riket låg arbetslösheten på samma nivå för fem år sedan.")


write_story("Stockholm", 7.1, 6.6) 
print("**************")

write_story("Kiruna", 7.6, 4.2) 
print("**************")

write_story("Lessebo", 9.5, 13.2) 
print("**************")

write_story("Mora", 8.5, 8.5) 
print("**************")



"""
Källa: http://www.ekonomifakta.se/sv/Fakta/Regional-statistik/Din-kommun-i-siffror/
"""