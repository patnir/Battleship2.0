'''
	@ AUTHOR NAME HERE
	@ Starter Code By Harris Christiansen (Harris@purduecs.com)
	2016-01-28
	For: Purdue Hackers - Battleship
	Battleship Client
'''

import sys
import socket
import time
import random

API_KEY = "463003004" ########## PUT YOUR API KEY HERE ##########

GAME_SERVER = "battleshipgs.purduehackers.com"

##############################  PUT YOUR CODE HERE ##############################

letters = ['A','B','C','D','E','F','G','H']
grid = [[-1 for x in range(8)] for x in range(8)] # Fill Grid With -1s

def placeShips(opponentID):
	global grid
	# Fill Grid With -1s
	grid = [[-1 for x in range(8)] for x in range(8)] # Fill Grid With -1s

	# Place Ships
	#i = 0#random.randint(0, 5)
	#print i

	'''if i == 0:
		placeDestroyer("A0","A1") # Ship Length = 2
		placeSubmarine("B0","B2") # Ship Length = 3
		placeCruiser("C0","C2") # Ship Length = 3
		placeBattleship("D0","D3") # Ship Length = 4
		placeCarrier("E0","E4") # Ship Length = 5
		placeDestroyer("A0","B0") # Ship Length = 2
		placeSubmarine("G3","G5") # Ship Length = 3
		placeCruiser("C0","C2") # Ship Length = 3
		placeBattleship("E7","H7") # Ship Length = 4
		placeCarrier("H0","H4") # Ship Length = 5

	elif i == 1:
		placeDestroyer("G1","G2") # Ship Length = 2
		placeSubmarine("E0","E2") # Ship Length = 3
		placeCruiser("F3","F5") # Ship Length = 3
		placeBattleship("H4","H7") # Ship Length = 4
		placeCarrier("A7","E7") # Ship Length = 5

	elif i == 2:
		placeDestroyer("A7","B7") # Ship Length = 2
		placeSubmarine("C6","E6") # Ship Length = 3
		placeCruiser("F7","H7") # Ship Length = 3
		placeBattleship("H2","H5") # Ship Length = 4
		placeCarrier("F1","F5") # Ship Length = 5

	elif i == 3:
		placeDestroyer("C5","D5") # Ship Length = 2
		placeSubmarine("E4","E6") # Ship Length = 3
		placeCruiser("F6","H6") # Ship Length = 3
		placeBattleship("G2","G5") # Ship Length = 4
		placeCarrier("H1","C1") # Ship Length = 5

	elif i == 4:
		placeDestroyer("F0","G0") # Ship Length = 2
		placeSubmarine("D0","D2") # Ship Length = 3
		placeCruiser("A3","C3") # Ship Length = 3
		placeBattleship("F4","F7") # Ship Length = 4
		placeCarrier("H2","H6") # Ship LengF0th = 5

	else:
		placeDestroyer("D4","E4") # Ship Length = 2
		placeSubmarine("B7","D7") # Ship Length = 3
		placeCruiser("C1","C3") # Ship Length = 3
		placeBattleship("F0","F3") # Ship Length = 4
		placeCarrier("H3","H7") # Ship Length = 5'''

	placeDestroyer("A0","A1") # Ship Length = 2
	placeSubmarine("B0","B2") # Ship Length = 3
	placeCruiser("C0","C2") # Ship Length = 3
	placeBattleship("D0","D3") # Ship Length = 4
	placeCarrier("E0","E4") # Ship Length = 5

class Node():
	def __init__(self, x, y):
		self.next = None
		self.x = x
		self.y = y
		self.hit = 0
		self.visited = 0
		self.next = None

	def checkOver(self):
		if self.x >= 8 or self.y < 0 or self.x < 0 or self.y >= 8:
			return True
		return False

class Stack():
	def __init__(self):
		self.head = None
		self.total = 0

	def push(self, node):
		if self.total == 0:
			self.head = node
			self.total += 1
			return
		node.next = self.head
		self.head = node
		self.total += 1

	def pop(self):
		if self.total == 0:
			print "cannot remove from empty stack"
			return

		toRet = self.head
		self.head = self.head.next
		toRet.next = None
		self.total -= 1
		return toRet

prob = [None] * 8
	for i in range(len(prob)):
	    prob[i] = [None] * 8
	    for j in range(len(prob[i])):
	        s = Node(i, j)
	        prob[i][j] = s

s = Stack()

def makeMove():
	global grid
    global prob
	global s

	"""for x in range(7, -1, -1): # Loop Till Find Square that has not been hit
		for y in range(7,-1, -1):

			if grid[x][y] == -1:
				print y, str(y)
				wasHitSunkOrMiss = placeMove(letters[x]+str(y)) # placeMove(LetterNumber) - Example: placeMove(D5)
				prob[x][y].visted = 1
				if(wasHitSunkOrMiss == "Hit" or wasHitSunkOrMiss == "Sunk"):
					grid[x][y] = 1
					prob[x][y].hit = 1
				else:
					grid[x][y] = 0"""

	move = 0

	s = Stack()

	'''for x in range(0,8): # Loop Till Find Square that has not been hit
		for y in range(0,8):
			if grid[x][y] == -1:
				wasHitSunkOrMiss = placeMove(letters[x]+str(y)) # placeMove(LetterNumber) - Example: placeMove(D5)
				if(wasHitSunkOrMiss == "Hit" or wasHitSunkOrMiss == "Sunk"):
					grid[x][y] = 1
				else:
					grid[x][y] = 0

				return'''

	while move < 64:
		print move
		randx = 0#random.randint(0, 7)
		randy = move % 8#random.randint(0, 7)

		print randx, randy

		'''while prob[randx][randy].visited != 0:
			randx = random.randint(0, 7)
			randy = random.randint(0, 7)
			print randx, randy'''

		x = randx
		y = randy

		print x, y

		wasHitSunkOrMiss = placeMove(letters[x]+str(y))
		move += 1

		prob[x][y].visited = 1;

		if(wasHitSunkOrMiss == "Hit" or wasHitSunkOrMiss == "Sunk"):
			print "hit"
			grid[x][y] = 1
			print prob[x][y].hit
			prob[x][y].hit = 1

		else:
			print "print no hit"
			grid[x][y] = 0

		'''top = Node(x, y + 1)
					dow = Node(x, y - 1)
					lef = Node(x - 1, y)
					rig = Node(x + 1, y)

					if top.checkOver() == False:
						s.push(top)
					if dow.checkOver() == False:
						s.push(dow)
					if lef.checkOver() == False:
						s.push(lef)
					if rig.checkOver() == False:
						s.push(rig)

					while s.total != 0:
						print "tjis is dick"
						curr = s.pop()
						if curr.visited != 0:
							print "second if"
							nX = curr.x
							nY = curr.y
							wasHitSunkOrMiss = placeMove(letters[nX]+str(nY))
							prob[nX][nY].visited = 1;
							move += 1

							if(wasHitSunkOrMiss == "Hit" or wasHitSunkOrMiss == "Sunk"):
								print "hit2"
								grid[nX][nY] = 1
								prob[nX][nY].hit = 1
								topN = Node(nX, nY + 1)
								dowN = Node(nX, nY - 1)
								lefN = Node(nX - 1, nY)
								rigN = Node(nX + 1, nY)
								if topN.checkOver() == False:
									s.push(topN)
								if dowN.checkOver() == False:
									s.push(dowN)
								if lefN.checkOver() == False:
									s.push(lefN)
								if rigN.checkOver() == False:
									s.push(rigN)
							else:
								print "no hit 2"
								grid[nX][nY] = 0'''
	
	return

############################## ^^^^^ PUT YOUR CODE ABOVE HERE ^^^^^ ##############################

def sendMsg(msg):
	global s
	try:
		s.send(msg)
	except:
		s = None

def connectToServer():
	global s
	invalidKey = False
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((GAME_SERVER, 23345))

		sendMsg(API_KEY)
		data = s.recv(1024)

		if("False" in data):
			s = None
			print "Invalid API_KEY"
			invalidKey = True
	except:
		s = None

	if invalidKey:
		sys.exit()


destroyer=submarine=cruiser=battleship=carrier=("A0","A0")
dataPassthrough = None

def gameMain():
	global s, dataPassthrough, moveMade
	while True:
		if(dataPassthrough == None):
			if s == None:
				return
			data = s.recv(1024)
		else:
			data = dataPassthrough
			dataPassthrough = None

		if not data:
			s.close()
			return
		
		if "Welcome" in data: # "Welcome To Battleship! You Are Playing:xxxx"
			welcomeMsg = data.split(":")
			placeShips(welcomeMsg[1])
			if "Destroyer" in data: # Only Place Can Receive Double Message, Pass Through
				dataPassthrough = "Destroyer(2):"
		elif "Destroyer" in data: # Destroyer(2)
			sendMsg(destroyer[0])
			sendMsg(destroyer[1])
		elif "Submarine" in data: # Submarine(3)
			sendMsg(submarine[0])
			sendMsg(submarine[1])
		elif "Cruiser" in data: # Cruiser(3)
			sendMsg(cruiser[0])
			sendMsg(cruiser[1])
		elif "Battleship" in data: # Battleship (4)
			sendMsg(battleship[0])
			sendMsg(battleship[1])
		elif "Carrier" in data: # Carrier(3)
			sendMsg(carrier[0])
			sendMsg(carrier[1])
		elif "Enter" in data: # Enter Coordinates
			moveMade = False
			makeMove()
		elif "Error" in data: # Error: xxx
			print("Received Error: "+data)
			sys.exit()
		elif "Hit" in data or "Miss" in data or "Sunk" in data:
			print("Error: Please Make Only 1 Move Per Turn.")
			sys.exit()
		elif "Die" in data:
			print("Error: Your client was disconnected using the Game Viewer.")
			sys.exit()
		else:
			print("Received Unknown Response: "+data)
			sys.exit()


def placeDestroyer(startPos, endPos):
	global destroyer
	destroyer = (startPos.upper(), endPos.upper())
def placeSubmarine(startPos, endPos):
	global submarine
	submarine = (startPos.upper(), endPos.upper())
def placeCruiser(startPos, endPos):
	global cruiser
	cruiser = (startPos.upper(), endPos.upper())
def placeBattleship(startPos, endPos):
	global battleship
	battleship = (startPos.upper(), endPos.upper())
def placeCarrier(startPos, endPos):
	global carrier
	carrier = (startPos.upper(), endPos.upper())

def placeMove(pos):
	global dataPassthrough, moveMade
	if moveMade: # Only Make 1 Move Per Turn
		print("Error: Your client was disconnected using the GameViewer")
		sys.exit()

	moveMade = True
	sendMsg(pos)
	data = s.recv(1024)
	if "Hit" in data:
		return "Hit"
	elif "Sunk" in data:
		return "Sunk"
	elif "Miss" in data:
		return "Miss"
	else:
		dataPassthrough = data
		return "Miss"

while True:
	connectToServer()
	if s != None:
		try:
			gameMain()
		except socket.error, msg:
			None
	time.sleep(1)
