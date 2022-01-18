# ** operacje-pliki.py **
# =======================
nazwa1 = 'linie.txt'
with open(nazwa1, "a") as linia_pliku:
	linia_pliku.write("\nTrzecia Nowa linia z programu")
with open(nazwa1, "r") as linia_pliku:	
	linie = linia_pliku.readlines()

# for alinia in linie:
# alinia = linie
print(*linie)
