import pygame , sys

import multiprocessing 
from pygame.locals import *
import math
from random import randint
from math import pi, cos, sin

class Car():
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.position = 2
		self.rad = 50
		self.color =  (255,255,0) # yellow
		self.lane = 3
		w = width//self.lane
		t = width//(2*self.lane)

		self.x_pos={}
		for i in range(self.lane):
			self.x_pos[i+1]=t+(i*w)

		self.y_pos = height-100
		self.theta = pi/6
		self.theta_sigh = -pi/36

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
		# pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x_pos[self.position]),int(self.y_pos)), self.rad, 0)
		x_p , y_p = int(self.x_pos[self.position]),int(self.y_pos)
		rect = pygame.Rect((x_p - 25, y_p-25), (50, 50))
		s_ang = (pi/2) + self.theta
		e_ang = (pi/2) - self.theta
		pygame.draw.arc(DISPLAYSURF, self.color, rect ,s_ang , e_ang , 24)

		self.theta += self.theta_sigh
		if self.theta< pi/36 or self.theta>=pi/6:
			self.theta_sigh*=-1


def init_car(width,height):
	print(101)
	global car
	car = Car(width,height)

# width = 300
# height = 600
# car = Car(width,height)

