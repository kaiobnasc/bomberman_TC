from __future__ import print_function
import signal,copy,sys,time
from random import randint
from posicionamento import * 
from tabuleiro import *
from jogador import *

inimigoPos = []
inimigoNum = 10
jg = Jogador()

class Inimigo(Posicionamento):

	def desenhaInimigo(self): #self referencia o proprio objeto (instância)
		x = len(inimigoPos)
		for i in range(x):
			x = inimigoPos[i][0]
			y = inimigoPos[i][1]
			if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="/"):
					gameArray[2*x+1][4*y+1] = "I" 
					gameArray[2*x+1][4*y+2] = "I"
					gameArray[2*x+1][4*y+3] = "I"
					gameArray[2*x+1][4*y+4] = "I"
					gameArray[2*x+2][4*y+1] = "I" 
					gameArray[2*x+2][4*y+2] = "I"
					gameArray[2*x+2][4*y+3] = "I"
					gameArray[2*x+2][4*y+4] = "I"
		return

	def checarPos(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+2][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="/" or gameArray[2*x+2][4*y+1]=="/"):
			return -1
		return 1	

	def inimigoInit(self):
		for i in range(inimigoNum):
			x = randint(1,17)
			y = randint(1,17)	
			inimigoPos.append([x,y]) #append adiciona um elemento à lista
			print(inimigoPos[i][0],inimigoPos[i][1])
		self.desenhaInimigo()
		return

	def matarJogador(self,x,y):
		jg.atualizaVida()
		return

	def atualizaPos(self):
		x = len(inimigoPos)
		for i in range(x):
			x = inimigoPos[i][0]
			y = inimigoPos[i][1]
			if(x == jogadorPos[0] and y == jogadorPos[1]):
				self.matarJogador(x,y)
			if(x<18 and y<18):
				dir = randint(1,4)
				if(dir == 1):
					if(self.checarPos(x-1,y)>0):
						
						if(x-1 == jogadorPos[0] and y == jogadorPos[1]):
							self.matarJogador(x-1,y)
						inimigoPos[i][0] -= 1
						
				elif(dir == 2):
					if(self.checarPos(x+1,y)>0):
						
						if(x+1 == jogadorPos[0] and y == jogadorPos[1]):
							self.matarJogador(x+1,y)
						inimigoPos[i][0] += 1
						
				elif(dir == 3):
					if(self.checarPos(x,y-1)>0):
						
						if(x == jogadorPos[0] and y-1 == jogadorPos[1]):
							self.matarJogador(x,y-1)
						inimigoPos[i][1] -= 1
						
				elif(dir == 4):
					if(self.checarPos(x,y+1)>0):
						
						if(x == jogadorPos[0] and y+1 == jogadorPos[1]):
							self.matarJogador(x,y+1)
						inimigoPos[i][1] += 1
					
		self.desenhaInimigo()
		return

	def atualizaNum(self,val):
		global inimigoNum
		inimigoNum += val
		return

	def iniNum(self):
		return inimigoNum
