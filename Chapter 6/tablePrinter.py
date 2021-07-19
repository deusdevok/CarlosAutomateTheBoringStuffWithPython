def printTable(table):
	colWidths = [0]*len(table)
	for index, t in enumerate(table):
		colWidths[index] = max([len(s) for s in t])

	for row in range(len(table[0])):
		for col in range(len(table)):
			print(table[col][row].rjust(colWidths[col]), end=' ')
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)