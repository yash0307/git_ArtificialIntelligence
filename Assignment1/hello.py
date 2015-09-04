import copy
class Player97:	
	def __init__(self):
		pass
	

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
			## we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
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


	def best_possible_move(self,prev_move,board,block,listofmoves,fl_,depth,myplayer_):
		prev_move_ = prev_move
		if depth>2:
			return 0,prev_move,self.Heuristic(board,block,prev_move_,myplayer_)
		else:		#if depth is even we have to choose max values of childs else min values of childs
			score_cells = []
			count = 0
			for valid_move in listofmoves:	
				t_board = self.copy_2DList(board)
				t_block = self.copy_1DList(block)
				rr = valid_move[0]
				cc = valid_move[1]
				if fl_ == 0:
					t_board[rr][cc] = 'x'
				else:
					t_board[rr][cc] = 'o'
				new_t_block = self.block_update(t_board,t_block,valid_move,fl_)


				new_list_of_moves = self.cells_allowed(valid_move,t_board,new_t_block)			

				p = (count,self.best_possible_move(valid_move, t_board, new_t_block, new_list_of_moves, fl_^1, depth+1,myplayer_))
				score_cells.append(p);
	
				count = count + 1

			if depth%2==0:
				txx = self.get_max(score_cells)			#even depth

				return txx
			else:
				tyy = self.get_min(score_cells)			#odd depth

				return tyy

	def block_update(self,t_brd,t_blck,v_m,XorO):
		rc = v_m[0]/3 #row change
		cc = v_m[1]/3 #coloumn change
		idx = rc*3+cc
		x_s = rc*3
		y_s = cc*3
		if XorO == 0:
			zz = 'x' ##
		else:
			zz = 'o'
		if(t_brd[x_s+0][y_s+0]==zz and t_brd[x_s+0][y_s+1]==zz and t_brd[x_s+0][y_s+2]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+1][y_s+0]==zz and t_brd[x_s+1][y_s+1]==zz and t_brd[x_s+1][y_s+2]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+2][y_s+0]==zz and t_brd[x_s+2][y_s+1]==zz and t_brd[x_s+2][y_s+2]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+0][y_s+0]==zz and t_brd[x_s+1][y_s+0]==zz and t_brd[x_s+2][y_s+0]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+0][y_s+1]==zz and t_brd[x_s+1][y_s+1]==zz and t_brd[x_s+2][y_s+1]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+0][y_s+2]==zz and t_brd[x_s+1][y_s+2]==zz and t_brd[x_s+2][y_s+2]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+0][y_s+0]==zz and t_brd[x_s+1][y_s+1]==zz and t_brd[x_s+2][y_s+2]==zz):
			t_blck[idx]=zz
		if(t_brd[x_s+0][y_s+2]==zz and t_brd[x_s+1][y_s+1]==zz and t_brd[x_s+2][y_s+0]==zz):
			t_blck[idx]=zz
		return t_blck

	 

	def get_max(self,list_of_tuple_and_heuristic):
		val_ = -9999999999999
		ma_ =	(0,0)
		index = 0
		for i in list_of_tuple_and_heuristic:
			if i[1][2]>val_:
				val_ = i[1][2]
				ma_ = i[1][1]
				index = i[0]
		return index,ma_,val_



	def get_min(self,list_of_tuple_and_heuristic): 
		val_ = 99999999999999
		mi_ = (0,0)
		index = 0
		for i in list_of_tuple_and_heuristic:
			if i[1][2]<val_:
				val_ = i[1][2]
				mi_ = i[1][1]
				index = i[0]
		return index,mi_,val_



	def Heuristic(self,temp_board_,temp_block_,tupleofcell,flag_):
		if flag_ == 0:
			player = 'x'
			opponent = 'o'
		else:
			player ='o'
			opponent = 'x'

		Winning_triads = [
			( 0, 1, 2 ),
			( 3, 4, 5 ),
			( 6, 7, 8 ),
			( 0, 3, 6 ),
			( 1, 4, 7 ),
			( 2, 5, 8 ),
			( 0, 4, 8 ),
			( 2, 4, 6 )
		]; 
		Heuristic_Array = [
			( 0, -10, -100, -1000 ),
			( 10, 0, 0, 0 ),
			( 100, 0, 0, 0 ),
			( 1000, 0, 0, 0 )
		];
		heuristic_value = 0
		for i in range(9):
			tx = i/3
			ty = i%3
			off_x = tx*3
			off_y = ty*3
			for j in range(8):
				opponent_count = 0
				player_count = 0
				for k in range(3):
					x = Winning_triads[j][k]
					r_add = x/3
					c_add = x%3
					if(temp_board_[off_x+r_add][off_y+c_add] == player):
						player_count+=1
					elif(temp_board_[off_x+r_add][off_y+c_add]==opponent):
						opponent_count+=1
				heuristic_value = heuristic_value + Heuristic_Array[player_count][opponent_count]
		for i in range(8):
			opponent_count = 0
			player_count = 0
			for j in range(3):
				if temp_block_[Winning_triads[i][j]] == player:
					player_count +=1
				elif temp_block_[Winning_triads[i][j]] == opponent:
					opponent_count+=1
			heuristic_value = heuristic_value + 5*Heuristic_Array[player_count][opponent_count]			
		return heuristic_value

		




	def get_empty_out_ofx(self,gameb, blal,block_stat):
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
			    
	def move(self,temp_board,temp_block,old_move,flag):
		if old_move == (-1,-1):
			return (4,4)
		old_move_ = old_move
		temp_board_ = self.copy_2DList(temp_board)
		temp_block_ = self.copy_1DList(temp_block)
		if flag=='x':
			flag_ = 0
		else:
			flag_ = 1
		myplayer = flag_
		cells = self.cells_allowed(old_move_,temp_board_,temp_block_)
		zzz = self.best_possible_move(old_move_,temp_board_,temp_block_,cells,flag_,0,myplayer)
		return cells[zzz[0]]
