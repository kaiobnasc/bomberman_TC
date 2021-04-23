from __future__ import print_function
import signal,copy,sys,time
from random import randint

class Posicionamento():

	def verificaPos(self,x,y):

		if(x<4 or x>35 or y<2 or y>76):
			return -1


