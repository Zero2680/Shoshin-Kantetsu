from pygame import *
from sys import *
init()


def draw_text(screen, text, size, color, x, y):
    main_font = font.SysFont('cambria', size)
    text_surface = main_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class CutSceneRetry:
    
    def __init__(self, player):

        # Variables
        self.name = 'retry'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'retry': "PRESS Z TO RETRY",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_z]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['retry']):
                self.text_counter += 0.4
            else:
                if space:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['retry'][0:int(self.text_counter)],
                100,
                (255, 255, 255),
                225,
                310
            )

class CutSceneZero:
    
    def __init__(self, player):

        # Variables
        self.name = 'zero'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "You don't have what it takes.",
            'two': "I've seen your training, but... it's not enough.",
            'three': "You'll never become a great swordsman.",
            'four': "That's not true!",
            'five': "I'm improving every day.",
            'six': "If you trained me properly...",
            'seven': "Being a great swordsman isn't just skill with a blade.",
            'eight': "It's a matter of heart, discipline, sacrifice.",
            'nine': "You'll be the first to break our legacy.",
            'ten': "You're a disgrace to the family.",
            'eleven': "I don't care about the legacy!",
            'twelve': "I'll prove you wrong...",
            'thirteen': "I'll leave and achieve it on my own, without your help.",
            'fourteen': "Yeah, right!",
            'fiveteen': "I don't want you back here until you've done it.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 4
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 5
                    self.time = 0
                    self.text_counter = 0

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 6
                    self.time = 0
                    self.text_counter = 0

        if self.step == 6:
            if int(self.text_counter) < len(self.text['seven']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 7
                    self.time = 0
                    self.text_counter = 0

        if self.step == 7:
            if int(self.text_counter) < len(self.text['eight']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 8
                    self.time = 0
                    self.text_counter = 0

        if self.step == 8:
            if int(self.text_counter) < len(self.text['nine']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 9
                    self.time = 0
                    self.text_counter = 0

        if self.step == 9:
            if int(self.text_counter) < len(self.text['ten']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 10
                    self.time = 0
                    self.text_counter = 0

        if self.step == 10:
            if int(self.text_counter) < len(self.text['eleven']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 11
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 11:
            if int(self.text_counter) < len(self.text['twelve']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 12
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 12:
            if int(self.text_counter) < len(self.text['thirteen']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 13
                    self.time = 0
                    self.text_counter = 0

        if self.step == 13:
            if int(self.text_counter) < len(self.text['fourteen']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 14
                    self.time = 0
                    self.text_counter = 0

        if self.step == 14:
            if int(self.text_counter) < len(self.text['fiveteen']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 7:
            draw_text(
                screen,
                self.text['eight'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 8:
            draw_text(
                screen,
                self.text['nine'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 9:
            draw_text(
                screen,
                self.text['ten'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 10:
            draw_text(
                screen,
                self.text['eleven'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 11:
            draw_text(
                screen,
                self.text['twelve'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 12:
            draw_text(
                screen,
                self.text['thirteen'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 13:
            draw_text(
                screen,
                self.text['fourteen'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 14:
            draw_text(
                screen,
                self.text['fiveteen'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

class CutSceneTutorial:
    
    def __init__(self, player):

        # Variables
        self.name = 'tutorial'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Hikaru!",
            'two': "There's nothing left before you begin the Path to the Mountain.",
            'three': "You will face thousands of challenges on your own.",
            'four': "Are you ready?",
            'five': "Of course!",
            'six': "I'll complete it and show my father he was never right.",
            'seven': "Alright...",
            'eight': "Let's review everything before you go.",
            'nine': "Use A and D to move across the stage.",
            'ten': "Use W and S to jump and crouch.",
            'eleven': "Use SPACE to attack enemies.",
            'twelve': "You can perform different attacks while jumping or crouching.",
            'thirteen': "Perfect, you have everything you need for the Path to the Mountain!",
            'fourteen': "Good luck on your journey, Hikaru!",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 500:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 4
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 5
                    self.time = 0
                    self.text_counter = 0

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 6
                    self.time = 0
                    self.text_counter = 0

        if self.step == 6:
            if int(self.text_counter) < len(self.text['seven']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 7
                    self.time = 0
                    self.text_counter = 0

        if self.step == 7:
            if int(self.text_counter) < len(self.text['eight']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 8
                    self.time = 0
                    self.text_counter = 0

        if self.step == 8:
            if int(self.text_counter) < len(self.text['nine']):
                self.text_counter += 0.4
            else:
                if (pressed[K_a] or pressed[K_d]) and self.time == 500:
                    self.step = 9
                    self.time = 0
                    self.text_counter = 0

        if self.step == 9:
            if int(self.text_counter) < len(self.text['ten']):
                self.text_counter += 0.4
            else:
                if (pressed[K_w] or pressed[K_s]) and self.time == 500:
                    self.step = 10
                    self.time = 0
                    self.text_counter = 0

        if self.step == 10:
            if int(self.text_counter) < len(self.text['eleven']):
                self.text_counter += 0.4
            else:
                if space and self.time == 500:
                    self.step = 11
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 11:
            if int(self.text_counter) < len(self.text['twelve']):
                self.text_counter += 0.4
            else:
                if space and self.time == 500:
                    self.step = 12
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 12:
            if int(self.text_counter) < len(self.text['thirteen']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.step = 13
                    self.time = 0
                    self.text_counter = 0

        if self.step == 13:
            if int(self.text_counter) < len(self.text['fourteen']):
                self.text_counter += 0.4
            else:
                if space and self.time >= 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                35,
                (213, 107, 42),
                50,
                650
            )

        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 7:
            draw_text(
                screen,
                self.text['eight'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 8:
            draw_text(
                screen,
                self.text['nine'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 9:
            draw_text(
                screen,
                self.text['ten'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )
        
        if self.step == 10:
            draw_text(
                screen,
                self.text['eleven'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 11:
            draw_text(
                screen,
                self.text['twelve'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 12:
            draw_text(
                screen,
                self.text['thirteen'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

        if self.step == 13:
            draw_text(
                screen,
                self.text['fourteen'][0:int(self.text_counter)],
                35,
                (255, 203, 219),
                50,
                650
            )

class CutSceneOneStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'one_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Are you seeking the Path to the Mountain?",
            'two': "No human steel has reached so high.",
            'three': "I am the Guardian of Celestial Steel, forged of thunder and blade.",
            'four': "If you wish to continue… prove your edge fears not the weight of the world!",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

class CutSceneOneFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'one_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        #Dialogue
        self.text = {
            'one': "You have endured the storm of steel... and your spirit did not break.",
            'two': "The Path to the Mountain opens before you...",
            'three': "Let your sword be more than an edge... let it be truth.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (205, 173, 91),
                50,
                650
            )

class CutSceneSecondStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'second_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "You climbed this far, but not all paths lead upward...",
            'two': "One wrong step, and the mountain will swallow you.",
            'three': "The wind is our ally. The void, our ground. Here, you are the stranger.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (139, 155, 180),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (139, 155, 180),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (139, 155, 180),
                50,
                650
            )

class CutSceneSecondFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'second_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        #Dialogue
        self.text = {
            'one': "If you managed to overcome the wind and the void...",
            'two': "Then perhaps the mountain will accept you.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (139, 155, 180),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (139, 155, 180),
                50,
                650
            )

class CutSceneThreeStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'three_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "The colors of the sky are the judgement of the gods.",
            'two': "Only those who can read its truth and make it resonate with the earth.",
            'three': "Will be worthy to continue.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (182, 182, 182),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (182, 182, 182),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (182, 182, 182),
                50,
                650
            )

class CutSceneThreeFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'three_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        #Dialogue
        self.text = {
            'one': "You have joined heaven and earth...",
            'two': "The Path remains open.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (182, 182, 182),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (182, 182, 182),
                50,
                650
            )

class CutSceneFourStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'four_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "You have come too far, swordsman.",
            'two': "The Path is not for those who walk...",
            'three': "But for those who rise.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (83, 233, 22),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (83, 233, 22),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (83, 233, 22),
                50,
                650
            )

class CutSceneFourFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'four_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        #Dialogue
        self.text = {
            'one': "Move forward, swordsman... but remember:",
            'two': "The higher you climb, the smaller the ground beneath your feet becomes.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (83, 233, 22),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (83, 233, 22),
                50,
                650
            )

class CutSceneFiveStart:
    
    def __init__(self, player):

        # Variables
        self.name = 'five_start'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "I told you again and again... you were not born to be a swordsman.",
            'two': "Your edge is weak, your spirit, trembling.",
            'three': "And yet you climbed up here?",
            'four': "Then I will seal your fate myself.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

class CutSceneFiveMiddle:
    
    def __init__(self, player):

        # Variables
        self.name = 'five_middle'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "Is that all?",
            'two': "Is that the great swordsman you swore you'd be?",
            'three': "You can barely stand...",
            'four': "And you think you can beat me.",
            'five': "How naive! You haven't seen who your father really is.",
            'six': "Now you will face the true Guardian of the Mountain!",
            'seven': "The darkness that neither you nor your spirit will be able to cut!",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 4
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 5
                    self.time = 0
                    self.text_counter = 0

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 6
                    self.time = 0
                    self.text_counter = 0

        if self.step == 6:
            if int(self.text_counter) < len(self.text['seven']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                35,
                (107, 25, 25),
                50,
                650
            )

class CutSceneFiveFinal:
    
    def __init__(self, player):

        # Variables
        self.name = 'five_final'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "I thought you would never reach my level.",
            'two': "That your steps would always fall behind mine.",
            'three': "But today... you caught up to me.",
            'four': "And you surpassed me.",
            'five': "You are no longer the son who sought my approval.",
            'six': "You are the heir of the Path to the Mountain.",
            'seven': "The guardian… is no longer me.",
            'eight': "Now, it is you.",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 100:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.step = 1
                    self.time = 0
                    self.text_counter = 0

        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 2
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 3
                    self.time = 0
                    self.text_counter = 0

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 4
                    self.time = 0
                    self.text_counter = 0
        
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 5
                    self.time = 0
                    self.text_counter = 0

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 6
                    self.time = 0
                    self.text_counter = 0

        if self.step == 6:
            if int(self.text_counter) < len(self.text['seven']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.step = 7
                    self.time = 0
                    self.text_counter = 0

        if self.step == 7:
            if int(self.text_counter) < len(self.text['eight']):
                self.text_counter += 0.4
            else:
                if space and self.time == 100:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )
        
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                35,
                (255, 255, 255),
                50,
                650
            )

        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                35,
                (107, 25, 25),
                50,
                650
            )

        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                35,
                (107, 25, 25),
                50,
                650
            )
        
        if self.step == 7:
            draw_text(
                screen,
                self.text['eight'][0:int(self.text_counter)],
                35,
                (107, 25, 25),
                50,
                650
            )

class CutSceneThanks:
    
    def __init__(self, player):

        # Variables
        self.name = 'thanks'
        self.step = 0
        self.timer = time.get_ticks()
        self.cut_scene_running = True
        self.time = 0

        # Dialogue
        self.text = {
            'one': "THANKS FOR PLAYING",
        }
        self.text_counter = 0

    def update(self):

        pressed = key.get_pressed()
        space = pressed[K_SPACE]
        
        if self.time < 500:
            self.time += 1

        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space and self.time == 500:
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                100,
                (255, 255, 255),
                120,
                300
            )

class CutSceneManager:

    def __init__(self, screen):
        self.cut_scenes_complete = []
        self.cut_scene = None
        self.cut_scene_running = False

        # Drawing variables
        self.screen = screen
        self.window_size = 0

    def start_cut_scene(self, cut_scene):
        if cut_scene.name not in self.cut_scenes_complete:
            self.cut_scenes_complete.append(cut_scene.name)
            self.cut_scene = cut_scene
            self.cut_scene_running = True

    def end_cut_scene(self):
        self.cut_scene = None
        self.cut_scene_running = False

    def update(self):

        if self.cut_scene_running:
            if self.window_size < self.screen.get_height()*0.3: self.window_size += 2
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.end_cut_scene()

    def draw(self):
        if self.cut_scene_running:
            # Draw rect generic to all cut scenes
            draw.rect(self.screen, (0, 0, 0, 0), (0, 600, self.screen.get_width(), self.window_size))
            # Draw specific cut scene details
            self.cut_scene.draw(self.screen)
