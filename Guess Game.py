import random as r
g=r.randint(0,11)
s=1
while True:
	n=int(input('Guess 1 Number between 0 to 11 :- '))
	if n>10:
		print('You are out of Range , Try Again!')
	elif n<=10 or n>=0:
		if n==g:
			print('\nCongratulations ! You won the game in',s,'Attempts')
			print('The Number was',g)
		else:
			s=s+1
			print('Oops ..... Try Again!')
			continue
