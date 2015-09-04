#==========Team 97=======================
#==========Yash Patel(201301134)=========
#==========Saurabh Jain(201301128)========

import copy

class Player97:
	def __init__(self):
		pass

	def move(self,temp_board,temp_block,old_move,flag):
		if (old_move == (-1,-1)):
			probability_block_favoured = self.initialize_data_probability_block_favoured()
			probability_block_favoured_opponent = self.initialize_data_probability_block_favoured_opponent()
			probability_cell_favoured = self.initialize_data_probability_cells_favoured()
			probability_cell_favoured_opponent = self.initialize_data_probability_cells_favoured_opponent()
			move = (4,4)
			return move
		else:
			copied_old_move = old_move
			copied_temp_board = self.copy_2DList(temp_board)
			copied_temp_block = self.copy_1DList(temp_block)
			flag = self.check_player(flag)
			player97 = flag
			cells = self.cells_allowed(copied_old_move,copied_temp_board,copied_temp_block)
			depth_of_root = 0
			moves = self.best_choosen_move(copied_old_move,copied_temp_board,copied_temp_block,cells,flag,depth_of_root,player97)
			return cells[moves[0]]

	def best_choosen_move(self,old_move,temp_board,temp_block,cells,flag,depth,player97):
		copied_old_move = old_move
		if(self.check_depth(depth) == True):
			return 0,old_move,self.Probability(temp_board,temp_block,old_move,player97)
		else:
			score_cells = []
			count = 0
			for i in cells:
				copied_temp_board = self.copy_2DList(temp_board)
				copied_temp_block = self.copy_1DList(temp_block)
				temp_coordinates = (i[0],i[1])
				changed_temp_board = self.make_changes(temp_board, flag, temp_coordinates)
				new_temp_block = self.update_block(temp_board,temp_block,temp_coordinates,flag)
				new_moves_available = self.cells_allowed(temp_coordinates,temp_board,new_temp_block)			
				p = (count,self.best_choosen_move(temp_coordinates, temp_board, new_temp_block, new_moves_available, flag^1, depth+1,player97))
				score_cells.append(p);
				count = count + 1
			if (self.check_if_even(depth)==True):
				txx = self.get_max(score_cells)			
				return txx
			else:
				tyy = self.get_min(score_cells)			
				return tyy

	def get_max(self,list_of_tuple_and_heuristic):
		val_ = -float("inf")
		ma_ =	(0,0)
		index = 0
		for i in list_of_tuple_and_heuristic:
			if i[1][2]>val_:
				val_ = i[1][2]
				ma_ = i[1][1]
				index = i[0]
		return index,ma_,val_



	def get_min(self,list_of_tuple_and_heuristic): 
		val_ = float("inf")
		mi_ = (0,0)
		index = 0
		for i in list_of_tuple_and_heuristic:
			if i[1][2]<val_:
				val_ = i[1][2]
				mi_ = i[1][1]
				index = i[0]
		return index,mi_,val_

	def get_winning_block_situation(self):
		make_list = []
		x = 3
		y = 6
		temp_1 = []
		temp_2 = []
		temp_3 = []
		temp_4 = []
		temp_5 = []
		temp_6 = []
		for i in xrange(0,3):
			temp_1.append(i)
			temp_2.append(i+x)
			temp_3.append(i+y)
			temp_4.append(i*3)
			temp_5.append(i*3 + 1)
			temp_6.append(i*3 + 2)
		make_list.append(tuple(temp_1))
		make_list.append(tuple(temp_2))
		make_list.append(tuple(temp_3))
		make_list.append(tuple(temp_4))
		make_list.append(tuple(temp_5))
		make_list.append(tuple(temp_6))
		make_list.append(tuple([0,4,8]))
		make_list.append(tuple([2,4,6]))
		return make_list

	def decide_player_and_opponent(self, flag):
		if(flag==0):
			return ('x','o')
		else:
			return ('o','x')

	def get_heu_array(self):
		make_list = []
		make_list.append((0,-10,-100,-1000))
		for i in xrange(1,4):
			temp = (pow(10,i),0,0,0)
			make_list.append(temp)
		return make_list

	def Probability(self,temp_board_,temp_block_,tupleofcell,flag_):
		output = self.decide_player_and_opponent(flag_)
		player = output[0]
		opponent = output[1]
		eight_winning_positions = self.get_winning_block_situation()
		Heuristic_Array = self.get_heu_array()
		heuristic_value = 0
		for i in xrange(0,9):
			row_changed = i/3 
			column_changed = i/3 
			x_state = row_changed*3
			y_state = column_changed*3
			for j in xrange(0,8):
				player_move_value = self.heu_player_dominance( eight_winning_positions,x_state,y_state,player,j,temp_board_)
				opponent_move_value = self.heu_opponent_dominance(eight_winning_positions,x_state,y_state,player,j,temp_board_)
				heuristic_value = heuristic_value + Heuristic_Array[player_move_value][opponent_move_value]
		for i in xrange(0,8):
			opponent_move_value = 0
			player_move_value = 0
			for j in xrange(0,3):
				if temp_block_[eight_winning_positions[i][j]] == player:
					player_move_value +=1
				elif temp_block_[eight_winning_positions[i][j]] == opponent:
					opponent_move_value+=1
			heuristic_value = heuristic_value + 5*Heuristic_Array[player_move_value][opponent_move_value]			
		return heuristic_value

	def get_symbol(self,flag):
		if(flag == 0):
			return 'x'
		else:
			return 'o'
			
	def update_block(self, temp_board, temp_block, temp_coordinates, flag):
		new_temp_block = self.copy_1DList(temp_block)
		row_changed = temp_coordinates[0]/3 
		column_changed = temp_coordinates[1]/3 
		block_index = row_changed*3+column_changed
		x_state = row_changed*3
		y_state = column_changed*3
		symbol = self.get_symbol(flag)
		for i in xrange(x_state, x_state + 3):
			count = 0
			for j in xrange(y_state, y_state + 3):
				if(temp_board[i][j]==symbol):
					count+=1
			if(count==3):
				temp_block[block_index] = symbol
		for i in xrange(y_state, y_state + 3):
			count = 0
			for j in xrange(x_state, x_state + 3):
				if(temp_board[i][j]==symbol):
					count+=1
			if(count==3):
				temp_block[block_index] = symbol
		if(temp_board[x_state+0][y_state+0]==symbol and temp_board[x_state+1][y_state+1]==symbol and temp_board[x_state+2][y_state+2]==symbol):
			temp_block[block_index]=symbol
		if(temp_board[x_state+0][y_state+2]==symbol and temp_board[x_state+1][y_state+1]==symbol and temp_board[x_state+2][y_state+0]==symbol):
			temp_block[block_index]=symbol
		return temp_block

	def make_changes(self,temp_board, flag, coordinates):
		copied_temp_board = self.copy_2DList(temp_board)
		if(flag == 0):
			copied_temp_board[coordinates[0]][coordinates[1]] = 'x'
		else:
			copied_temp_board[coordinates[0]][coordinates[1]] = 'o'
		return copied_temp_board

	def check_depth(self,depth):
		if(depth > 2):
			return True
		else:
			return False
	def check_if_even(self,depth):
		if(depth%2==0):
			return True
		else:
			return False
	def get_empty_out_ofx(self,gameb, blal,block_stat):
		cells = []
		for idb in blal:
			id1 = idb/3
			id2 = idb%3
			for i in range(id1*3,id1*3+3):
				for j in range(id2*3,id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))

		if cells == []:
			for i in range(9):
				for j in range(9):
                        	        no = (i/3)*3
                                	no += (j/3)
					if gameb[i][j] == '-' and block_stat[no] == '-':
						cells.append((i,j))	
		return cells

	def check_player(self,flag):
		if(flag == 'x'):
			return 0
		elif(flag == 'o'):
			return 1
		else:
			return False

	def copy_1DList(self,list_1D):
		copied_1dList = []
		copied_1dList = copy.copy(list_1D)
		return copied_1dList
		
	def copy_2DList(self,list_2D):
		copied_2dList = []
		for i in list_2D:
			temp_list = []
			temp_list = copy.copy(i)
			copied_2dList.append(temp_list)
		return copied_2dList

	def initialize_data_probability_block_favoured(self):
		probability_block_favoured = []
		probability_block_favoured.append(300)
		l = [200,300,200,400,200,300,200,300]
		probability_block_favoured.extend(l)
		return probability_block_favoured

	def initialize_data_probability_cells_favoured(self):
		probability_cell_favoured = {}
		for i in xrange(0,9):
			for j in xrange(0,9):
				temp = (i,j)
				temp_i = i%3
				temp_j = j%3
				if(temp_i==0 and temp_j == 0):
					probability_cell_favoured[temp] = 300
				elif(temp_i == 0 and temp_j == 1):
					probability_cell_favoured[temp] = 200
				elif(temp_i == 0 and temp_j == 2):
					probability_cell_favoured[temp] = 300
				elif(temp_i == 1 and temp_j == 0):
					probability_cell_favoured[temp] = 200
				elif(temp_i == 1 and temp_j == 1):
					probability_cell_favoured[temp] = 400
				elif(temp_i == 1 and temp_j == 2):
					probability_cell_favoured[temp] = 200
				elif(temp_i == 2 and temp_j == 0):
					probability_cell_favoured[temp] = 300
				elif(temp_i == 2 and temp_j == 1):
					probability_cell_favoured[temp] = 200
				elif(temp_i == 2 and temp_j == 2):
					probability_cell_favoured[temp] = 300
		return probability_cell_favoured

	def initialize_data_probability_block_favoured_opponent(self):
		probability_block_favoured_opponent = []
		probability_block_favoured_opponent.append(300)
		l = [200,300,200,400,200,300,200,300]
		probability_block_favoured_opponent.extend(l)
		return probability_block_favoured_opponent

	def initialize_data_probability_cells_favoured_opponent(self):
		probability_cell_favoured_opponent = {}
		for i in xrange(0,9):
			for j in xrange(0,9):
				temp = (i,j)
				temp_i = i%3
				temp_j = j%3
				if(temp_i==0 and temp_j == 0):
					probability_cell_favoured_opponent[temp] = 300
				elif(temp_i == 0 and temp_j == 1):
					probability_cell_favoured_opponent[temp] = 200
				elif(temp_i == 0 and temp_j == 2):
					probability_cell_favoured_opponent[temp] = 300
				elif(temp_i == 1 and temp_j == 0):
					probability_cell_favoured_opponent[temp] = 200
				elif(temp_i == 1 and temp_j == 1):
					probability_cell_favoured_opponent[temp] = 400
				elif(temp_i == 1 and temp_j == 2):
					probability_cell_favoured_opponent[temp] = 200
				elif(temp_i == 2 and temp_j == 0):
					probability_cell_favoured_opponent[temp] = 300
				elif(temp_i == 2 and temp_j == 1):
					probability_cell_favoured_opponent[temp] = 200
				elif(temp_i == 2 and temp_j == 2):
					probability_cell_favoured_opponent[temp] = 300
		return probability_cell_favoured_opponent
	
	#from simulator

	def cells_allowed(self,old_move,temp_board,temp_block):
		for_corner = [0,2,3,5,6,8]
	
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
				## bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
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
		cells = self.get_empty_out_ofx(temp_board,blocks_allowed,temp_block)
		return cells

	def heu_player_dominance(self, eight_winning_positions,x_s,y_s,player,j, temp_board_):
		player_move_value = 0
		for k in xrange(0,3):
			x = eight_winning_positions[j][k]
			r_add = x/3
			c_add = x%3
			if(temp_board_[x_s+r_add][y_s+c_add] == player):
				player_move_value+=1
		return player_move_value

	def heu_opponent_dominance(self, eight_winning_positions,x_s,y_s,opponent,j,temp_board_):
		opponent_move_value = 0
		for k in xrange(0,3):
			x = eight_winning_positions[j][k]
			r_add = x/3
			c_add = x%3
			if(temp_board_[x_s+r_add][y_s+c_add]==opponent):
				opponent_move_value+=1
		return opponent_move_value
	
	#from simulator
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

