import pygame , sys

import multiprocessing 
from pygame.locals import *
import math
from random import randint

class Car():
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.position = 2
		self.rad = 10
		self.color =  (0,0,255) # blue
		self.lane = 3
		w = width//self.lane
		t = width//(2*self.lane)

		self.x_pos={}
		for i in range(self.lane):
			self.x_pos[i+1]=t+(i*w)

		self.y_pos = height-100
	def left(self):
		# if self.position!=1:
		# 	self.position-=1
		self.position=1
	def right(self):
		# if self.position!=self.lane:
		# 	self.position+=1
		self.position=3

	def middle(self):
		# if self.position!=self.lane:
		self.position=2
	def draw(self,pygame,DISPLAYSURF):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x_pos[self.position]),int(self.y_pos)), self.rad, 0)


def init_car(width,height):
	print(101)
	global car
	car = Car(width,height)

# width = 300
# height = 600
# car = Car(width,height)

