import random
import sys
import signal

grid = []
stat = []
toss = random.randint(0,1)
count = toss
last_move_i = 0
last_move_j = 0
flag_init = 0
flag_firstmove = 0
symbol_for_human = 'X'
symbol_for_bot = 'O'
class Player97:
	def __init__(self):
		pass
	def move(self,current_board_game, board_stat, move_by_opponent, flag):
						

		
Player97 mybot
def give_symbols():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	flag_init = 1
	if(toss == 1):
		symbol_for_human = 'X'
		symbol_for_bot = 'O'
	elif(toss == 0):
		symbol_for_human = 'O'
		symbol_for_bot = 'X'
def make_grid():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	for i in xrange(0,9):
		stat.append(0)
		row = ['-']*9
		grid.append(row)
def print_grid():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	print '=========== Game Board ==========='
	for i in range(9):
		if i > 0 and i % 3 == 0:
			print
		for j in range(9):
			if j > 0 and j % 3 == 0:
				print " " + grid[i][j],
			else:
				print grid[i][j],

		print
	print "=================================="
def check_move(a,b):
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	range_a = range((last_move_i%3)*3,(last_move_i%3)*3 + 3)
	range_b = range((last_move_j%3)*3,(last_move_j%3)*3 + 3)
	last_mod_i = last_move_i%3
	last_mod_j = last_move_j%3
	if(((last_mod_i + last_mod_j)%2 == 0) and ((last_mod_i != 1) and (last_mod_j != 1))):
		if(last_mod_i == 0):
			range_mod_a = range(0,6)
		elif(last_mod_i == 2):
			range_mod_a = range(3,9)
		if(last_mod_j == 0):
			range_mod_b = range(0,6)
		elif(last_mod_j == 2):
			range_mod_b = range(3,9)
		range_check_a = range(3,6)
		range_check_b = range(3,6)
		if((a in range_mod_a)and(b in range_mod_b)):
			if( a in range_check_a and b not in range_check_b):
				last_move_i = a
				last_move_j = b
				return 1
			elif(b in range_check_b and a not in range_check_a):
				last_move_i = a
				last_move_j = b
				return 1
			else:
				return 0
		else:
			return 0
	else:
		if((a in range_a) and (b in range_b)):
			last_move_j = b
			last_move_i = a
			return 1
		else:
			return 0
def move_by_human():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	print '=====ENTER MOVE====='
	a = int(raw_input())
	b = int(raw_input())
	if(count == 1):
		count = count + 1
		print 'MOVE IS VALID'
		grid[a][b] = symbol_for_human
		last_move_i = a
		last_move_j = b
		print_grid()
	elif(count != 1):
		check = check_move(a,b)
		if(check == 1):
			print 'MOVE IS VALID'
			grid[a][b] = symbol_for_human
			last_move_i = a
			last_move_j = b
			print_grid()
		else:
			print 'MOVE IS INVALID'
			sys.exit()
def make_move():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	if(count%2!=0):
		move_by_human()
	else:
		mybot.move(grid, stat, previous_move, symbol_for_bot)
def main():
	global count
	global grid
	global last_move_i
	global last_move_j
	global toss
	global count
	global flag_init
	global flag_firstmove
	global symbol_for_human
	global symbol_for_bot
	global flag_init
	if(flag_init == 0):
		give_symbols()
	make_grid()
	print_grid()
	while(1):
		make_move()
		
main()