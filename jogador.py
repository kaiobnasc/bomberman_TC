from __future__ import print_function
import signal,copy,sys,time
from random import randint
from posicionamento import * 
from tabuleiro import *

jogadorPos = [1,1]
score = 0
lives = 3

class Jogador(Posicionamento):

	def desenhaJogador(self,x,y):
		if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="/"):
				gameArray[2*x+1][4*y+1] = "P" 
				gameArray[2*x+1][4*y+2] = "P"
				gameArray[2*x+1][4*y+3] = "P"
				gameArray[2*x+1][4*y+4] = "P"
				gameArray[2*x+2][4*y+1] = "P" 
				gameArray[2*x+2][4*y+2] = "P"
				gameArray[2*x+2][4*y+3] = "P"
				gameArray[2*x+2][4*y+4] = "P"
		return

	def checarPosicao(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="/"):
			return -1
		return 1

	def checarInimigo(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="I"):
			return -1
		return 1	

	def atualizaJogador(self):
		x = jogadorPos[0]
		y = jogadorPos[1]
		self.desenhaJogador(x,y)
		if(lives <= 0):
			print("Game Over")
			print("Pontuação:",score)
			sys.exit(1)

		print("Pontuação:",score,"\t\t\t\t\t\t","Vidas restantes:",lives)
		return		

	def jogadorInit(self):
		jogadorPos[0] = 1
		jogadorPos[1] = 1
		x = jogadorPos[0]
		y = jogadorPos[1]
		return

	def desce(self):
		x = jogadorPos[0]
		y = jogadorPos[1]
		if(self.checarInimigo(x+1,y)>0):
			if(self.checarPos(x+1,y)>0):
				jogadorPos[0] += 1
				self.desenhaJogador(jogadorPos[0],jogadorPos[1])
		else:
			self.atualizaVida()
		return

	def sobe(self):
		x = jogadorPos[0]
		y = jogadorPos[1]	
		if(self.checarInimigo(x-1,y)>0):
			if(self.checarPos(x-1,y)>0):
				jogadorPos[0] -= 1
				self.desenhaJogador(jogadorPos[0],jogadorPos[1])
		else:
			self.atualizaVida()	
		return

	def esquerda(self):
		x = jogadorPos[0]
		y = jogadorPos[1]		
		if(self.checarInimigo(x,y-1)>0):
			if(self.checarPos(x,y-1)>0):
				jogadorPos[1] -= 1
				self.desenhaJogador(jogadorPos[0], jogadorPos[1])
		else:
			self.atualizaVida()
		return

	def direita(self):
		x = jogadorPos[0]
		y = jogadorPos[1]		
		if(self.checarInimigo(x,y+1)>0):
			if(self.checarPos(x,y+1)>0):
				jogadorPos[1] += 1
				self.desenhaJogador(jogadorPos[0],jogadorPos[1])
		else:
			self.atualizaVida()
		return

	def atualizaScore(self, update):
		global score
		score += update
		return 

	def atualizaVida(self):
		global lives
		lives -= 1
		jogadorPos[0] = 1
		jogadorPos[1] = 1
		return
