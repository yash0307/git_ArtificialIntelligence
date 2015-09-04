import sys
import random
import signal
import copy
#Timer handler, helper function
probability_block_favoured = []
probability_cell_favoured = {}
probability_block_favoured_bitch = []
probability_cell_favoured_bitch = {}
flag_init = 0
class TimedOutExc(Exception):
        pass

def handler(signum, frame):
    #print 'Signal handler called with signal', signum
    raise TimedOutExc()
class Manual_player:
	def __init__(self):
		pass
	def move(self, temp_board, temp_block, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"	
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))
class Player1:
	
	def __init__(self):
		pass

	def move(self,temp_board,temp_block,old_move,flag):
#		while(1):
#			pass
		for_corner = [0,2,3,5,6,8]

		#List of permitted blocks, based on old move.
		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

                for i in reversed(blocks_allowed):
                    if temp_block[i] != '-':
                        blocks_allowed.remove(i)
	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
		#cells are free cells and allowed block are those which we got to deal with.
		#entire code and stuff goes here :D :D 
		#think about what to do ??
		global flag_init, probability_block_favoured, probability_cell_favoured, probability_block_favoured_bitch, probability_cell_favoured_bitch
		if(flag_init == 0):
			flag_init = 1
			if(flag == 'x'):
				probability_block_favoured.append(300)
				l = [200,300,200,400,200,300,200,300]
				probability_block_favoured_bitch.append(300)
				probability_block_favoured.extend(l)
				probability_block_favoured_bitch.extend(l)
				for i in xrange(0,9):
					for j in xrange(0,9):
						temp = (i,j)
						temp_i = i%3
						temp_j = j%3
						if(temp_i==0 and temp_j == 0):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 0 and temp_j == 1):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 0 and temp_j == 2):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 1 and temp_j == 0):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 1 and temp_j == 1):
							probability_cell_favoured[temp] = 400
							probability_cell_favoured_bitch[temp] = 400
						elif(temp_i == 1 and temp_j == 2):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 2 and temp_j == 0):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 2 and temp_j == 1):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 2 and temp_j == 2):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300			
			elif(flag == 'o'):
				block_affected = (old_move[0]/3)*3 + (old_move[1]/3)
				r = range(0,9)
				#blocks will not be affected on first move, assuming the blocks to be affected when it is either won or drawn.
				probability_block_favoured.append(300)
				l = [200,300,200,400,200,300,200,300]
				probability_block_favoured_bitch.append(300)
				probability_block_favoured.extend(l)
				probability_block_favoured_bitch.extend(l)
				for i in r:
					cells_in_block = []
					i_x = i/3
					i_y = i%3
					if(i_x == 0):
						i_x = 1
					elif(i_x == 1):
						i_x = 4
					elif(i_x == 2):
						i_x = 7
					if(i_y == 0):
						i_y = 1
					elif(i_y == 1):
						i_y = 4
					elif(i_y == 2):
						i_y = 7
					range_x = range(i_x -1 , i_x + 2)
					range_y = range(i_y - 1 , i_y + 2)
					for j in xrange(0,3):
						for k in xrange(0,3):
							temp = (range_x[j], range_y[k])
							cells_in_block.append(temp)
					for j in xrange(0,9):
						temp = cells_in_block[j]
						temp_i = cells_in_block[j][0]%3
						temp_j = cells_in_block[j][1]%3
						if(temp_i==0 and temp_j == 0):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 0 and temp_j == 1):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 0 and temp_j == 2):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 1 and temp_j == 0):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 1 and temp_j == 1):
							probability_cell_favoured[temp] = 400
							probability_cell_favoured_bitch[temp] = 400
						elif(temp_i == 1 and temp_j == 2):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 2 and temp_j == 0):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
						elif(temp_i == 2 and temp_j == 1):
							probability_cell_favoured[temp] = 200
							probability_cell_favoured_bitch[temp] = 200
						elif(temp_i == 2 and temp_j == 2):
							probability_cell_favoured[temp] = 300
							probability_cell_favoured_bitch[temp] = 300
				i_x = block_affected/3
				i_y = block_affected%3
				if(i_x == 0):
					i_x = 1
				elif(i_x == 1):
					i_x = 4
				elif(i_x == 2):
					i_x = 7
				if(i_y == 0):
					i_y = 1
				elif(i_y == 1):
					i_y = 4
				elif(i_y == 2):
					i_y = 7
				range_x = range(i_x -1 , i_x + 2)
				range_y = range(i_y - 1 , i_y + 2)
				cells_in_block = []
				for j in xrange(0,3):
					for k in xrange(0,3):
						temp = (range_x[j], range_y[k])
						cells_in_block.append(temp)
				for j in xrange(0,9):
					temp = cells_in_block[j]
					temp_i = cells_in_block[j][0]%3
					temp_j = cells_in_block[j][1]%3
					old_move_xmod = old_move[0]%3
					old_move_ymod = old_move[1]%3
					if(old_move_xmod - temp_i == 0):
						slope = 0
					elif(old_move_xmod - temp_i != 0):
						slope = float(float((old_move_ymod - temp_j))/float((old_move_xmod - temp_i)))
					if(old_move[0] == temp[0] and old_move[1] == temp[1]):
						probability_cell_favoured[temp] -= 100
						probability_cell_favoured_bitch[temp] += 100
					##Adjacent and blocking stuff, change here in future :P.
					elif((old_move!=temp)and(slope == 0 or slope == 1 or slope == -1)):
						probability_cell_favoured[temp] -= 100
						probability_cell_favoured_bitch[temp] += 100
			return cells[random.randrange(len(cells))]
		elif(flag_init == 1):
			move = min_max(temp_board, temp_block,flag, cells)
			return move
		return cells[random.randrange(len(cells))]
def cutoff_test(temp_board, depth,d):
	if(depth > d):
		return True
	else:
		return False
def eval_fn(temp_board):
	return random.randint(0,1000)
def alphabeta_search(state, d=5, flag, temp_block, old_move):
	if(flag=='x'):
		player = 'x'
	elif(flag=='o'):
		player = 'o'
	def max_value(state, alpha, beta, depth):
		if(cutoff_test(state,depth,d)==True):
			return eval_fn(state, flag)
		v = -float("inf")
		next_moves = []
		next_moves = cells_allowed(state,temp_block,old_move,flag)
		for i in next_moves:
			s = change_state(state, i, flag)
			v = max(v,min_value(s, alpha, beta, depth+1))
			if v >= beta:
				return v
			alpha = max(alpha,v)
		return v
	def min_value(state, alpha, beta, depth):
		if(cutoff_test(state,depth,d)== True):
			return eval_fn(state)
		v = float("inf")
		next_moves = []
		next_moves = cells_allowed(state,temp_block,old_move,flag)
		for i in next_moves:
			s = change_state(state,i,flag)
			v = min(v,max_value(s,alpha,beta,depth+1))
			if v <= alpha:
				return v
			beta = min(beta,v)
		return v
def change_state(state, move, flag):
	if(flag == 'x'):
		state[move[0]][move[1]] = 'x'
	else:
		state[move[0]][move[1]] = 'o'
def min_max(temp_board, temp_block,flag, cells):
	"""boards = {}
	parent_level_one = copy.copy(temp_board)
	print parent_level_one
	boards[parent_level_one] = []
	for i in cells:
		change_level_one = copy.copy(parent_level_one)
		change_level_one[cells[i][0]][cells[i][1]] = 'x'
		child_level_one = copy.copy(change_level_one)
		boards[parent_level_one].append(child_level_one)
		cells_for_level_two = cells_allowed(child_level_one, temp_block, (cells[i][0], cells[i][1]), flag)
		parent_level_two = copy.copy(child_level_one)
		boards[parent_level_two] = []
		for j in cells_for_level_two:
			change_level_two = copy.copy(parent_level_two)
			change_level_two[cells_for_level_two[j][0]][cells_for_level_two[j][1]] = 'o'
			child_level_two = copy.copy(change_level_two)
			boards[parent_level_two].append(child_level_two)
	print boards"""
	boards_level1 =[]
	boards_level2 =[]
	cells_allowed_level1 = []
	tupple_level1 = []
	tupple_level2 = []
	for i in cells:
		parent_level0 = []
		for j in xrange(0,9):
			temp = copy.copy(temp_board[j])
			parent_level0.append(temp)
		parent_level0[i[0]][i[1]] = 'x'
		tupple_level1.append(i)
		cells_allowed_level1.append(cells_allowed(parent_level0,temp_block,i,flag))
		boards_level1.append(parent_level0)

	for i in boards_level1:
		temp_list=[]
		temp_list_tuple=[]
		for j in cells_allowed_level1[boards_level1.index(i)]:
			parent_level1=[]
			for k in xrange(0,9):
				temp = copy.copy(i[k])
				parent_level1.append(temp)
			parent_level1[j[0]][j[1]] = 'o'
			temp_list_tuple.append(j)
			temp_list.append(parent_level1)
		tupple_level2.append(temp_list_tuple)
		boards_level2.append(temp_list) 

	probability_level2=[]
	for i in boards_level2:
		temp_list2=[]
		for j in i:
			prob = random.randint(0,500)
			temp_list2.append(prob)
		probability_level2.append(temp_list2)
	#print probability_level2

	probability_level1=[]
	for i in probability_level2:
		temp = min(i)
		probability_level1.append(temp)

	final = max(probability_level1)
	move_to_be_made = tupple_level1[probability_level1.index(final)]
	return move_to_be_made
	#print probability_level1
	#print final


def cells_allowed(temp_board,temp_block,old_move,flag):
	#		while(1):
#			pass
		for_corner = [0,2,3,5,6,8]

		#List of permitted blocks, based on old move.
		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

                for i in reversed(blocks_allowed):
                    if temp_block[i] != '-':
                        blocks_allowed.remove(i)
	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board, blocks_allowed,temp_block)
		return cells


def fucking_heu_cell(temp_board,block, flag,flag_init, probability_block_favoured, probability_cell_favoured, probability_block_favoured_bitch, probability_cell_favoured_bitch):
	i_x = block/3
	i_y = block%3
	if(i_x == 0):
		i_x = 1
	elif(i_x == 1):
		i_x = 4
	elif(i_x == 2):
		i_x = 7
	if(i_y == 0):
		i_y = 1
	elif(i_y == 1):
		i_y = 4
	elif(i_y == 2):
		i_y = 7
	range_x = range(i_x -1 , i_x + 2)
	range_y = range(i_y - 1 , i_y + 2)
	cells_in_block = []
	for j in xrange(0,3):
		for k in xrange(0,3):
			temp = (range_x[j], range_y[k])
			cells_in_block.append(temp)
	if(flag == 'x'):
		for i in cells_in_block:
			if(temp_board[cells_in_block[i][0]][cells_in_block[i][1]] == 'x'):
				for j in xrange(0,9):
					temp = cells_in_block[j]
					temp_i = cells_in_block[j][0]%3
					temp_j = cells_in_block[j][1]%3
					old_move_xmod = cells_in_block[i][0]%3
					old_move_ymod = cells_in_block[i][1]%3
					if(old_move_xmod - temp_i == 0):
						slope = 0
					elif(old_move_xmod - temp_i != 0):
						slope = float(float((old_move_ymod - temp_j))/float((old_move_xmod - temp_i)))
					if(old_move[0] == temp[0] and old_move[1] == temp[1]):
						probability_cell_favoured[temp] -= 100
						probability_cell_favoured_bitch[temp] += 100
					##Adjacent and blocking stuff, change here in future :P.
					elif((old_move!=temp)and(slope == 0 or slope == 1 or slope == -1)):
						probability_cell_favoured[temp] -= 100
						probability_cell_favoured_bitch[temp] += 100
			elif(temp_board[cells_in_block[i][0]][cells_in_block[i][1]] == 'o'):
				for j in xrange(0,9):
					temp = cells_in_block[j]
					temp_i = cells_in_block[j][0]%3
					temp_j = cells_in_block[j][1]%3
					old_move_xmod = cells_in_block[i][0]%3
					old_move_ymod = cells_in_block[i][1]%3
					if(old_move_xmod - temp_i == 0):
						slope = 0
					elif(old_move_xmod - temp_i != 0):
						slope = float(float((old_move_ymod - temp_j))/float((old_move_xmod - temp_i)))
					if(old_move[0] == temp[0] and old_move[1] == temp[1]):
						probability_cell_favoured[temp] += 100
						probability_cell_favoured_bitch[temp] -= 100
					##Adjacent and blocking stuff, change here in future :P.
					elif((old_move!=temp)and(slope == 0 or slope == 1 or slope == -1)):
						probability_cell_favoured[temp] += 100
						probability_cell_favoured_bitch[temp] -= 100
	elif(flag == 'o'):
		pass			
class Player2:
	
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		for_corner = [0,2,3,5,6,8]

		#List of permitted blocks, based on old move.
		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]
                
                for i in reversed(blocks_allowed):
                    if temp_block[i] != '-':
                        blocks_allowed.remove(i)

	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board,blocks_allowed,temp_block)
		return cells[random.randrange(len(cells))]

#Initializes the game
def get_init_board_and_blockstatus():
	board = []
	for i in range(9):
		row = ['-']*9
		board.append(row)
	
	block_stat = ['-']*9
	return board, block_stat

# Checks if player has messed with the board. Don't mess with the board that is passed to your move function. 
def verification_fails_board(board_game, temp_board_state):
	return board_game == temp_board_state	

# Checks if player has messed with the block. Don't mess with the block array that is passed to your move function. 
def verification_fails_block(block_stat, temp_block_stat):
	return block_stat == temp_block_stat	

#Gets empty cells from the list of possible blocks. Hence gets valid moves. 
def get_empty_out_of(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		for i in range(9):
			for j in range(9):
                                no = (i/3)*3
                                no += (j/3)
				if gameb[i][j] == '-' and block_stat[no] == '-':
					cells.append((i,j))	
	return cells
		
# Note that even if someone has won a block, it is not abandoned. But then, there's no point winning it again!
# Returns True if move is valid
def check_valid_move(game_board,block_stat, current_move, old_move):

	# first we need to check whether current_move is tuple of not
	# old_move is guaranteed to be correct
	if type(current_move) is not tuple:
		return False
	
	if len(current_move) != 2:
		return False

	a = current_move[0]
	b = current_move[1]	

	if type(a) is not int or type(b) is not int:
		return False
	if a < 0 or a > 8 or b < 0 or b > 8:
		return False

	#Special case at start of game, any move is okay!
	if old_move[0] == -1 and old_move[1] == -1:
		return True


	for_corner = [0,2,3,5,6,8]

	#List of permitted blocks, based on old move.
	blocks_allowed  = []

	if old_move[0] in for_corner and old_move[1] in for_corner:
		## we will have 3 representative blocks, to choose from

		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			## top left 3 blocks are allowed
			blocks_allowed = [0,1,3]
		elif old_move[0] % 3 == 0 and old_move[1] in [2,5,8]:
			## top right 3 blocks are allowed
			blocks_allowed = [1,2,5]
		elif old_move[0] in [2,5,8] and old_move[1] % 3 == 0:
			## bottom left 3 blocks are allowed
			blocks_allowed  = [3,6,7]
		elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
			### bottom right 3 blocks are allowed
			blocks_allowed = [5,7,8]

		else:
			print "SOMETHING REALLY WEIRD HAPPENED!"
			sys.exit(1)

	else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
		if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
			## upper-center block
			blocks_allowed = [1]
	
		elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
			## middle-left block
			blocks_allowed = [3]
		
		elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
			## lower-center block
			blocks_allowed = [7]

		elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
			## middle-right block
			blocks_allowed = [5]

		elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
			blocks_allowed = [4]

        #Check if the block is won, or completed. If so you cannot move there. 

        for i in reversed(blocks_allowed):
            if block_stat[i] != '-':
                blocks_allowed.remove(i)
        
        # We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
        cells = get_empty_out_of(game_board, blocks_allowed,block_stat)

	#Checks if you made a valid move. 
        if current_move in cells:
     	    return True
        else:
    	    return False

def update_lists(game_board, block_stat, move_ret, fl):
	#move_ret has the move to be made, so we modify the game_board, and then check if we need to modify block_stat
	game_board[move_ret[0]][move_ret[1]] = fl

	block_no = (move_ret[0]/3)*3 + move_ret[1]/3
	id1 = block_no/3
	id2 = block_no%3
	mg = 0
	mflg = 0
	if block_stat[block_no] == '-':
		if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
		if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
		
                if mflg != 1:
                    for i in range(id2*3,id2*3+3):
                        if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-':
                                mflg = 1
                                break

                ### row-wise
		if mflg != 1:
                    for i in range(id1*3,id1*3+3):
                        if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-':
                                mflg = 1
                                break

	
	if mflg == 1:
		block_stat[block_no] = fl
	
        #check for draw on the block.

        id1 = block_no/3
	id2 = block_no%3
        cells = []
	for i in range(id1*3,id1*3+3):
	    for j in range(id2*3,id2*3+3):
		if game_board[i][j] == '-':
		    cells.append((i,j))

        if cells == [] and mflg!=1:
            block_stat[block_no] = 'd' #Draw
        
        return

def terminal_state_reached(game_board, block_stat):
	
        #Check if game is won!
        bs = block_stat
	## Row win
	if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!='-' and bs[1]!='d') or (bs[3]!='d' and bs[3]!='-' and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!='d' and bs[6]!='-' and bs[6] == bs[7] and bs[7] == bs[8]):
		print block_stat
		return True, 'W'
	## Col win
	elif (bs[0]!='d' and bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!='-') or (bs[1]!='d'and bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!='-') or (bs[2]!='d' and bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!='-'):
		print block_stat
		return True, 'W'
	## Diag win
	elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!='-' and bs[0]!='d') or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!='-' and bs[2]!='d'):
		print block_stat
		return True, 'W'
	else:
		smfl = 0
		for i in range(9):
			for j in range(9):
				if game_board[i][j] == '-' and block_stat[(i/3)*3+(j/3)] == '-':
					smfl = 1
					break
		if smfl == 1:
                        #Game is still on!
			return False, 'Continue'
		
		else:
                        #Changed scoring mechanism
                        # 1. If there is a tie, player with more boxes won, wins.
                        # 2. If no of boxes won is the same, player with more corner move, wins. 
                        point1 = 0
                        point2 = 0
                        for i in block_stat:
                            if i == 'x':
                                point1+=1
                            elif i=='o':
                                point2+=1
			if point1>point2:
				return True, 'P1'
			elif point2>point1:
				return True, 'P2'
			else:
                                point1 = 0
                                point2 = 0
                                for i in range(len(game_board)):
                                    for j in range(len(game_board[i])):
                                        if i%3!=1 and j%3!=1:
                                            if game_board[i][j] == 'x':
                                                point1+=1
                                            elif game_board[i][j]=='o':
                                                point2+=1
			        if point1>point2:
				    return True, 'P1'
			        elif point2>point1:
				    return True, 'P2'
                                else:
				    return True, 'D'	


def decide_winner_and_get_message(player,status, message):
	if player == 'P1' and status == 'L':
		return ('P2',message)
	elif player == 'P1' and status == 'W':
		return ('P1',message)
	elif player == 'P2' and status == 'L':
		return ('P1',message)
	elif player == 'P2' and status == 'W':
		return ('P2',message)
	else:
		return ('NO ONE','DRAW')
	return


def print_lists(gb, bs):
	print '=========== Game Board ==========='
	for i in range(9):
		if i > 0 and i % 3 == 0:
			print
		for j in range(9):
			if j > 0 and j % 3 == 0:
				print " " + gb[i][j],
			else:
				print gb[i][j],

		print
	print "=================================="

	print "=========== Block Status ========="
	for i in range(0, 9, 3):
		print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
	print "=================================="
	print
	

def simulate(obj1,obj2):
	
	# Game board is a 9x9 list, block_stat is a 1D list of 9 elements
	game_board, block_stat = get_init_board_and_blockstatus()

	pl1 = obj1 
	pl2 = obj2

	### basically, player with flag 'x' will start the game
	pl1_fl = 'x'
	pl2_fl = 'o'

	old_move = (-1, -1) # For the first move

	WINNER = ''
	MESSAGE = ''

        #Make your move in 6 seconds!
	TIMEALLOWED = 60

	print_lists(game_board, block_stat)

	while(1):

		# Player1 will move
		
		temp_board_state = game_board[:]
		temp_block_stat = block_stat[:]
	
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		# Player1 to complete in TIMEALLOWED secs. 
		try:
			ret_move_pl1 = pl1.move(temp_board_state, temp_block_stat, old_move, pl1_fl)
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'TIMED OUT')
			break
		signal.alarm(0)
	
                #Checking if list hasn't been modified! Note: Do not make changes in the lists passed in move function!
		if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			#Player1 loses - he modified something
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
		
		# Check if the move made is valid
		if not check_valid_move(game_board, block_stat,ret_move_pl1, old_move):
			## player1 loses - he made the wrong move.
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 1 made the move:", ret_move_pl1, 'with', pl1_fl

                #So if the move is valid, we update the 'game_board' and 'block_stat' lists with move of pl1
                update_lists(game_board, block_stat, ret_move_pl1, pl1_fl)

		# Checking if the last move resulted in a terminal state
		gamestatus, mesg =  terminal_state_reached(game_board, block_stat)
		if gamestatus == True:
			print_lists(game_board, block_stat)
			WINNER, MESSAGE = decide_winner_and_get_message('P1', mesg,  'COMPLETE')	
			break

		
		old_move = ret_move_pl1
		print_lists(game_board, block_stat)

                # Now player2 plays

                temp_board_state = game_board[:]
                temp_block_stat = block_stat[:]


		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		try:
                	ret_move_pl2 = pl2.move(temp_board_state, temp_block_stat, old_move, pl2_fl)
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'TIMED OUT')
			break
		signal.alarm(0)

                if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
			
                if not check_valid_move(game_board, block_stat,ret_move_pl2, old_move):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 2 made the move:", ret_move_pl2, 'with', pl2_fl
                
                update_lists(game_board, block_stat, ret_move_pl2, pl2_fl)

		gamestatus, mesg =  terminal_state_reached(game_board, block_stat)
                if gamestatus == True:
			print_lists(game_board, block_stat)
                        WINNER, MESSAGE = decide_winner_and_get_message('P2', mesg,  'COMPLETE' )
                        break
		old_move = ret_move_pl2
		print_lists(game_board, block_stat)
	
	print WINNER + " won!"
	print MESSAGE

if __name__ == '__main__':
	## get game playing objects

	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)
 
	obj1 = ''
	obj2 = ''
	option = sys.argv[1]	
	if option == '1':
		obj1 = Player1()
		obj2 = Player2()

	elif option == '2':
		obj1 = Player1()
		obj2 = Manual_player()
	elif option == '3':
		obj1 = Manual_player()
		obj2 = Manual_player()
        
        # Deciding player1 / player2 after a coin toss
        # However, in the tournament, each player will get a chance to go 1st. 
        num = random.uniform(0,1)
        if num > 0.5:
		simulate(obj2, obj1)
	else:
		simulate(obj1, obj2)
