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
		global salto, angulo, x_jump, salto_doble, w, correr, suelo, x_sup, jump
		x = self.x
		y = self.y
		keys = key.get_pressed()
		#print(angulo)
		#print(suelo)
		if angulo == 0.0 and suelo == False:
			self.y += 2
		else:
			if suelo == True:
				salto = False
				angulo = 0.0
				x_jump = self.y
				x_sup = self.y
				salto_doble = True
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
			
			if salto == True:
				jump += 1
				if jump == 50:
					jump = 0
					x_jump = x_sup
					salto_doble = False
					salto = False
			if angulo == 0.0 and suelo == False and x_jump != x_sup:
				x_jump = x_sup
				angulo = pi / 2

			self.y = x_jump - sin(angulo)*100
			
			if 0 < angulo:
				angulo += 0.025
			if angulo > pi:
				angulo = 0.0

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
		self.disparo1 = Disparo(1380, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo2 = Disparo(-100, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo3 = Disparo(1380, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo4 = Disparo(-100, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo5 = Disparo(1380, 500, self.ancho, 100, (255,0,0), 0, 0, 0)
		self.disparo6 = Disparo(-100, 500, self.ancho, 100, (255,0,0), 0, 0, 0)

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
	
	def Ataque_Plataforma(self):
		global ataque_plataforma, aleatorio1, aleatorio2, aleatorio3, cont_plataforma
		if ataque_plataforma > 0:
			cont_plataforma = 0
			aleatorio1 = randrange(2, 14)
			if ataque_plataforma > 1:
				aleatorio2 = randrange(2,14)
				if ataque_plataforma > 2:
					aleatorio3 = randrange(2,14)
			ataque_plataforma = 0
		if aleatorio1 != -1:
			if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
				screen.blit(ninja_preataque, (587.5, 499))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo2, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 2:
						aleatorio1 = -1
					elif aleatorio2 == 2:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
				screen.blit(ninja_preataque, (40, 499))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo3, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 3:
						aleatorio1 = -1
					elif aleatorio2 == 3:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
				screen.blit(ninja_preataque, (1140, 499))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo4, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 4:
						aleatorio1 = -1
					elif aleatorio2 == 4:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
				screen.blit(ninja_preataque, (307.5, 399))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo5, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 5:
						aleatorio1 = -1
					elif aleatorio2 == 5:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 6 or aleatorio2 == 6 or aleatorio3 == 6:
				screen.blit(ninja_preataque, (867.5, 399))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo6, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 6:
						aleatorio1 = -1
					elif aleatorio2 == 6:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 7 or aleatorio2 == 7 or aleatorio3 == 7:
				screen.blit(ninja_preataque, (587.5, 299))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo7, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 7:
						aleatorio1 = -1
					elif aleatorio2 == 7:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 8 or aleatorio2 == 8 or aleatorio3 == 8:
				screen.blit(ninja_preataque, (40, 299))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo8, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 8:
						aleatorio1 = -1
					elif aleatorio2 == 8:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 9 or aleatorio2 == 9 or aleatorio3 == 9:
				screen.blit(ninja_preataque, (1140, 299))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo9, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 9:
						aleatorio1 = -1
					elif aleatorio2 == 9:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 10 or aleatorio2 == 10 or aleatorio3 == 10:
				screen.blit(ninja_preataque, (307.5, 199))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo10, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 10:
						aleatorio1 = -1
					elif aleatorio2 == 10:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 11 or aleatorio2 == 11 or aleatorio3 == 11:
				screen.blit(ninja_preataque, (867.5, 199))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo11, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 11:
						aleatorio1 = -1
					elif aleatorio2 == 11:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 12 or aleatorio2 == 12 or aleatorio3 == 12:
				screen.blit(ninja_preataque, (587.5, 99))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo12, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 12:
						aleatorio1 = -1
					elif aleatorio2 == 12:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 13 or aleatorio2 == 13 or aleatorio3 == 13:
				screen.blit(ninja_preataque, (40, 99))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo13, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 13:
						aleatorio1 = -1
					elif aleatorio2 == 13:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 14 or aleatorio2 == 14 or aleatorio3 == 14:
				screen.blit(ninja_preataque, (1140, 99))
				if cont_plataforma > 1000:
					if Personaje.check_colisiones(suelo14, plataforma) == True:
						plataforma.vidas -= 10
					if aleatorio1 == 14:
						aleatorio1 = -1
					elif aleatorio2 == 14:
						aleatorio2 = -1
					else:
						aleatorio3 = -1	

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def Movimiento_Terremoto1(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = 1380
		if self.x < 1380:
			self.x += 2
	
	def Movimiento_Terremoto2(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = -100
		if self.x > -100:
			self.x -= 2
	
	def Caida_Espada(self, disparo1, disparo2):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.y = -100
			disparo1.x = 1380
			disparo2.x = -100
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
		if disparo1.x == 1380 and disparo2.x == -100 and self.vidas == 1:
			self.y = -100
			self.vidas = 0

class Suelo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def check_suelo(self, sprite1):
		if (sprite1.y + sprite1.largo) > self.y and sprite1.y < (self.y + self.largo) and (sprite1.x + sprite1.ancho) > self.x and sprite1.x < (self.x + self.ancho):
			return True

def barra_hp(screen, x, y, hp, color):
	largo = 165
	ancho = 10
	calculo_barra = int((hp / 100)*largo)
	draw.rect(screen, color, Rect(x, y, calculo_barra, ancho))

plataforma = Personaje(625, 500, 20, 25,(255,255,255), 100, 1, 2)
enemigo = Boss(100, 550, 30, 50, (255,0,0), 100, 1, 2)
level = 0
z = -1
suelo1 = Suelo(0, 599, 1280, 300, (0, 0, 0), 0, 0, 0)
suelo2 = Suelo(587.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo3 = Suelo(40, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo4 = Suelo(1140, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo5 = Suelo(307.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo6 = Suelo(867.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo7 = Suelo(587.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo8 = Suelo(40, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo9 = Suelo(1140, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo10 = Suelo(307.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo11 = Suelo(867.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo12 = Suelo(587.5, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo13 = Suelo(40, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
suelo14 = Suelo(1140, 3000, 100, 10, (0, 0, 0), 0, 0, 0)
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
ninja1 = transform.scale(image.load("shoshin-kantetsu_images/ninja1.png"), (75, 150))
ninja2 = transform.scale(image.load("shoshin-kantetsu_images/ninja2.png"), (75, 150))
ninja_preataque = transform.scale(image.load("shoshin-kantetsu_images/ninja_preataque.png"), (100, 100))
animacion_hikaru = 0
animacion_gordo = 0
save_vida = 90
level = 0
fondo = fondo2
cut_scene_manager = CutSceneManager(screen)

while True:
	global salto, angulo, x_jump, salto_doble, w, quieto, correr, ataque, ataque_espada, time_ataque, terremoto, hit, suelo, x_sup, jump, ataque_plataforma, aleatorio1, aleatorio2, aleatorio3, cont_plataforma
	if z == -1:
		salto = False
		angulo = 0.0
		x_jump = 575
		x_sup = 575
		salto_doble = False
		w = False
		quieto = True
		correr = False
		ataque = 0
		ataque_espada = 0
		time_ataque = 0
		terremoto = True
		hit = False
		suelo = False
		jump = 0
		ataque_plataforma = 0
		aleatorio1 = -1
		aleatorio2 = -1
		aleatorio3 = -1
		cont_plataforma = 1100
		#cut_scene_manager.start_cut_scene(CutSceneZero(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 0
	if level == 0 and z == 0: #TUTORIAL
		level = 1
		z = 1
	if level == 1 and z == 1:
		z = 2
	if level == 2 and z == 2:
		fondo = fondo3
		enemigo.vidas = 100
		enemigo.largo = 125
		enemigo.y = 475
		suelo1.y = 3000
		suelo2.y = 599
		suelo3.y = 599
		suelo4.y = 599
		suelo5.y = 499
		suelo6.y = 499
		suelo7.y = 399
		suelo8.y = 399
		suelo9.y = 399
		suelo10.y = 299
		suelo11.y = 299
		suelo12.y = 199
		suelo13.y = 199
		suelo14.y = 199
		z = 3

	animacion_hikaru += 1
	#print(plataforma.y)

	if cut_scene_manager.cut_scene is None:
		
		plataforma.Movimiento()
		plataforma.Ataque()

	#FONDO
	screen.blit(fondo, [0, 0])
	#draw.rect(screen, (0, 0, 0, 255), (0, 600, 1280, 300))
	barra_hp(screen, 50, 40, enemigo.vidas, (255,0,0))
	barra_hp(screen, 1060, 40, plataforma.vidas, (0,0,255))
	screen.blit(vida_hikaru, [1000, -100])
	screen.blit(vida_boss, [-25, -100])
	plataforma.DibujarObjeto()
	enemigo.DibujarObjeto()
	
	if level == 1:
		suelo1.DibujarObjeto()
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma) or suelo2.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False	
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
			if terremoto == True and suelo == False:
				enemigo.disparo1.x = enemigo.x + 30
				enemigo.disparo2.x = enemigo.x
				terremoto = False
			enemigo.Terremoto_Gordo()
			screen.blit(slash, [enemigo.disparo1.x-50, enemigo.disparo1.y])
			screen.blit(slash_, [enemigo.disparo2.x-20, enemigo.disparo2.y])
		if enemigo.disparo1.x != 1380 and enemigo.disparo2.x != -100:
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

	if level == 2:
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma) or suelo2.check_suelo(plataforma) or suelo3.check_suelo(plataforma) or suelo4.check_suelo(plataforma) or suelo5.check_suelo(plataforma) or suelo6.check_suelo(plataforma) or suelo7.check_suelo(plataforma) or suelo8.check_suelo(plataforma) or suelo9.check_suelo(plataforma) or suelo10.check_suelo(plataforma) or suelo11.check_suelo(plataforma) or suelo12.check_suelo(plataforma) or suelo13.check_suelo(plataforma) or suelo14.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False
		enemigo.Ataque_Plataforma()
		if cont_plataforma < 1100:
			cont_plataforma += 1
		suelo2.DibujarObjeto()
		suelo3.DibujarObjeto()
		suelo4.DibujarObjeto()
		suelo5.DibujarObjeto()
		suelo6.DibujarObjeto()
		suelo7.DibujarObjeto()
		suelo8.DibujarObjeto()
		suelo9.DibujarObjeto()
		suelo10.DibujarObjeto()
		suelo11.DibujarObjeto()
		suelo12.DibujarObjeto()
		suelo13.DibujarObjeto()
		suelo14.DibujarObjeto()
		if enemigo.x <= 640:
			screen.blit(ninja1, [enemigo.x-40, enemigo.y-32.5])
		else:
			screen.blit(ninja2, [enemigo.x-40, enemigo.y-32.5])
		if enemigo.vidas <= 0:
			level = 3

	#ANIMACIÓN HIKARU
	if suelo == False and ataque == 0:
		if plataforma.direccionx == 0:
			screen.blit(hikaru_jump_, [plataforma.x-10, plataforma.y-20])
		elif plataforma.direccionx == 1:
			screen.blit(hikaru_jump, [plataforma.x-20, plataforma.y-20])

	if quieto == True and correr == False and ataque == 0 and suelo == True:
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
	
	if plataforma.direcciony == 0 and suelo == True and quieto == False and ataque == 0:
		if plataforma.direccionx == 0:
			screen.blit(hikaru_agachar_, [plataforma.x-10, plataforma.y-20])
		elif plataforma.direccionx == 1:
			screen.blit(hikaru_agachar, [plataforma.x-20, plataforma.y-20])

	if correr == True and suelo == True:
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
			if evento.key == K_RIGHT:
				level += 1
			if evento.key == K_LEFT:
				ataque_plataforma = 3
			if evento.key == K_ESCAPE:
				quit()
				exit()
		else:
			quieto = True
