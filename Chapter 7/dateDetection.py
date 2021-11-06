import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

def dateDetect(date):
	mo = dateRegex.search(date)

	if mo == None:
		print('Date is not valid')
	else:
		day, month, year = int(mo.group(1)), int(mo.group(2)), int(mo.group(3))

	if day < 1 or day > 31:
		return False

	if month < 1 or month > 12:
		return False

	if year < 1000 or year > 2999:
		return False

	thirtyMonths = [4, 6, 9, 11] # Months with 30 days

	# Check if leap year
	if year%4 == 0:
		if year%100 == 0:
			if year%400 == 0:
				leapYear = True
			else:
				leapYear = False
		else:
			leapYear = True
	else:
		leapYear = False

	if month in thirtyMonths:
		if day == 31:
			return False
	elif month == 2: # February
		if leapYear:
			if day > 29:
				return False
		else:
			if day > 28:
				return False

	return True

dates = [
	'05/12/1986',
	'31/11/1986',
	'05/12/2060',
	'29/02/2060',
	'29/02/2061']

for date in dates:
	print(date, dateDetect(date))