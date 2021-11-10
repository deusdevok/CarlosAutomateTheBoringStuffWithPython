import pyinputplus as pyip

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'])

proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])

cheese = pyip.inputYesNo('Do you want cheese? (Y/N): ')

if cheese == 'yes':
	cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])

mayo = pyip.inputYesNo('Do you want mayo? (Y/N): ')
mustard = pyip.inputYesNo('Do you want mustard? (Y/N): ')
lettuce = pyip.inputYesNo('Do you want lettuce? (Y/N): ')
tomato = pyip.inputYesNo('Do you want tomato? (Y/N): ')

numberSandwiches = pyip.inputInt('How many sandwiches you want? ', min=1)

prices = {'wheat': 0.2, 'white': 0.3, 'sourdough': 0.4,
	'chicken': 0.1, 'turkey': 0.2, 'ham': 0.25, 'tofu': 0.3,
	'cheddar': 0.1, 'Swiss': 0.2, 'mozzarella': 0.15,
	'mayo': 0.1, 'mustard': 0.1, 'lettuce': 0.2, 'tomato': 0.2}

price = prices[breadType]+prices[proteinType]
if cheese == 'yes':
	price += prices[cheeseType]
if mayo == 'yes':
	price += prices['mayo']
if mustard == 'yes':
	price += prices['mustard']
if lettuce == 'yes':
	price += prices['lettuce']
if tomato == 'yes':
	price += prices['tomato']

price = price*numberSandwiches

print('The price of your order is ', price)