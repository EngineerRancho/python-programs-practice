def days_count(days):
	
	years = days // 365
	months = days // 28 - years*13
	weeks = days // 7 - ((years*13 + months)*4)
	
	
	
	return  years, months, weeks
	
years, months, weeks = days_count(500)
print(years, months, int(weeks))


