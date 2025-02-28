from pygame import *
from math import *
screen = display.set_mode((1280, 720), FULLSCREEN)
display.set_caption('Shoshi-Kantetsu')

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.color = color
		self.vidas = vidas
		self.direccionx = direccionx
		self.direcciony = direcciony

	def DibujarObjeto(self):
		draw.rect(screen, self.color, (self.x,self.y,self.ancho,self.largo))

class Personaje(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
		self.espada = Espada(self.x, self.y, 20, 50, (255,255,255), 1, 0, 0)
	
	def Movimiento(self):
		global salto, angulo, x_jump, salto_doble, w
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if keys[K_w]==1 and angulo == 0.0:
			angulo = 0.001
			self.direcciony = 1
			salto = True
			w = True
		if keys[K_w]==0:
			w = False
		if keys[K_w]==1 and w == False and salto_doble == False:
			angulo = 0.001
			x_jump = self.y
			salto_doble = True
		self.y = x_jump - sin(angulo)*100
		if angulo > 0:
			angulo += 0.025
		if angulo > pi:
			angulo = 0.0
		if angulo == 0.0 and self.y < 400:
			self.y += 1

		if keys[K_s]:
			self.direcciony = 0
		if keys[K_a]:
			self.direccionx = 0
			self.direcciony = 2
			if x > 0:
				self.x -= 1
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			if x < 1260:
				self.x += 1
		self.DibujarObjeto()

	def Ataque(self):
		keys = key.get_pressed()
		if keys[K_SPACE] == 1:
			self.espada.Movimiento(plataforma)
		#else:
		#	self.espada.y = 10000

	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Espada(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)

	def Movimiento(self, plataforma):
		if plataforma.direcciony == 1:
			self.ancho = 50
			self.largo = 20
			self.y = plataforma.y - 50
			self.x = plataforma.x - 15
		elif plataforma.direcciony == 0:
			self.ancho = 50
			self.largo = 20
			self.y = plataforma.y + 50
			self.x = plataforma.x - 15
		else:
			if plataforma.direccionx == 1:
				self.ancho = 20
				self.largo = 50
				self.x = plataforma.x + 50
				self.y = plataforma.y - 15
			elif plataforma.direccionx == 0:
				self.ancho = 20
				self.largo = 50
				self.x = plataforma.x - 50
				self.y = plataforma.y - 15
		self.DibujarObjeto()

plataforma = Personaje(625, 350, 20, 20,(255,255,255), 3, 1, 2)
jump = 0
z = 0

while True:
	global salto, angulo, x_jump, salto_doble, w
	if z == 0:
		salto = False
		angulo = 0.0
		x_jump = 400
		salto_doble = False
		w = False
		z = 1
	if salto == True:
		jump += 1
		if jump == 50:
			jump = 0
			x_jump = 400
			salto_doble = False
			salto = False
	if angulo == 0.0 and plataforma.y < 625 and x_jump != 400:
		x_jump = 400
		angulo = pi / 2
	screen.fill((0,0,0))
	plataforma.Movimiento()
	plataforma.Ataque()
	display.flip()
	for evento in event.get():
		if evento.type==QUIT:
				quit()
				exit()
		if evento.type==KEYDOWN:
			if evento.key == K_ESCAPE:
				quit()
				exit()
