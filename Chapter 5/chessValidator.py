def isValidChessBoard(board):
	if not 'bking' in board.values():
		return False
	if not 'wking' in board.values():
		return False

	whiteCount = 0
	blackCount = 0
	whitePawns = 0
	blackPawns = 0

	for k, v in board.items():
		if int(k[0]) < 1 or int(k[0]) > 8:
			return False
		if k[1] not in 'abcdefgh':
			return False
		if v[0] == 'w':
			whiteCount += 1
			if v[1:] == 'pawn':
				whitePawns += 1
		elif v[0] == 'b':
			blackCount += 1
			if v[1:] == 'pawn':
				blackPawns += 1
		else:
			return False

		if whiteCount > 16 or blackCount > 16 or whitePawns > 8 or blackPawns > 8:
			return False

	return True

board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
		  '5g': 'bqueen', '3e': 'wking'}

board2 = {}

board3 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
		  '5g': 'bqueen', '3e': 'wking', '9a': 'bpawn'}	  

print(isValidChessBoard(board1), 'expected True')
print(isValidChessBoard(board2), 'expected False')
print(isValidChessBoard(board3), 'expected False')