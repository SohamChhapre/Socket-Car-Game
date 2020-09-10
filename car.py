import pygame , sys

import multiprocessing 
from pygame.locals import *
import math
from random import randint

class Car():
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.position = 1
		self.rad = 10
		self.color =  (255,0,0) # red
		w = width//3
		t = width//6
		self.x_pos = {1: t ,2: t+w,3:2*w+t}
		self.y_pos = height-100
	def left(self,x):
		if self.position!=1:
			self.position=x
		for i in range(1000):pass
	def right(self,x):
		# if self.position==1:
		# 	self.position+=1
		# if self.position==2:
		# 	self.position+=1
		if self.position!=3:
			self.position=x
		for i in range(1000):pass
	def draw(self,pygame,DISPLAYSURF):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x_pos[self.position]),int(self.y_pos)), self.rad, 0)


def init_car(width,height):
	print(101)
	global car
	car = Car(width,height)

# width = 300
# height = 600
# car = Car(width,height)

