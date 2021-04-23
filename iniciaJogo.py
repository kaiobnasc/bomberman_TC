from __future__ import print_function
import signal,copy,sys,time
from random import randint
from termcolor import colored
from tabuleiro import *
from parede import *
from posicionamento import *
from jogador import *
from inimigo import *
from bomba import *

tab = Tabuleiro()
pa = Parede()
jg = Jogador()
ini = Inimigo()
bom = Bomba()

class IniciaJogo():

	def __init__(self):
		self.cur_time = time.time()


	def printboard(self):

		jg.updatePlayer()

		run_time = time.time() - self.cur_time
		if(run_time > 1):
			ini.atualizaPos()
			self.cur_time = time.time()
		else:
			ini.desenhaInimigo()

		
		if(run_time > 1 and bomPos[2] >= 0):
			bom.desenhaBomba()
		
		for i in range(1,39):
			for j in range(1,77):
				if(gameArray[i][j]=="X"):
					print(colored(gameArray[i][j],"blue"),end="")
				elif(gameArray[i][j]=="I"):
					print(colored(gameArray[i][j],"red"),end="")
				elif(gameArray[i][j]=="/"):
					print(colored(gameArray[i][j],"green"),end="")
				else:
					print(gameArray[i][j],end="")
			print("\n",end="")
		print("Aperte 'q' para sair do jogo...	")	

		return

