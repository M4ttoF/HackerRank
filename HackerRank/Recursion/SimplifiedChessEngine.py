




games=input()
pos={'A':0,'B':1,'C':2,'D':3}
WHITE=0
BLACK=1

class Piece:
	x=0
	y=0
	moves=[]
	name=''
	color=-1
	def __init__(self, x,y,name,color):
		self.x=x
		self.y=y
		self.name=name
		self.color=color
	def findMoves(self):
		if self.name=='R' or self.name=='Q':
			#check moves to right
			for i in range(self.x+1,4):
				if board[i][self.y]==None:
					self.moves.append([i,self.y])
			#check moves to left
			for i in range(self.x+1):
				if board[self.x-i][self.y]==None:
					self.moves.append([i,self.y])
			#check moves up
			for i in range(self.y+1,4):
				if board[self.x][i]==None:
					self.moves.append([self.x,i])
			#check moves to down
			for i in range(self.y+1):
				if board[self.x][self.y-i]==None:
					self.moves.append([self.x,i])
			print(self.moves)

rook=Piece(0,0,'R',0)
board=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
rook.findMoves()

'''
for i in range(0,games):
    infoLine=input()
    info=infoLine.split()
    wPieces=[]
    bPieces=[]
    board=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    
    for j in int(info[0]):
        #adding white pieces
        pce=input()
        pce=pieces.split()
        pce=Piece()
        wPieces.append(Piece(pos[pce[1]],int(pce[2]),pce[0],0))
'''