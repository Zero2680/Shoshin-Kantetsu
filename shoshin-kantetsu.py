from pygame import *
from math import *
screen = display.set_mode((1280, 720), FULLSCREEN)
display.set_caption('Shoshi-Kantetsu')

#HIJO: HIKARU		PADRE: TAKASHI

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
		global salto, angulo, x_jump, salto_doble, w, correr
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
		if angulo == 0.0 and self.y < 575:
			self.y += 1

		if keys[K_s]:
			self.direcciony = 0
		
		if keys[K_a]:
			self.direccionx = 0
			self.direcciony = 2
			correr = True
			if x > 0:
				self.x -= 1
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			correr = True
			if x < 1260:
				self.x += 1
		if keys[K_a] == 0 and keys[K_d] == 0:
			correr = False
		self.DibujarObjeto()

	def Ataque(self):
		global quieto, ataque, time_ataque
		keys = key.get_pressed()
		if keys[K_SPACE] == 1:
			self.espada.Movimiento(plataforma)
			quieto = False
			time_ataque += 1
			if ataque == 0:
				ataque = 1
			if time_ataque == 50:          
				if ataque == 1:
					ataque = 2
				else:
					ataque = 1
				time_ataque = 0
		if keys[K_SPACE] == 0:
			ataque = 0
			time_ataque = 0
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
		if plataforma.direcciony == 0:
			self.ancho = 50
			self.largo = 20
			self.y = plataforma.y + 25
			self.x = plataforma.x - 20
		elif plataforma.direcciony == 1:
			self.ancho = 50
			self.largo = 20
			self.y = plataforma.y - 25
			self.x = plataforma.x - 20 
		else:
			if plataforma.direccionx == 1:
				self.ancho = 20
				self.largo = 50
				self.x = plataforma.x + 25
				self.y = plataforma.y - 20
			elif plataforma.direccionx == 0:
				self.ancho = 20
				self.largo = 50
				self.x = plataforma.x - 25
				self.y = plataforma.y - 20
		self.DibujarObjeto()

plataforma = Personaje(625, 500, 20, 20,(255,255,255), 3, 1, 2)
jump = 0
z = 0
fondo1 = transform.scale(image.load("shoshin-kantetsu_images/fondo1.jpg").convert(), (1280, 720))
hikaru1 = transform.scale(image.load("shoshin-kantetsu_images/hikaru1.png"), (50, 50))
hikaru1_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru1_.png"), (50, 50))
hikaru2 = transform.scale(image.load("shoshin-kantetsu_images/hikaru2.png"), (50, 50))
hikaru2_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru2_.png"), (50, 50))
hikaru_jump = transform.scale(image.load("shoshin-kantetsu_images/hikaru_jump.png"), (50, 50))
hikaru_jump_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_jump_.png"), (50, 50))
hikaru_agachar = transform.scale(image.load("shoshin-kantetsu_images/hikaru_agachar.png"), (50, 50))
hikaru_agachar_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_agachar_.png"), (50, 50))
hikaru_land = transform.scale(image.load("shoshin-kantetsu_images/hikaru_land.png"), (50, 50))
hikaru_attack = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attack.png"), (75, 75))
hikaru_attack_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attack_.png"), (75, 75))
hikaru_attack2 = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attack2.png"), (75, 75))
hikaru_attack2_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attack2_.png"), (75, 75))
hikaru_attackup = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attackup.png"), (75, 75))
hikaru_attackdown = transform.scale(image.load("shoshin-kantetsu_images/hikaru_attackdown.png"), (75, 75))
hikaru_run = transform.scale(image.load("shoshin-kantetsu_images/hikaru_run.png"), (50, 50))
hikaru_run_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_run_.png"), (50, 50))
hikaru_run2 = transform.scale(image.load("shoshin-kantetsu_images/hikaru_run2.png"), (50, 50))
hikaru_run2_ = transform.scale(image.load("shoshin-kantetsu_images/hikaru_run2_.png"), (50, 50))
animacion_hikaru = 0
fondo = fondo1

while True:
	global salto, angulo, x_jump, salto_doble, w, quieto, correr, ataque, time_ataque
	if z == 0:
		salto = False
		angulo = 0.0
		x_jump = 575
		salto_doble = False
		w = False
		quieto = True
		correr = False
		ataque = 0
		time_ataque = 0
		z = 1
	
	animacion_hikaru += 1
	#print(correr)

	if salto == True:
		jump += 1
		if jump == 50:
			jump = 0
			x_jump = 575
			salto_doble = False
			salto = False
	if angulo == 0.0 and plataforma.y < 625 and x_jump != 575:
		x_jump = 575
		angulo = pi / 2
	
	#screen.fill((0,0,0))
	plataforma.Movimiento()
	plataforma.Ataque()

	#FONDO
	screen.blit(fondo, [0, 0])
	draw.rect(screen, (0, 0, 0), (0, 600, 1280, 300))

	#ANIMACIÓN HIKARU
	if plataforma.y != 575 and ataque == 0:
		if plataforma.direccionx == 0:
			screen.blit(hikaru_jump_, [plataforma.x-10, plataforma.y-20])
		elif plataforma.direccionx == 1:
			screen.blit(hikaru_jump, [plataforma.x-20, plataforma.y-20])

	if quieto == True and correr == False and ataque == 0 and plataforma.y == 575:
		if plataforma.direccionx == 0:
			if animacion_hikaru <= 100:
				screen.blit(hikaru1_, [plataforma.x-10, plataforma.y-20])
			if animacion_hikaru > 100:
				screen.blit(hikaru2_, [plataforma.x-10, plataforma.y-20])
				if animacion_hikaru >= 200:
					animacion_hikaru = 0
		elif plataforma.direccionx == 1:
			if animacion_hikaru <= 100:
				screen.blit(hikaru1, [plataforma.x-20, plataforma.y-20])
			if animacion_hikaru > 100:
				screen.blit(hikaru2, [plataforma.x-20, plataforma.y-20])
				if animacion_hikaru >= 200:
					animacion_hikaru = 0
	
	if plataforma.direcciony == 0 and plataforma.y == 575 and quieto == False and ataque == 0:
		if plataforma.direccionx == 0:
			screen.blit(hikaru_agachar_, [plataforma.x-10, plataforma.y-20])
		elif plataforma.direccionx == 1:
			screen.blit(hikaru_agachar, [plataforma.x-20, plataforma.y-20])

	if correr == True and plataforma.y == 575:
		if plataforma.direccionx == 0:
			if animacion_hikaru <= 50:
				screen.blit(hikaru_run_, [plataforma.x-10, plataforma.y-20])
			if animacion_hikaru > 50:
				screen.blit(hikaru_run2_, [plataforma.x-10, plataforma.y-20])
				if animacion_hikaru >= 100:
					animacion_hikaru = 0
		elif plataforma.direccionx == 1:
			if animacion_hikaru <= 50:
				screen.blit(hikaru_run, [plataforma.x-20, plataforma.y-20])
			if animacion_hikaru > 50:
				screen.blit(hikaru_run2, [plataforma.x-20, plataforma.y-20])
				if animacion_hikaru >= 100:
					animacion_hikaru = 0

	if ataque == 1:
		if plataforma.direcciony == 0:
			screen.blit(hikaru_attackdown, [plataforma.x-32.5, plataforma.y-32.5])
		elif plataforma.direcciony == 1:
			screen.blit(hikaru_attackup, [plataforma.x-32.5, plataforma.y-32.5])
		else:
			if plataforma.direccionx == 0:
				screen.blit(hikaru_attack_, [plataforma.x-22.5, plataforma.y-32.5])
			if plataforma.direccionx == 1:
				screen.blit(hikaru_attack, [plataforma.x-32.5, plataforma.y-32.5])
	elif ataque == 2:
		if plataforma.direcciony == 0:
			screen.blit(hikaru_attackdown, [plataforma.x-32.5, plataforma.y-32.5])
		elif plataforma.direcciony == 1:
			screen.blit(hikaru_attackup, [plataforma.x-32.5, plataforma.y-32.5])
		else:
			if plataforma.direccionx == 0:
				screen.blit(hikaru_attack2_, [plataforma.x-22.5, plataforma.y-32.5])
			if plataforma.direccionx == 1:
				screen.blit(hikaru_attack2, [plataforma.x-32.5, plataforma.y-32.5])

	display.flip()
	for evento in event.get():
		if evento.type==QUIT:
				quit()
				exit()
		if evento.type==KEYDOWN:
			quieto = False
			if evento.key == K_ESCAPE:
				quit()
				exit()
		else:
			quieto = True
