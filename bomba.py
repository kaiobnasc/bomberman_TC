from __future__ import print_function
import signal,copy,sys,time
from random import randint
from tabuleiro import *
from jogador import *
from inimigo import *
from parede import *

bomPos = [0,0,-1]
jg = Jogador()
ini = Inimigo()

class Bomba():

	def desenhaBomba(self):
		x = bomPos[0]
		y = bomPos[1]
		

		if(bomPos[2] > -1):
			for i in range(1,3):
					for j in range(1,5):
						bomba.append([2*x+i,4*y+j])

			gameArray[2*x+1][4*y+1] = bomPos[2]
			gameArray[2*x+1][4*y+2] = bomPos[2]
			gameArray[2*x+1][4*y+3] = bomPos[2]
			gameArray[2*x+1][4*y+4] = bomPos[2]
			gameArray[2*x+2][4*y+1] = bomPos[2]
			gameArray[2*x+2][4*y+2] = bomPos[2]
			gameArray[2*x+2][4*y+3] = bomPos[2]
			gameArray[2*x+2][4*y+4] = bomPos[2]
		
		bomPos[2] -= 1
		if(bomPos[2] == -1):
			self.explosao()
		return

	def desenhaExplosao(self,x,y):

		gameArray[2*x+1][4*y+1] = "e"
		gameArray[2*x+1][4*y+2] = "e"
		gameArray[2*x+1][4*y+3] = "e"
		gameArray[2*x+1][4*y+4] = "e"
		gameArray[2*x+2][4*y+1] = "e"
		gameArray[2*x+2][4*y+2] = "e"
		gameArray[2*x+2][4*y+3] = "e"
		gameArray[2*x+2][4*y+4] = "e"		
		return

	def depoisExplosao(self,x,y):

		if(x == jogadorPos[0] and y == jogadorPos[1]):
			jg.updateLife()

		if(inimigoNum>0 and [x,y] in inimigoPos):
			inimigoPos.remove([x,y])
			jg.atualizaScore(100)
			ini.atualizaNum(-1)

		if([x,y] in paredePos):
			paredePos.remove([x,y])
			jg.atualizaScore(20)	
			
		return

	def checarPos(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" ):
			return -1
		return 1


	def explosao(self):
		x = bomPos[0]
		y = bomPos[1]
		self.desenhaExplosao(x,y)
		self.depoisExplosao(x,y)

		if(self.checkPos(x-1,y)>0):
			self.desenhaExplosao(x-1,y)
			self.depoisExplosao(x-1,y)

		if(self.checkPos(x+1,y)>0):
			self.desenhaExplosao(x+1,y)
			self.depoisExplosao(x+1,y)

		if(self.checkPos(x,y-1)>0):
			self.desenhaExplosao(x,y-1)
			self.depoisExplosao(x,y-1)

		if(self.checkPos(x,y+1)>0):
			self.desenhaExplosao(x,y+1)
			self.depoisExplosao(x,y+1)
		return


