from pygame import *
from random import *
from math import *
from cut_scenes import *
init()
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

		if keys[K_w]:
			self.direcciony = 1

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
		global ataque, ataque_espada
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
		if Personaje.check_colisiones(self, enemigo) and ataque_espada == ataque:
			enemigo.vidas -= 1
			if ataque_espada == 1:
				ataque_espada = 2
			elif ataque_espada == 2:
				ataque_espada = 0
		self.DibujarObjeto()

class Boss(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
		self.espada1 = Disparo(1000, -100, 20, 100, (255,0,0), 0, 0, 0)
		self.espada2 = Disparo(1000, -100, 20, 100, (255,0,0), 0, 0, 0)
		self.disparo1 = Disparo(1330, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo2 = Disparo(-50, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo3 = Disparo(1330, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo4 = Disparo(-50, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo5 = Disparo(1330, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo6 = Disparo(-50, 500, self.ancho, 100, (255,0,0), 0, 0, 0)

	def Movimiento_Gordo(self):
		global hit
		if Personaje.check_colisiones(self, plataforma) == True and hit == False:
			plataforma.vidas -= 10
			hit = True
		if self.direccionx == 0:
			self.x -= 2
			if self.x < 80:
				self.direccionx = 2
				hit = False
		if self.direccionx == 1:
			self.x += 2
			if self.x > 1200:
				self.direccionx = 2
				hit = False

	def Terremoto_Gordo(self):
		self.disparo1.Movimiento_Terremoto1()
		self.disparo2.Movimiento_Terremoto2()

	def Terremoto_Espada1(self):
		self.espada1.Caida_Espada(self.disparo3, self.disparo4)

	def Terremoto_Espada2(self):
		self.espada2.Caida_Espada(self.disparo5, self.disparo6)

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def Movimiento_Terremoto1(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = 1330
		if self.x < 1330:
			self.x += 2
	
	def Movimiento_Terremoto2(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = -50
		if self.x > -50:
			self.x -= 2
	
	def Caida_Espada(self, disparo1, disparo2):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.y = -100
			self.vidas = 0
		if self.y < 500:
			if self.y == -100:
				self.x = randrange(1, 13) * 100
			self.y += 1
		if self.y == 500:
			if self.vidas == 0:
				disparo1.x = self.x
				disparo2.x = self.x
				self.vidas = 1
			disparo1.Movimiento_Terremoto1()
			disparo2.Movimiento_Terremoto2()
		if disparo1.x == 1330 and disparo2.x == -50 and self.vidas == 1:
			self.y = -100
			self.vidas = 0

def barra_hp(screen, x, y, hp, color):
	largo = 165
	ancho = 10
	calculo_barra = int((hp / 100)*largo)
	draw.rect(screen, color, Rect(x, y, calculo_barra, ancho))

plataforma = Personaje(625, 500, 20, 20,(255,255,255), 100, 1, 2)
enemigo = Boss(100, 550, 30, 50, (255,0,0), 100, 1, 2)
jump = 0
level = 0
z = -1
fondo1 = transform.scale(image.load("shoshin-kantetsu_images/fondo1.jpg").convert(), (1280, 720))
fondo2 = transform.scale(image.load("shoshin-kantetsu_images/fondo2.jpg").convert(), (1280, 720))
fondo3 = transform.scale(image.load("shoshin-kantetsu_images/fondo3.jpg").convert(), (1280, 720))
fondo4 = transform.scale(image.load("shoshin-kantetsu_images/fondo4.jpg").convert(), (1280, 720))
fondo5 = transform.scale(image.load("shoshin-kantetsu_images/fondo5.jpg").convert(), (1280, 720))
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
gordo1 = transform.scale(image.load("shoshin-kantetsu_images/gordo1.png"), (100, 100))
gordo2 = transform.scale(image.load("shoshin-kantetsu_images/gordo2.png"), (100, 100))
gordo_attack = transform.scale(image.load("shoshin-kantetsu_images/gordo_attack.png"), (100, 100))
gordo_run = transform.scale(image.load("shoshin-kantetsu_images/gordo_run.png"), (100, 100))
gordo_run_ = transform.scale(image.load("shoshin-kantetsu_images/gordo_run_.png"), (100, 100))
gordo_run2 = transform.scale(image.load("shoshin-kantetsu_images/gordo_run2.png"), (100, 100))
gordo_run2_ = transform.scale(image.load("shoshin-kantetsu_images/gordo_run2_.png"), (100, 100))
espada_gordo = transform.scale(image.load("shoshin-kantetsu_images/espada_gordo.png"), (100, 100))
slash = transform.scale(image.load("shoshin-kantetsu_images/slash.png"), (100, 100))
slash_ = transform.scale(image.load("shoshin-kantetsu_images/slash_.png"), (100, 100))
vida_hikaru = transform.scale(image.load("shoshin-kantetsu_images/vida_hikaru.png"), (300, 300))
vida_boss = transform.scale(image.load("shoshin-kantetsu_images/vida_boss.png"), (300, 300))
animacion_hikaru = 0
animacion_gordo = 0
save_vida = 90
level = 1
fondo = fondo2
cut_scene_manager = CutSceneManager(screen)

while True:
	global salto, angulo, x_jump, salto_doble, w, quieto, correr, ataque, ataque_espada, time_ataque, terremoto, hit
	if z == -1:
		salto = False
		angulo = 0.0
		x_jump = 575
		salto_doble = False
		w = False
		quieto = True
		correr = False
		ataque = 0
		ataque_espada = 0
		time_ataque = 0
		terremoto = True
		hit = False
		#cut_scene_manager.start_cut_scene(CutSceneZero(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 0

	animacion_hikaru += 1

	if cut_scene_manager.cut_scene is None:
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
		
		plataforma.Movimiento()
		plataforma.Ataque()

	#FONDO
	screen.blit(fondo, [0, 0])
	draw.rect(screen, (0, 0, 0, 255), (0, 600, 1280, 300))
	barra_hp(screen, 50, 40, enemigo.vidas, (255,0,0))
	barra_hp(screen, 1060, 40, plataforma.vidas, (0,0,255))
	screen.blit(vida_hikaru, [1000, -100])
	screen.blit(vida_boss, [-25, -100])
	#plataforma.DibujarObjeto()
	#enemigo.DibujarObjeto()

	if level == 1:
		#ANIMACION GORDO
		if enemigo.vidas <= save_vida:
			if enemigo.x <= 80:
				enemigo.direccionx = 1
			elif enemigo.x >= 1200:
				enemigo.direccionx = 0
			save_vida = enemigo.vidas - 10
			terremoto = True
		enemigo.Movimiento_Gordo()
		if enemigo.vidas <= 100:
			enemigo.Terremoto_Espada1()
			screen.blit(espada_gordo, [enemigo.espada1.x-40, enemigo.espada1.y])
			screen.blit(slash, [enemigo.disparo3.x-50, enemigo.disparo3.y])
			screen.blit(slash_, [enemigo.disparo4.x-20, enemigo.disparo4.y])
			if enemigo.vidas <= 100:
				enemigo.Terremoto_Espada2()
				screen.blit(espada_gordo, [enemigo.espada2.x-40, enemigo.espada2.y])
				screen.blit(slash, [enemigo.disparo5.x-50, enemigo.disparo5.y])
				screen.blit(slash_, [enemigo.disparo6.x-20, enemigo.disparo6.y])
		if enemigo.direccionx == 2:
			if terremoto == True and plataforma.x != 625:
				enemigo.disparo1.x = enemigo.x + 30
				enemigo.disparo2.x = enemigo.x
				terremoto = False
			enemigo.Terremoto_Gordo()
			screen.blit(slash, [enemigo.disparo1.x-50, enemigo.disparo1.y])
			screen.blit(slash_, [enemigo.disparo2.x-20, enemigo.disparo2.y])
		if enemigo.disparo1.x != 1330 and enemigo.disparo2.x != -50:
			screen.blit(gordo_attack, [enemigo.x-40, enemigo.y-32.5])
		elif enemigo.direccionx != 2:
			animacion_gordo += 1
			if animacion_gordo <= 100:
				if enemigo.direccionx == 0:
					screen.blit(gordo_run_, [enemigo.x-40, enemigo.y-32.5])
				else:
					screen.blit(gordo_run, [enemigo.x-40, enemigo.y-32.5])
			elif animacion_gordo > 100:
				if enemigo.direccionx == 0:
					screen.blit(gordo_run2_, [enemigo.x-40, enemigo.y-32.5])
				else:
					screen.blit(gordo_run2, [enemigo.x-40, enemigo.y-32.5])
				if animacion_gordo >= 200:
					animacion_gordo = 0
		else:
			if enemigo.x <= 640:
				screen.blit(gordo1, [enemigo.x-40, enemigo.y-32.5])
			else:
				screen.blit(gordo2, [enemigo.x-40, enemigo.y-32.5])
		if enemigo.vidas <= 0:
			level = 2

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
		if ataque_espada == 0:
			ataque_espada = 1
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

	cut_scene_manager.update()
	cut_scene_manager.draw()
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
