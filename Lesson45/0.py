import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BG = 52,78,91
font = pygame.font.SysFont('arialblack',30)
TEXT_COLOR = 255,255,255

class Button:
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.clicked = False

    def draw(self,screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0]==False:
                self.clicked = False

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action



def draw_text(text,font,text_color,x,y):
    surface = font.render(text,True,text_color)
    screen.blit(surface,(x,y))

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('главное меню')

resume_img = pygame.image.load('button_resume.png')
options_img = pygame.image.load('button_options.png')
quit_img = pygame.image.load('button_quit.png')
video_img = pygame.image.load('button_video.png')
audio_img = pygame.image.load('button_audio.png')
keys_img = pygame.image.load('button_keys.png')
back_img = pygame.image.load('button_back.png')

resume_button = Button(304,125,resume_img)
options_button = Button(297,250,options_img)
quit_button = Button(336,375,quit_img)

video_button = Button(226,75,video_img)
audio_button = Button(225,200,audio_img)
keys_button = Button(246,325,keys_img)
back_button = Button(332,450,back_img)


game_pause = False
menu_state = 'main'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True

    screen.fill(BG)
    if game_pause==True:
        if menu_state == 'main':
            if resume_button.draw(screen) == True:
                game_pause = False
            elif options_button.draw(screen) == True:
                menu_state = 'options'
            elif quit_button.draw(screen) == True:
                running = False
        elif menu_state == 'options':
            if video_button.draw(screen):
                print('video')
            if audio_button.draw(screen):
                print('audio')
            if keys_button.draw(screen):
                print('keys')
            if back_button.draw(screen):
                menu_state = 'main'
    else:
        draw_text('Нажмите пробел для паузы',font,TEXT_COLOR,160,250)
    pygame.display.update()
pygame.quit()