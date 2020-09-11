import pygame , sys

import threading

import server
from pygame.locals import *
import math
from random import randint
import car 
import time


class Stone():
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.y_speed = 0.1
		self.init_speed = 0.1
		self.rad = 10
		self.color_dict = {0: (255,0,0),1:(0,255,0) }# red , green

		self.lane = 3
		self.position = randint(1,self.lane)
		w = width//self.lane
		t = width//(2*self.lane)

		self.x_pos={}
		for i in range(self.lane):
			self.x_pos[i+1]=t+(i*w)
		self.y_pos = 10
		self.count = 0
		self.good  = randint(0,1)

	def restart(self):
		self.y_pos = -100
		self.position = randint(1,self.lane)
		self.good  = randint(0,1)
		self.count+=1

	def update(self):
		self.y_pos += self.y_speed
		# if self.count==5:
		self.y_speed = self.init_speed + score.score*0.001
		self.count=0

		if self.height-self.y_pos<5:
			# print("restart")
			self.y_pos = 5
			self.position = randint(1,2)
			self.good  = randint(0,1)
			# self.count+=1

	def draw(self,pygame,DISPLAYSURF):
		pygame.draw.circle(DISPLAYSURF, self.color_dict[self.good], (int(self.x_pos[self.position]),int(self.y_pos)), self.rad, 0)



class Score:
	def __init__(self,pygame,width,height):
		self.width = width
		self.height = height
		self.score = 0
		self.color = (0,0,0)
		self.back = (255,255,255)
		self.fontObj = pygame.font.Font('freesansbold.ttf', 20)
		self.textSurfaceObj = self.fontObj.render(str(self.score), True, self.color, self.back)
		self.textRectObj = self.textSurfaceObj.get_rect()
		self.textRectObj.center = (self.width//2, 20)
		
	def update(self,a):

		self.score+=a
		self.textSurfaceObj = self.fontObj.render(str(self.score), True, self.color, self.back)
		self.textRectObj = self.textSurfaceObj.get_rect()
		self.textRectObj.center = (self.width//2, 20)

	def text(self,t):
		self.textSurfaceObj = self.fontObj.render(t, True, self.color, self.back)
		self.textRectObj = self.textSurfaceObj.get_rect()
		self.textRectObj.center = (self.width//2, 20)

	def draw(self,pygame,DISPLAYSURF):
		# DISPLAYSURF.fill(self.back)
		DISPLAYSURF.blit(self.textSurfaceObj, self.textRectObj)



def game():


	time.sleep(2)
	score.text("3")
	score.draw(pygame,DISPLAYSURF)
	pygame.display.update()
	time.sleep(1)
	score.text("2")
	score.draw(pygame,DISPLAYSURF)
	pygame.display.update()
	time.sleep(1)
	score.text("1")
	score.draw(pygame,DISPLAYSURF)
	pygame.display.update()
	score.text("GAME STARTS")
	score.draw(pygame,DISPLAYSURF)
	pygame.display.update()

	stones = []
	stone_count = 0
	# for i in range(level):
	# 	stones.append(Stone(width,height,i/level))



	while True:
		DISPLAYSURF.fill(WHITE)
		car.car.draw(pygame,DISPLAYSURF)
		if stone_count<level and (not(stones) or stones[-1].y_pos>(height/level)):
			stones.append(Stone(width,height))
			stone_count+=1
		for s in stones:
			s.update()
			s.draw(pygame,DISPLAYSURF)



		score.draw(pygame,DISPLAYSURF)
		endgame=False
		for stone in stones:
			if car.car.position == stone.position and abs(car.car.y_pos-stone.y_pos)<1:
				if stone.good==0:
					score.text(str(score.score)+"  GAME ENDS")
					score.draw(pygame,DISPLAYSURF)
					pygame.display.update()
					time.sleep(1)
					# endgame=True
					break
				else:
					stone.restart()
					score.update(1)
					score.draw(pygame,DISPLAYSURF)

		if endgame==True:
			break
		pygame.display.update()

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
	score = Score(pygame,width,height)


	t1 = threading.Thread(target=game, args=()) 
	t2 = threading.Thread(target=server.start, args=(pygame,DISPLAYSURF,))

	t1.start()
	t2.start() 


	t1.join()
	t2.join()