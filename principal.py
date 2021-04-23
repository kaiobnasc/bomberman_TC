from __future__ import print_function
import signal,copy,sys,time
from random import randint
import os
from getchunix import *
from iniciajogo import *
from posicionamento import *
from jogador import *
from bomba import *
from parede import *

getch = GetchUnix()

def input_char(timeout=1): #pega os dados de entrada do jogador
        text = getch()
        return text

g=IniciaJogo()
jg = Jogador()
bom = Bomba()
pa = Parede()
jg.jogadorInit()
ini.inimigoInit()
pa.paredeInit()
level = 1

while(1):
	os.system("tput reset")
	inimigoNum = ini.inNum()
	if(inimigoNum == 0):
	
		print ("Fim de jogo! Você venceu todos inimigos!");
		sys.exit(0)
		
	g.printboard()		
	teclado = input_char()	
	if(teclado == 'q'):
		sys.exit(0)		
	elif(teclado == 's'):
		jg.desce()	
	elif(teclado == 'w'):
		jg.sobe()		
	elif(teclado == 'a'):
		jg.esquerda()	
	elif(teclado == 'd'):
		jg.direita()	
	elif(teclado == 'b'):	
		if(bomPos[2] == -1):
			bomPos[0] = jogadorPos[0]
			bomPos[1] = jogadorPos[1]
			bomPos[2] = 3
			bom.desenhaBomba()
