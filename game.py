import pygame , sys

import threading

import server
from pygame.locals import *
import math
from random import randint
import car 
import time


class Stone():
	def __init__(self,width,height,start):
		self.width = width
		self.height = height
		self.position = randint(1,3)
		self.y_speed = 0.1
		self.rad = 10
		self.color =  (0,255,0) # green
		w = width//3
		t = width//6
		# z=width//
		self.x_pos = {1: t ,2: t+w,3: t+2*w}
		self.y_pos = height*start
		self.count = 0

	def update(self):
		self.y_pos += self.y_speed
		if self.count==10:
			self.y_speed+=0.005
			self.count=0

		if self.height-self.y_pos<5:
			print("restart")
			self.y_pos = 5
			self.position = randint(1,3)
			self.count+=1





	def draw(self,pygame,DISPLAYSURF):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x_pos[self.position]),int(self.y_pos)), self.rad, 0)



def game():

	time.sleep(5)
	print("GAME STARTS")
	stones = []
	for i in range(level):
		stones.append(Stone(width,height,i/level))

	two=False

	while True:
		DISPLAYSURF.fill(WHITE)
		car.car.draw(pygame,DISPLAYSURF)
		for s in stones:
			s.update()
			s.draw(pygame,DISPLAYSURF)



		pygame.display.update()
		endgame=False
		for stone in stones:
			if car.car.position == stone.position and abs(car.car.y_pos-stone.y_pos)<1:
				print("GAME END")
				endgame=True
				break
		if endgame==True:
			break

if __name__ == "__main__": 

	level = 4

	print(1)
	pygame.init()

	width = 300
	height = 600
	DISPLAYSURF = pygame.display.set_mode((width,height))
	pygame.display.set_caption('helloworls')

	GREEN = (  0, 255,   0)
	RED = (255,0,0)
	WHITE = (0,0,0)

	car.init_car(width,height)
	

	t1 = threading.Thread(target=game, args=()) 
	t2 = threading.Thread(target=server.start, args=(pygame,DISPLAYSURF,))

	t1.start()
	t2.start() 


	t1.join()
	t2.join()