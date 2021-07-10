def commaCode(input_list):
	if len(input_list) == 0:
		print('')
		return
	elif len(input_list) == 1:
		print(input_list[0])
		return
	else:
		for index, ele in enumerate(input_list):
			if index < len(input_list)-1 and index != len(input_list)-2:
				print(ele, end=', ')
			elif index == len(input_list)-2:
				print(ele, end=' ')
			else:
				print('and ' + ele + '.\n')

spam1 = ['apples', 'banana', 'tofu', 'cats']
commaCode(spam1)

spam2 = ['apples', 'banana']
commaCode(spam2)

spam3 = ['apples']
commaCode(spam3)

spam4 = []
commaCode(spam4)