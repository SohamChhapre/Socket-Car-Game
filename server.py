from flask import Flask 
from flask_sockets import Sockets

import pygame , sys

from pygame.locals import *
import math
from random import randint
import time
import car


app = Flask(__name__) 
sockets = Sockets(app)

@sockets.route('/accelerometer') 
def echo_socket(ws):
	f=open("accelerometer.txt","a")
	while True:
		message = ws.receive()
		print(message) 
		ws.send(message)
		print(message, file=f)
	f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
	f=open("gyroscope.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()
	
@sockets.route('/magnetometer')
def echo_socket(ws):
	f=open("magnetometer.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/orientation')
def echo_socket(ws):

	while True:
		message = ws.receive()
		# print(message)
		data = float(message.split(",")[1])
		# print(data)
		if data<20 and data>0:
			# print("left" , data//10)
			car.car.left(2)
		if data>20 and data<40:
			car.car.left(1)
			# car.car.left()

		elif data>100 and data<145:
			# print("right" , (360-data)//10)
			# if time.time()-now>1/5:
				# if data//10==2:
			car.car.right(2)
		elif data>145 and data<200:
			car.car.right(3)
			# car.car.right()




@sockets.route('/stepcounter')
def echo_socket(ws):
	f=open("stepcounter.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/thermometer')
def echo_socket(ws):
	f=open("thermometer.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/lightsensor')
def echo_socket(ws):
	f=open("lightsensor.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/proximity')
def echo_socket(ws):
	f=open("proximity.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

@sockets.route('/geolocation')
def echo_socket(ws):
	f=open("geolocation.txt","a")
	while True:
		message = ws.receive()
		print(message)
		ws.send(message)
		print(message, file=f)
	f.close()

	

@app.route('/') 
def hello(): 
	return 'Hello World!'

def start(pygame1,DISPLAYSURF1):
	global pygame
	global DISPLAYSURF
	pygame,DISPLAYSURF = pygame1,DISPLAYSURF1


	print(id(car))

	print("server started")
	global now
	now = time.time()
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5001), app, handler_class=WebSocketHandler)

	server.serve_forever()
