from __future__ import print_function
import signal,copy,sys,time
from random import randint
from tabuleiro import *
paredePos = []

class Parede(Tabuleiro):


	def paredeInit(self):
		for i in range(20):
			x = randint(1,17)
			y = randint(1,17)	
			paredePos.append([x,y])
		return

	def desenhaParede(self):
		size = len(paredePos)
		for i in range(size):
	
			x = paredePos[i][0]
			y = paredePos[i][1]
			
			if(x*y!=1 and (gameArray[2*x+1][4*y+1]!="X" )):
				gameArray[2*x+1][4*y+1] = "/" 
				gameArray[2*x+1][4*y+2] = "/"
				gameArray[2*x+1][4*y+3] = "/"
				gameArray[2*x+1][4*y+4] = "/"
				gameArray[2*x+2][4*y+1] = "/" 
				gameArray[2*x+2][4*y+2] = "/"
				gameArray[2*x+2][4*y+3] = "/"
				gameArray[2*x+2][4*y+4] = "/"


		return
