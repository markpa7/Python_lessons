# Sprawdzanie czy podana liczba jest l. pierwszą
#================================================
def trial_division(n: int) -> list:
	a=[]
	
	while n % 2 == 0:
		print("W petli 1, n=",n,a)			# można usunąć
		a.append(2)
		n //= 2
		print("W koncu petli 1, n=",n,a)	# można usunąć
	f=3
	while f*f <= n:
		if n % f == 0:			
			a.append(f)
			n //= f
			print('W petli 2, n=',n,a)		# można usunąć
		else:
			f += 2
	if n != 1 : a.append(n)
	# Tylko nieparzyste liczy są możliwe
	return a 

print('Podaj liczbę:')
licz=input()
licz=int(licz)
wynik=trial_division(licz)
print('Wynik', wynik)