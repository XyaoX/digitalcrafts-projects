import pygame
import random
import time

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

start_ticks=pygame.time.get_ticks()

key_down={
    'up':False,
    'down':False,
    'left':False,
    'right':False
}


class Background(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top=location


class Obstacle(object):
    def __init__(self,x,y):
        self.x=0
        self.y=0

    def update(self):
        self.x +=self.speed_x
        self.y += self.speed_y


class Obstacle_Up(Obstacle):
    def __init__(self,x,y,name):
        self.y=0
        self.x=random.randrange(0,960,50)
        self.name=name

    def name(self):
        return name

    def move(self):
        self.y+=7
        if self.y>720:
            self.y=-50

class Obstacle_Left(Obstacle):
    def __init__(self,x,y,name):
        self.x=0
        self.y=random.randrange(0,720,50)
        self.name=name

    def name(self):
        return name

    def move(self):
        self.x+=7
        if self.x>960:
            self.x=-50

class Obstacle_Right(Obstacle):
    def __init__(self,x,y,name):
        self.x=920
        self.y=random.randrange(0,720,50)
        self.name=name

    def name(self):
        return name

    def move(self):
        self.x-=7
        if self.x<0:
            self.x=960

class Obstacle_Down(Obstacle):
    def __init__(self,x,y):
        self.x=random.randrange(0,920,50)
        self.y=720
        self.name=name

    def name(self):
        return name

    def move(self):
        self.y-=7
        if self.y<0:
            self.y=750


class Sumo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 50

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def border(self):
        if self.x<-50:
            self.x=950
        elif self.x>950:
            self.x=-50
        if self.y<-50:
            self.y=750
        elif self.y>770:
            self.y=-30

    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)


#sumo image loader
sumo_up1=pygame.image.load('img/sumo/SumoBack.png')
sumo_up2=pygame.image.load('img/sumo/SumoBack2.png')
sumo_down1=pygame.image.load('img/sumo/SumoFront.png')
sumo_down2=pygame.image.load('img/sumo/SumoFront2.png')
sumo_left1=pygame.image.load('img/sumo/SumoLeft.png')
sumo_left2=pygame.image.load('img/sumo/SumoLeft2.png')
sumo_right1=pygame.image.load('img/sumo/SumoRight.png')
sumo_right2=pygame.image.load('img/sumo/SumoRight2.png')
apple=pygame.image.load('img/mov/Apple.png')
apple_rotten=pygame.image.load('img/mov/Apple_rotten.png')
blowfish=pygame.image.load('img/mov/Blowfish.png')
fish_fresh=pygame.image.load('img/mov/Fish_fresh.png')
fish_rotten=pygame.image.load('img/mov/Fish_rotten.png')
rice=pygame.image.load('img/mov/Rice_fresh.png')
rice_rotten=pygame.image.load('img/mov/Rice_rotten.png')
good_food=[apple,fish_fresh,rice]
bad_food=[apple_rotten,blowfish,fish_rotten,rice_rotten]



def animation(timer):
    if key_down['up']==True:
        if timer%2==0:
            return sumo_up1
        else:
            return sumo_up2

    elif key_down['down']==True:
        if timer%2==0:
            return sumo_down1
        else:
            return sumo_down2

    elif key_down['left']==True:
        if timer%2==0:
            return sumo_left1
        else:
            return sumo_left2

    elif key_down['right']==True:
        if timer%2==0:
            return sumo_right1
        else:
            return sumo_right2

    else:
        return sumo_down1




def main():
    # declare the size of the canvas
    width = 960
    height = 720
    white_color = (255, 255, 255)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    BackGround=Background('img/background.png',[0,0])
    obstacle_list=[apple,fish_fresh,rice,apple_rotten,blowfish,fish_rotten,rice_rotten]
    obstacle1,obstacle2,obstacle3=apple,rice,rice_rotten
    box=[Obstacle_Right(0,0,apple),Obstacle_Right(0,0,fish_fresh),Obstacle_Right(0,0,fish_rotten)]
    # Game initialization
    sumo=Sumo(450,350)

    stop_game = False
    while not stop_game:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    sumo.speed_y = 7
                    key_down['down']=True
                elif event.key == KEY_UP:
                    sumo.speed_y = -7
                    key_down['up']=True
                elif event.key == KEY_LEFT:
                    sumo.speed_x = -7
                    key_down['left']=True
                elif event.key == KEY_RIGHT:
                    sumo.speed_x = 7
                    key_down['right']=True
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    sumo.speed_y = 0
                    key_down['down']=False
                elif event.key == KEY_UP:
                    sumo.speed_y = 0
                    key_down['up']=False
                elif event.key == KEY_LEFT:
                    sumo.speed_x = 0
                    key_down['left']=False
                elif event.key == KEY_RIGHT:
                    sumo.speed_x = 0
                    key_down['right']=False


            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        sumo.update()
        sumo.border()
        #Loop for obstacles 
        for x in box:
            x.move()

        # Draw background
        screen.fill(white_color)
        screen.blit(BackGround.image,BackGround.rect)
        screen.blit(animation(seconds),(sumo.x,sumo.y))

        for i in box:
            screen.blit(i.name,(i.x,i.y))

        #Set the Gui title to "Con sumo"
        pygame.display.set_caption("Con Sumo")

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()