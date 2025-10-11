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
	
	def check_orbe(suelo, orbe):
		if orbe.x < suelo.x + (suelo.ancho / 2):
			if Personaje.check_colisiones(suelo, orbe) == True:
				orbe.direccionx = 0
		else:
			if Personaje.check_colisiones(suelo, orbe) == True:
				orbe.direccionx = 1

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
			self.x -= 1
			if self.x < 130:
				self.direccionx = 2
				hit = False
		if self.direccionx == 1:
			self.x += 1
			if self.x > 1150:
				self.direccionx = 2
				hit = False

	def Terremoto_Gordo(self):
		self.disparo1.Movimiento_Terremoto1()
		self.disparo2.Movimiento_Terremoto2()

	def Terremoto_Espada1(self):
		self.espada1.Caida_Espada(self.disparo3, self.disparo4)

	def Terremoto_Espada2(self):
		self.espada2.Caida_Espada(self.disparo5, self.disparo6)

	def Ataque_Orbe(self, enemigo):
		self.disparo1.Movimiento_Orbe(enemigo)
		self.disparo2.Movimiento_Orbe(enemigo)
		self.disparo3.Movimiento_Orbe(enemigo)
		self.disparo4.Movimiento_Orbe(enemigo)
		self.disparo5.Movimiento_Orbe(enemigo)
		self.disparo6.Movimiento_Orbe(enemigo)
	
	def Ataque_Mago(self, plataforma, suelo2, suelo3, suelo4, suelo5, suelo6):
		global ataque_mago, aleatorio1, aleatorio2, aleatorio3, cont_mago
		if ataque_mago > 0:
			aleatorio1 = randrange(2,7)
			if ataque_mago > 1:
				aleatorio2 = randrange(2,7)
				if ataque_mago > 2:
					aleatorio3 = randrange(2,7)
			self.x = 3000
			ataque_mago = 0
		if aleatorio1 != -1:
			self.x = 3000
			if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
				suelo2.golpear(plataforma, self, self.disparo1, self.disparo2, self.disparo3, self.disparo4, self.disparo5, self.disparo6)
			if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
				suelo3.golpear(plataforma, self, self.disparo1, self.disparo2, self.disparo3, self.disparo4, self.disparo5, self.disparo6)
			if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
				suelo4.golpear(plataforma, self, self.disparo1, self.disparo2, self.disparo3, self.disparo4, self.disparo5, self.disparo6)					
			if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
				suelo5.golpear(plataforma, self, self.disparo1, self.disparo2, self.disparo3, self.disparo4, self.disparo5, self.disparo6)
			if aleatorio1 == 6 or aleatorio2 == 6 or aleatorio3 == 6:
				suelo6.golpear(plataforma, self, self.disparo1, self.disparo2, self.disparo3, self.disparo4, self.disparo5, self.disparo6)
	
	def Ataque_Espaditas(self):
		self.disparo1.Movimiento_Espadita()
		self.disparo4.Movimiento_Espadita()
		if self.vidas <= 75:
			self.disparo2.Movimiento_Espadita()
			self.disparo5.Movimiento_Espadita()
			if self.vidas <= 25:
				self.disparo3.Movimiento_Espadita()
				self.disparo6.Movimiento_Espadita()

	def Ataque_Plataforma(self):
		global ataque_plataforma, aleatorio1, aleatorio2, aleatorio3, cont_plataforma
		if ataque_plataforma > 0:
			cont_plataforma = 0
			aleatorio3 = randrange(2, 14)
			if ataque_plataforma > 1:
				aleatorio2 = randrange(2,14)
				if ataque_plataforma > 2:
					aleatorio1 = randrange(2,14)
					self.y = 3000
			ataque_plataforma = 0
		if aleatorio3 != -1:
			if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (587.5, 499))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (587.5, 499))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (587.5, 499))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo2, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 2:
						self.x = 620
						self.y = 475
						aleatorio1 = -1
					elif aleatorio2 == 2:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (40, 499))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (40, 499))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (40, 499))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo3, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 3:
						self.x = 72.5
						self.y = 475
						aleatorio1 = -1
					elif aleatorio2 == 3:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (1140, 499))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (1140, 499))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (1140, 499))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo4, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 4:
						self.x = 1172.5
						self.y = 475
						aleatorio1 = -1
					elif aleatorio2 == 4:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (307.5, 399))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (307.5, 399))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (307.5, 399))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo5, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 5:
						self.x = 340
						self.y = 375
						aleatorio1 = -1
					elif aleatorio2 == 5:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 6 or aleatorio2 == 6 or aleatorio3 == 6:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (867.5, 399))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (867.5, 399))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (867.5, 399))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo6, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 6:
						self.x = 900
						self.y = 375
						aleatorio1 = -1
					elif aleatorio2 == 6:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 7 or aleatorio2 == 7 or aleatorio3 == 7:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (587.5, 299))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (587.5, 299))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (587.5, 299))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo7, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 7:
						self.x = 620
						self.y = 275
						aleatorio1 = -1
					elif aleatorio2 == 7:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 8 or aleatorio2 == 8 or aleatorio3 == 8:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (40, 299))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (40, 299))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (40, 299))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo8, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 8:
						self.x = 72.5
						self.y = 275
						aleatorio1 = -1
					elif aleatorio2 == 8:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 9 or aleatorio2 == 9 or aleatorio3 == 9:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (1140, 299))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (1140, 299))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (1140, 299))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo9, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 9:
						self.x = 1172.5
						self.y = 275
						aleatorio1 = -1
					elif aleatorio2 == 9:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 10 or aleatorio2 == 10 or aleatorio3 == 10:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (307.5, 199))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (307.5, 199))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (307.5, 199))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo10, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 10:
						self.x = 340
						self.y = 175
						aleatorio1 = -1
					elif aleatorio2 == 10:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 11 or aleatorio2 == 11 or aleatorio3 == 11:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (867.5, 199))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (867.5, 199))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (867.5, 199))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo11, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 11:
						self.x = 900
						self.y = 175
						aleatorio1 = -1
					elif aleatorio2 == 11:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 12 or aleatorio2 == 12 or aleatorio3 == 12:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (587.5, 99))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (587.5, 99))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (587.5, 99))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo12, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 12:
						self.x = 620
						self.y = 75
						aleatorio1 = -1
					elif aleatorio2 == 12:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 13 or aleatorio2 == 13 or aleatorio3 == 13:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (40, 99))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (40, 99))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (40, 99))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo13, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 13:
						self.x = 72.5
						self.y = 75
						aleatorio1 = -1
					elif aleatorio2 == 13:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
			if aleatorio1 == 14 or aleatorio2 == 14 or aleatorio3 == 14:
				if 0 < cont_plataforma <= 300:
					screen.blit(ninja_preataque, (1140, 99))
				elif 300 < cont_plataforma <= 400:
					screen.blit(ninja_preataque2, (1140, 99))
				elif cont_plataforma > 400:
					screen.blit(ninja_preataque3, (1140, 99))
				if cont_plataforma > 500:
					if Personaje.check_colisiones(suelo14, plataforma) == True:
						plataforma.vidas -= 25
					if aleatorio1 == 14:
						self.x = 1172.5
						self.y = 75
						aleatorio1 = -1
					elif aleatorio2 == 14:
						aleatorio2 = -1
					else:
						aleatorio3 = -1
		
	def Colores(self):
		global color, choice, racha, color_x, color_y, oscuridad
		color_y += 0.25
		if self.vidas < 75 or oscuridad == 1:
			color_y += 0.25
			if self.vidas < 50:
				color_y += 0.25
				if self.vidas < 25:
					color_y += 0.25
		if color == 8:
			screen.blit(rojo, [color_x, color_y])
		elif color == 9:
			screen.blit(azul, [color_x, color_y])
		elif color == 10:
			screen.blit(blanco, [color_x, color_y])
		elif color == 11:
			screen.blit(negro, [color_x, color_y])
		elif color == 12:
			screen.blit(dorado, [color_x, color_y])
		if (color != choice and choice != 0) or color_y == 750:
			plataforma.vidas -= 10
			racha = 0
			choice = 0
			color = randrange(8,13)
			color_x = randrange(0, 1230)
			color_y = 0
		if color == choice:
			racha += 1
			choice = 0
			color = randrange(8,13)
			color_x = randrange(0, 1230)
			color_y = 0
		if racha == 5:
			self.vidas -= 10
			racha = 0
			choice = 0
			color = randrange(8,13)
			color_x = randrange(0, 1230)
			color_y = 0

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def Movimiento_Terremoto1(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = 1380
		if self.x < 1380:
			self.x += 1
	
	def Movimiento_Terremoto2(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 10
			self.x = -100
		if self.x > -100:
			self.x -= 1
	
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
	
	def Movimiento_Orbe(self, enemigo):
		global oscuridad
		if self.x == 2000 and enemigo.x == 3000:
			self.x = 3000
		if self.x == 3000 and enemigo.x != 3000:
			self.x = 640
			self.y = 100
		if self.x < 2000:
			if self.direccionx == 0:
				self.x -= 2
			if self.direccionx == 1:
				self.x += 2
			if self.direcciony == 0:
				self.y -= 2
			if self.direcciony == 1:
				self.y += 2
			if self.x <= 0:
				self.direccionx = 1
			if self.x >= 1260:
				self.direccionx = 0
			if self.y <= 0:
				self.direcciony = 1
			if self.y >= 600:
				self.direcciony = 0
			if Personaje.check_colisiones(self, plataforma) == True:
				plataforma.vidas -= 10
				if oscuridad == 0:
					self.x = 2000
					self.y = 2000
				else:
					self.x = 15
					self.y = 15
	
	def Movimiento_Espadita(self):
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 20
			self.x = 1280
			self.y = 210
		if self.direccionx == 0:
			if self.direcciony == 0:
				screen.blit(espadita2_1, [self.x-15, self.y-15])
			else:
				screen.blit(espadita2_2, [self.x-15, self.y-15])
			self.x -= 1
		if self.direccionx == 1:
			if self.direcciony == 0:
				screen.blit(espadita1_1, [self.x-15, self.y-15])
			else:
				screen.blit(espadita1_2, [self.x-15, self.y-15])
			self.x += 1
		if self.direcciony == 0:
			self.y -= 2.5
		if self.direcciony == 1:
			self.y += 2.5
		if self.x <= 0 and self.direccionx == 0:
			self.x = 1260
		if self.x >= 1280 and self.direccionx == 1:
			self.x = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 700:
			self.direcciony = 0

class Suelo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas, direccionx, direcciony):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas, direccionx, direcciony)
	
	def check_suelo(self, sprite1):
		if (sprite1.y + sprite1.largo) > self.y and sprite1.y < (self.y + self.largo) and (sprite1.x + sprite1.ancho) > self.x and sprite1.x < (self.x + self.ancho):
			return True
	
	def golpear(self, plataforma, enemigo, orbe1, orbe2, orbe3, orbe4, orbe5, orbe6):
		global cont_mago, aleatorio1, aleatorio2, aleatorio3, ataque_mago
		self.largo = 1000
		if self.y != 599 or self.y != 3000:
			self.color = (0,255,0)
		else:
			self.color = (0, 0, 0)
		if 0 < cont_mago <= 200:
			self.y -= 0.25
		elif 50 < cont_mago <= 400:
			self.y += 0.25
		elif self.y > 0 and 400 < cont_mago <= 800:
			self.y -= 2
		elif cont_mago > 5000:
			if self.y == 599:
				self.color = (0, 0, 0)
				enemigo.x = self.x
				if cont_mago > 10000:
					cont_mago = 0
					ataque_mago = 1
					if enemigo.vidas <= 60:
						ataque_mago = 2
						if enemigo.vidas <= 20:
							ataque_mago = 3
					aleatorio1 = -1
					aleatorio2 = -1
					aleatorio3 = -1
			else:
				self.y += 1
		if self.y <= 0:
			if Personaje.check_colisiones(self, plataforma) == True:
				plataforma.vidas = 0
			Personaje.check_orbe(self, orbe1)
			Personaje.check_orbe(self, orbe2)
			Personaje.check_orbe(self, orbe3)
			Personaje.check_orbe(self, orbe4)
			Personaje.check_orbe(self, orbe5)
			Personaje.check_orbe(self, orbe6)
	
	def reducir(self, enemigo):
		if self.ancho <= 583 and self.x >= 350:
			enemigo.x = 800
		else:
			enemigo.x = 3000
			if self.ancho > 583:
				self.ancho -= 1
			if self.x < 350:
				self.x += 0.5

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
suelo2 = Suelo(587.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo3 = Suelo(40, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo4 = Suelo(1140, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo5 = Suelo(307.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo6 = Suelo(867.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo7 = Suelo(587.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo8 = Suelo(40, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo9 = Suelo(1140, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo10 = Suelo(307.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo11 = Suelo(867.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo12 = Suelo(587.5, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo13 = Suelo(40, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
suelo14 = Suelo(1140, 3000, 100, 1, (0, 0, 0), 0, 0, 0)
fondo1 = transform.scale(image.load("shoshin-kantetsu_images/fondo1.jpg").convert(), (1280, 720))
fondo2 = transform.scale(image.load("shoshin-kantetsu_images/fondo2.jpg").convert(), (1280, 720))
fondo3 = transform.scale(image.load("shoshin-kantetsu_images/fondo3.jpg").convert(), (1280, 720))
fondo4 = transform.scale(image.load("shoshin-kantetsu_images/fondo4.jpg").convert(), (1280, 720))
fondo5 = transform.scale(image.load("shoshin-kantetsu_images/fondo5.jpg").convert(), (1280, 720))
fondo6 = transform.scale(image.load("shoshin-kantetsu_images/fondo6.jpg").convert(), (1280, 720))
fondo7 = transform.scale(image.load("shoshin-kantetsu_images/fondo7.jpg").convert(), (1280, 720))
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
ninja1 = transform.scale(image.load("shoshin-kantetsu_images/ninja1_1.png"), (75, 150))
ninja2 = transform.scale(image.load("shoshin-kantetsu_images/ninja2_1.png"), (75, 150))
ninja_preataque = transform.scale(image.load("shoshin-kantetsu_images/ninja_preataque.png"), (100, 100))
ninja_preataque2 = transform.scale(image.load("shoshin-kantetsu_images/ninja_preataque2.png"), (100, 100))
ninja_preataque3 = transform.scale(image.load("shoshin-kantetsu_images/ninja_preataque3.png"), (100, 100))
columna = transform.scale(image.load("shoshin-kantetsu_images/columna.png"), (120, 250))
columna_vieja = transform.scale(image.load("shoshin-kantetsu_images/columna_vieja.png"), (120, 500))
estatua = transform.scale(image.load("shoshin-kantetsu_images/estatua.png"), (96, 164))
estatua_rojo = transform.scale(image.load("shoshin-kantetsu_images/estatua_rojo.png"), (96, 164))
estatua_azul = transform.scale(image.load("shoshin-kantetsu_images/estatua_azul.png"), (96, 164))
estatua_negro = transform.scale(image.load("shoshin-kantetsu_images/estatua_negro.png"), (96, 164))
estatua_blanco = transform.scale(image.load("shoshin-kantetsu_images/estatua_blanco.png"), (96, 164))
estatua_dorado = transform.scale(image.load("shoshin-kantetsu_images/estatua_dorado.png"), (96, 164))
rojo = transform.scale(image.load("shoshin-kantetsu_images/rojo.png"), (50, 50))
azul = transform.scale(image.load("shoshin-kantetsu_images/azul.png"), (50, 50))
negro = transform.scale(image.load("shoshin-kantetsu_images/negro.png"), (50, 50))
blanco = transform.scale(image.load("shoshin-kantetsu_images/blanco.png"), (50, 50))
dorado = transform.scale(image.load("shoshin-kantetsu_images/dorado.png"), (50, 50))
mago1 = transform.scale(image.load("shoshin-kantetsu_images/mago1.png"), (100, 100))
mago2 = transform.scale(image.load("shoshin-kantetsu_images/mago2.png"), (100, 100))
orbe = transform.scale(image.load("shoshin-kantetsu_images/orbe.png"), (50, 50))
orbe_o = transform.scale(image.load("shoshin-kantetsu_images/orbe_o.png"), (50, 50))
padre1 = transform.scale(image.load("shoshin-kantetsu_images/padre1.png"), (150, 150))
padre2 = transform.scale(image.load("shoshin-kantetsu_images/padre2.png"), (150, 150))
espadita1_1 = transform.scale(image.load("shoshin-kantetsu_images/espada1_1.png"), (50, 50))
espadita1_2 = transform.scale(image.load("shoshin-kantetsu_images/espada1_2.png"), (50, 50))
espadita2_1 = transform.scale(image.load("shoshin-kantetsu_images/espada2_1.png"), (50, 50))
espadita2_2 = transform.scale(image.load("shoshin-kantetsu_images/espada2_2.png"), (50, 50))
oscuridad1 = transform.scale(image.load("shoshin-kantetsu_images/oscuridad1.png"), (150, 150))
oscuridad2 = transform.scale(image.load("shoshin-kantetsu_images/oscuridad2.png"), (150, 150))
animacion_hikaru = 0
animacion_gordo = 0
animacion_ninja = 3
save_vida = 90
level = 0
retry = False
fondo = fondo1
cut_scene_manager = CutSceneManager(screen)

while True:
	global salto, angulo, x_jump, salto_doble, w, quieto, correr, ataque, ataque_espada, time_ataque, terremoto, hit, suelo, x_sup, jump, ataque_plataforma, aleatorio1, aleatorio2, aleatorio3, cont_plataforma, color, choice, racha, ataque_mago, cont_mago, oscuridad
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
		cont_plataforma = 600
		color = randrange(8, 13)
		choice = 0
		racha = 0
		color_x = randrange(0, 1230)
		color_y = 0
		ataque_mago = -1
		cont_mago = 0
		oscuridad = 0
		#cut_scene_manager.start_cut_scene(CutSceneZero(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 0
	if level == 0 and z == 0: #TUTORIAL
		fondo = fondo1
		#cut_scene_manager.start_cut_scene(CutSceneTutorial(plataforma))
		if cut_scene_manager.cut_scene is None:
			level = 1
			z = 1
	if level == 1 and z == 1:
		fondo = fondo2
		plataforma.vidas = 100
		plataforma.x = 130
		plataforma.y = 576
		enemigo.vidas = 100
		save_vida = 90
		enemigo.x = 1150
		enemigo.y = 550
		terremoto = True
		enemigo.direccionx = 0
		enemigo.espada1.y = -100
		enemigo.espada2.y = -100
		enemigo.disparo1.x = 1380
		enemigo.disparo2.x = -100
		enemigo.disparo3.x = 1380
		enemigo.disparo4.x = -100
		enemigo.disparo5.x = 1380
		enemigo.disparo6.x = -100
		cut_scene_manager.start_cut_scene(CutSceneOneStart(plataforma))
		if cut_scene_manager.cut_scene is None:
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
		plataforma.vidas = 100
		plataforma.x = 350
		plataforma.y = 475
		enemigo.vidas = 100
		save_vida = 90
		enemigo.x = 900
		enemigo.y = 175
		ninja = 3
		cut_scene_manager.start_cut_scene(CutSceneSecondStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 3
	if level == 3 and z == 3:
		fondo = fondo4
		suelo1.y = 599
		suelo2.y = 3000
		suelo3.y = 3000
		suelo4.y = 3000
		suelo5.y = 3000
		suelo6.y = 3000
		suelo7.y = 449
		suelo8.y = 149
		suelo9.y = 149
		suelo10.y = 299
		suelo11.y = 299
		suelo12.y = 149
		suelo13.y = 3000
		suelo14.y = 3000
		enemigo.vidas = 100
		enemigo.x = 3000
		plataforma.vidas = 100
		plataforma.x = 130
		plataforma.y = 575
		cut_scene_manager.start_cut_scene(CutSceneThreeStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 4
	if level == 4 and z == 4:
		fondo = fondo5
		suelo1.y = 3000
		suelo2.x = 0
		suelo2.y = 599
		suelo2.ancho = 256
		suelo2.largo = 300
		suelo3.x = 256
		suelo3.y = 599
		suelo3.ancho = 256
		suelo3.largo = 300
		suelo4.x = 512
		suelo4.y = 599
		suelo4.ancho = 256
		suelo4.largo = 300
		suelo5.x = 768
		suelo5.y = 599
		suelo5.ancho = 256
		suelo5.largo = 300
		suelo6.x = 1024
		suelo6.y = 599
		suelo6.ancho = 256
		suelo6.largo = 300
		suelo7.y = 3000
		suelo8.y = 3000
		suelo9.y = 3000
		suelo10.y = 3000
		suelo11.y = 3000
		suelo12.y = 3000
		enemigo.vidas = 100
		enemigo.x = 1150
		enemigo.y = 550
		plataforma.vidas = 100
		plataforma.x = 130
		plataforma.y = 576
		enemigo.disparo1.largo = 20
		enemigo.disparo1.ancho = 20
		enemigo.disparo2.largo = 20
		enemigo.disparo2.ancho = 20
		enemigo.disparo3.largo = 20
		enemigo.disparo3.ancho = 20
		enemigo.disparo4.largo = 20
		enemigo.disparo4.ancho = 20
		enemigo.disparo5.largo = 20
		enemigo.disparo5.ancho = 20
		enemigo.disparo6.largo = 20
		enemigo.disparo6.ancho = 20
		enemigo.disparo1.x = enemigo.x
		enemigo.disparo1.direccionx = 0
		enemigo.disparo1.direcciony = 1
		enemigo.disparo2.x = enemigo.x
		enemigo.disparo2.direccionx = 1
		enemigo.disparo2.direcciony = 0
		enemigo.disparo3.x = 5000
		enemigo.disparo3.direccionx = 0
		enemigo.disparo3.direcciony = 1
		enemigo.disparo4.x = 5000
		enemigo.disparo4.direccionx = 1
		enemigo.disparo4.direcciony = 0
		enemigo.disparo5.x = 5000
		enemigo.disparo5.direccionx = 0
		enemigo.disparo5.direcciony = 1
		enemigo.disparo6.x = 5000
		enemigo.disparo6.direccionx = 1
		enemigo.disparo6.direcciony = 0
		aleatorio1 = -1
		aleatorio2 = -1
		aleatorio3 = -1
		cont_mago = 0
		ataque_mago = -1
		suelo2.color = (0,0,0)
		suelo3.color = (0,0,0)
		suelo4.color = (0,0,0)
		suelo5.color = (0,0,0)
		suelo6.color = (0,0,0)
		cut_scene_manager.start_cut_scene(CutSceneFourStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 5
	if level == 5 and z == 5:
		fondo = fondo6
		suelo1.y = 474
		enemigo.vidas = 100
		enemigo.x = 1150
		enemigo.y = 400
		plataforma.vidas = 100
		plataforma.x = 130
		plataforma.y = 450
		enemigo.disparo1.largo = 20
		enemigo.disparo1.ancho = 20
		enemigo.disparo2.largo = 20
		enemigo.disparo2.ancho = 20
		enemigo.disparo3.largo = 20
		enemigo.disparo3.ancho = 20
		enemigo.disparo4.largo = 20
		enemigo.disparo4.ancho = 20
		enemigo.disparo5.largo = 20
		enemigo.disparo5.ancho = 20
		enemigo.disparo6.largo = 20
		enemigo.disparo6.ancho = 20
		enemigo.disparo1.x = 0
		enemigo.disparo1.direccionx = 1
		enemigo.disparo1.direcciony = 1
		enemigo.disparo2.x = -300
		enemigo.disparo2.direccionx = 1
		enemigo.disparo2.direcciony = 0
		enemigo.disparo3.x = -600
		enemigo.disparo3.direccionx = 1
		enemigo.disparo3.direcciony = 1
		enemigo.disparo4.x = 1280
		enemigo.disparo4.direccionx = 0
		enemigo.disparo4.direcciony = 0
		enemigo.disparo5.x = 1580
		enemigo.disparo5.direccionx = 0
		enemigo.disparo5.direcciony = 1
		enemigo.disparo6.x = 1880
		enemigo.disparo6.direccionx = 0
		enemigo.disparo6.direcciony = 0
		cut_scene_manager.start_cut_scene(CutSceneFiveStart(plataforma))
		if cut_scene_manager.cut_scene is None:
			z = 6
	if level == 6 and z == 6:
		oscuridad = 1

		fondo = fondo7
		suelo1.y = 599
		suelo2.y = 3000
		suelo3.y = 3000
		suelo4.y = 3000
		suelo5.y = 3000
		suelo6.y = 3000
		suelo7.y = 449
		suelo8.y = 149
		suelo9.y = 149
		suelo10.y = 299
		suelo11.y = 299
		suelo12.y = 149
		suelo13.y = 3000
		suelo14.y = 3000
		enemigo.vidas = 100
		enemigo.x = 3000

		enemigo.disparo1.largo = 20
		enemigo.disparo1.ancho = 20
		enemigo.disparo2.largo = 20
		enemigo.disparo2.ancho = 20
		enemigo.disparo3.largo = 20
		enemigo.disparo3.ancho = 20
		enemigo.disparo4.largo = 20
		enemigo.disparo4.ancho = 20
		enemigo.disparo1.x = 320
		enemigo.disparo1.direccionx = 0
		enemigo.disparo1.direcciony = 1
		enemigo.disparo2.x = 640
		enemigo.disparo2.direccionx = 1
		enemigo.disparo2.direcciony = 0
		enemigo.disparo3.x = 960
		enemigo.disparo3.direccionx = 0
		enemigo.disparo3.direcciony = 1
		enemigo.disparo4.x = 1280
		enemigo.disparo4.direccionx = 1
		enemigo.disparo4.direcciony = 0
		enemigo.disparo5.x = 5000
		enemigo.disparo6.x = 5000

		z = 7

	animacion_hikaru += 1
	#print(plataforma.x)
	#print(plataforma.y)

	#FONDO
	screen.blit(fondo, [0, 0])
	barra_hp(screen, 50, 40, enemigo.vidas, (255,0,0))
	barra_hp(screen, 1060, 40, plataforma.vidas, (0,0,255))
	screen.blit(vida_hikaru, [1000, -100])
	screen.blit(vida_boss, [-25, -100])
	#plataforma.DibujarObjeto()
	#enemigo.DibujarObjeto()
	
	if (cut_scene_manager.cut_scene is None and retry == False) or (level == 0 and z == 0):
		plataforma.Movimiento()
		plataforma.Ataque()
	
	if level == 0:
		suelo1.DibujarObjeto()
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False

	if level == 1:
		suelo1.DibujarObjeto()
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False	
		#ANIMACION GORDO
		if retry == False and cut_scene_manager.cut_scene is None:
			if enemigo.vidas <= save_vida:
				if enemigo.x <= 130:
					enemigo.direccionx = 1
				elif enemigo.x >= 1150:
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
				if terremoto == True: #and suelo == False:
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
		
		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True

		if enemigo.vidas <= 0:
			cut_scene_manager.start_cut_scene(CutSceneOneFinal(plataforma))
			if cut_scene_manager.cut_scene is None:
				level = 2

	if level == 2:
		if plataforma.y > 720:
			plataforma.vidas = 0
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma) or suelo2.check_suelo(plataforma) or suelo3.check_suelo(plataforma) or suelo4.check_suelo(plataforma) or suelo5.check_suelo(plataforma) or suelo6.check_suelo(plataforma) or suelo7.check_suelo(plataforma) or suelo8.check_suelo(plataforma) or suelo9.check_suelo(plataforma) or suelo10.check_suelo(plataforma) or suelo11.check_suelo(plataforma) or suelo12.check_suelo(plataforma) or suelo13.check_suelo(plataforma) or suelo14.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False
		if retry == False and cut_scene_manager.cut_scene is None and z == 3:
			if enemigo.vidas <= save_vida:
				save_vida = enemigo.vidas - 10
				ataque_plataforma = 3
				cont_plataforma = 0
			enemigo.Ataque_Plataforma()
			if cont_plataforma < 600:
				cont_plataforma += 1
			else:
				cont_plataforma = 0
				if enemigo.vidas <= 75:
					ataque_plataforma = 1
				if enemigo.vidas <= 50:
					ataque_plataforma = 2
		screen.blit(columna, [30, 200])
		screen.blit(columna, [30, 400])
		screen.blit(columna, [30, 600])
		screen.blit(columna, [575, 200])
		screen.blit(columna, [575, 400])
		screen.blit(columna, [575, 600])
		screen.blit(columna, [1130, 200])
		screen.blit(columna, [1130, 400])
		screen.blit(columna, [1130, 600])
		screen.blit(columna, [300, 300])
		screen.blit(columna, [300, 500])
		screen.blit(columna, [850, 300])
		screen.blit(columna, [850, 500])
		#ANIMACION NINJA
		if enemigo.vidas <= 75 and animacion_ninja == 3 and z == 3:
			ninja1 = transform.scale(image.load("shoshin-kantetsu_images/ninja1_2.png"), (75, 150))
			ninja2 = transform.scale(image.load("shoshin-kantetsu_images/ninja2_2.png"), (75, 150))
			animacion_ninja = 2
		elif enemigo.vidas <= 50 and animacion_ninja == 2 and z == 3:
			ninja1 = transform.scale(image.load("shoshin-kantetsu_images/ninja1_3.png"), (75, 150))
			ninja2 = transform.scale(image.load("shoshin-kantetsu_images/ninja2_3.png"), (75, 150))
			animacion_ninja = 1
		if enemigo.x <= 640:
			screen.blit(ninja1, [enemigo.x-20, enemigo.y-25])
		else:
			screen.blit(ninja2, [enemigo.x-25, enemigo.y-25])
		
		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True
		
		if enemigo.vidas <= 0 and z == 3:
			cut_scene_manager.start_cut_scene(CutSceneSecondFinal(plataforma))
			if cut_scene_manager.cut_scene is None:
				level = 3
	
	if level == 3:
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma) or suelo7.check_suelo(plataforma) or suelo8.check_suelo(plataforma) or suelo9.check_suelo(plataforma) or suelo10.check_suelo(plataforma) or suelo11.check_suelo(plataforma) or suelo12.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False
		screen.blit(columna_vieja, [30, 147])
		screen.blit(columna_vieja, [575, 147])
		screen.blit(columna_vieja, [575, 447])
		screen.blit(columna_vieja, [1130, 147])
		screen.blit(columna_vieja, [300, 297])
		screen.blit(columna_vieja, [850, 297])
		screen.blit(estatua, [582.5, 325])
		screen.blit(estatua_rojo, [37.5, 35])
		screen.blit(estatua_blanco, [307.5, 185])
		screen.blit(estatua_dorado, [582.5, 35])
		screen.blit(estatua_negro, [857.5, 185])
		screen.blit(estatua_azul, [1137.5, 35])
		suelo1.DibujarObjeto()

		if retry == False and cut_scene_manager.cut_scene is None:
			enemigo.Colores()

		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True

		if (ataque == 1 or ataque == 2) and plataforma.direcciony == 0 and color_y >= 50:
			#if suelo7.check_suelo(plataforma): #ESTATUA
				#choice = 7
			if suelo8.check_suelo(plataforma): #ROJO
				choice = 8
			if suelo9.check_suelo(plataforma): #AZUL
				choice = 9
			if suelo10.check_suelo(plataforma): #BLANCO
				choice = 10
			if suelo11.check_suelo(plataforma): #NEGRO
				choice = 11
			if suelo12.check_suelo(plataforma): #DORADO
				choice = 12
		
		if enemigo.vidas <= 0 and z == 4:
			cut_scene_manager.start_cut_scene(CutSceneThreeFinal(plataforma))
			if cut_scene_manager.cut_scene is None:
				level = 4
	
	if level == 4:
		screen.blit(orbe, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
		screen.blit(orbe, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
		screen.blit(orbe, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
		screen.blit(orbe, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])
		screen.blit(orbe, [enemigo.disparo5.x-15, enemigo.disparo5.y-15])
		screen.blit(orbe, [enemigo.disparo6.x-15, enemigo.disparo6.y-15])
		suelo2.DibujarObjeto()
		suelo3.DibujarObjeto()
		suelo4.DibujarObjeto()
		suelo5.DibujarObjeto()
		suelo6.DibujarObjeto()

		if suelo2.check_suelo(plataforma) or suelo3.check_suelo(plataforma) or suelo4.check_suelo(plataforma) or suelo5.check_suelo(plataforma) or suelo6.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False

		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True
		
		if enemigo.vidas <= 80 and cont_mago == 200:
			if enemigo.disparo3.x == 5000:
				enemigo.disparo3.x = 3000
				enemigo.disparo4.x = 3000
			if enemigo.vidas <= 40:
				if enemigo.disparo5.x == 5000:
					enemigo.disparo5.x = 3000
					enemigo.disparo6.x = 3000
		
		if cont_mago == 0:
			save_vida = enemigo.vidas - 10
		if enemigo.vidas <= save_vida:
			cont_mago = 10000

		if enemigo.vidas == 100:
			enemigo.x = 1150

		if enemigo.vidas <= 80:
			if ataque_mago == -1:
				ataque_mago = 1
			else:
				cont_mago += 1
		
		if retry == False and cut_scene_manager.cut_scene is None and z == 5:
			enemigo.Ataque_Orbe(enemigo)
			enemigo.Ataque_Mago(plataforma, suelo2, suelo3, suelo4, suelo5, suelo6)
		
		#ANIMACION MAGO
		if enemigo.x <= 640:
			screen.blit(mago1, [enemigo.x-40, enemigo.y-50])
		else:
			screen.blit(mago2, [enemigo.x-30, enemigo.y-50])
		
		if enemigo.vidas <= 0 and z == 5:
			cut_scene_manager.start_cut_scene(CutSceneFourFinal(plataforma))
			if cut_scene_manager.cut_scene is None:
				level = 5
	
	if level == 5:
		suelo1.DibujarObjeto()
		if suelo1.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False
		
		if retry == False and cut_scene_manager.cut_scene is None:
			enemigo.Ataque_Espaditas()

		if enemigo.vidas <= 75 and enemigo.vidas > 50:
			enemigo.x = 150
		if enemigo.vidas < 50:
			if (enemigo.vidas <= 40 and enemigo.vidas > 30) or (enemigo.vidas <= 20 and enemigo.vidas > 10):
				enemigo.x = 400
			if (enemigo.vidas <= 30 and enemigo.vidas > 20) or (enemigo.vidas <= 10 and enemigo.vidas > 0):
				enemigo.x = 800 
		
		if enemigo.vidas <= 50 and enemigo.vidas > 40:
			suelo1.reducir(enemigo)
		
		#ANIMACION PADRE
		if enemigo.x <= 640:
			screen.blit(padre1, [enemigo.x-60, enemigo.y-55])
		else:
			screen.blit(padre2, [enemigo.x-60, enemigo.y-55])
		
		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True

		if enemigo.vidas <= 0 and z == 6:
			cut_scene_manager.start_cut_scene(CutSceneFiveMiddle(plataforma))
			if cut_scene_manager.cut_scene is None:
				level = 6
	
	if level == 6:
		#COMPROBACION SUELO
		if suelo1.check_suelo(plataforma) or suelo7.check_suelo(plataforma) or suelo8.check_suelo(plataforma) or suelo9.check_suelo(plataforma) or suelo10.check_suelo(plataforma) or suelo11.check_suelo(plataforma) or suelo12.check_suelo(plataforma):
			suelo = True
		else:
			suelo = False
		screen.blit(columna_vieja, [30, 147])
		screen.blit(columna_vieja, [575, 147])
		screen.blit(columna_vieja, [575, 447])
		screen.blit(columna_vieja, [1130, 147])
		screen.blit(columna_vieja, [300, 297])
		screen.blit(columna_vieja, [850, 297])
		screen.blit(estatua_rojo, [37.5, 35])
		screen.blit(estatua_blanco, [307.5, 185])
		screen.blit(estatua_dorado, [582.5, 35])
		screen.blit(estatua_negro, [857.5, 185])
		screen.blit(estatua_azul, [1137.5, 35])
		suelo1.DibujarObjeto()

		screen.blit(orbe_o, [enemigo.disparo1.x-15, enemigo.disparo1.y-15])
		screen.blit(orbe_o, [enemigo.disparo2.x-15, enemigo.disparo2.y-15])
		screen.blit(orbe_o, [enemigo.disparo3.x-15, enemigo.disparo3.y-15])
		screen.blit(orbe_o, [enemigo.disparo4.x-15, enemigo.disparo4.y-15])

		if retry == False and cut_scene_manager.cut_scene is None:
			enemigo.Colores()
			enemigo.Ataque_Orbe(enemigo)

		if plataforma.vidas <= 0:
			screen.fill((0, 0, 0))
			cut_scene_manager.start_cut_scene(CutSceneRetry(plataforma))
			retry = True

		if (ataque == 1 or ataque == 2) and plataforma.direcciony == 0 and color_y >= 50:
			if suelo8.check_suelo(plataforma): #ROJO
				choice = 8
			if suelo9.check_suelo(plataforma): #AZUL
				choice = 9
			if suelo10.check_suelo(plataforma): #BLANCO
				choice = 10
			if suelo11.check_suelo(plataforma): #NEGRO
				choice = 11
			if suelo12.check_suelo(plataforma): #DORADO
				choice = 12
			
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

	if z == -1:
		screen.fill((0, 0, 0))

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
				enemigo.vidas = 0
			if evento.key == K_UP:
				z = 5
				level = 5
			if evento.key == K_z and retry == True:
				cut_scene_manager.cut_scenes_complete = []
				z -= 1
				retry = False
			if evento.key == K_ESCAPE:
				quit()
				exit()
		else:
			quieto = True
