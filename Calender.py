import calendar
print("\n \n----------------------|  Calender of 2020  |---------------------\n ")
yy=int(input("Enter Year to Display Calender"))
print(calendar.calendar(yy))
opt=input("Do you want to Find your Current Calender is Leap Year [Y/N] / [Yes/No] / [YES/NO] / [yes/no] :- \n")
if opt=='Y' or opt=='Yes' or opt=='YES' or opt=='yes':
	if(yy%4==0):
		print("The Current Year",yy,"is a leap year")
		opt2=input("Do you want to display all leap years of 21st Century [Y/N] / [Yes/No] / [YES/NO] / [yes/no] :- \n")
		if opt2=='Y' or opt2=='Yes' or opt2=='YES' or opt2=='yes':
			start=2001
			end=2100
			for year in range(start, end):
				if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
					print(year)
		elif(opt2=='N'):
			print("Wrong Choice")
		else:
			print("Wrong Choice")
	else:
		print("The Current Year",yy,"is not a leap Year")
else:
	print("You Choosen Invalid Option")