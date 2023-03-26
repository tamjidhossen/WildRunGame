import pygame
from pygame import mixer

pygame.init()

W = 800
H = 400
window = pygame.display.set_mode((W, H))


#setting window name(game name)
pygame.display.set_caption("Wild Run")


#loading game icon
ICON = pygame.image.load("sprites\Dinasour\Run4.png")
pygame.display.set_icon(ICON)

global environment_speed
environment_speed = 1


def rabbit_animation(): #rabbit running and jumping animation
    global rabbit_run, rabbit_index
    
    if rabbit_rect.bottom < 295:
        # rabit_index = 0
        rabbit_run = rabbit_list[1] #rabbit jump 
    else:
        rabbit_index += 0.3 
        if rabbit_index >= 8:
            rabbit_index = 0
        rabbit_run = rabbit_list[int(rabbit_index)]

def dinasour_animation(): #dinasour running and jumping animation
    global dinasour_run, dinasour_index
    
    if dinasour_rect.bottom < 338:
        # dinasour_index = 0
        dinasour_run = dinasour_list[2] #dinasour jump 
    else:
        dinasour_index += 0.32 
        if dinasour_index >= 8:
            dinasour_index = 0
        dinasour_run = dinasour_list[int(dinasour_index)]

def fox_animation(): #fox running and jumping animation
    global fox_run, fox_index
    
    if fox_rect.bottom < 325:
        # fox_index = 0
        fox_run = fox_list[5] #fox jump 
    else:
        fox_index += 0.5 
        if fox_index >= 9:
            fox_index = 0
        fox_run = fox_list[int(fox_index)]

def ninja_animation(): #ninja running and jumping animation
    global ninja_run, ninja_index
    
    if ninja_rect.bottom < 328:
        # ninja_index = 0
        ninja_run = ninja_list[3] #ninja jump 
    else:
        ninja_index += 0.5 
        if ninja_index >= 10:
            ninja_index = 0
        ninja_run = ninja_list[int(ninja_index)]


def game_score():
    global final_score 
    current_time = int(pygame.time.get_ticks()/200) - start_time
    final_score = current_time
    score_surf = font.render(str(current_time), False, (0,64,64))
    score_rect = score_surf.get_rect(center = (760,30))
    window.blit(score_surf, score_rect)

def final_score_endcard():
    final_score_surf = end_font.render(str(final_score), False, (255,255,255))
    final_score_rect = final_score_surf.get_rect(center = (480,215))
    window.blit(final_score_surf, final_score_rect)

def sprite_cutout(size, img_name):
    name = []
    cnt = 1
    for i in range(size):
        img = pygame.image.load(img_name+str(cnt)+".png").convert_alpha()
        name.append(img)
        cnt += 1
    return name



#music//////////////////////////////////////////////////
mixer.music.load('Sounds/BG_Music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.05)

jump_sound = mixer.Sound('Sounds\jump.wav')
jump_sound.set_volume(.1)

crash_sound = mixer.Sound('Sounds\crash.wav')
crash_sound.set_volume(.05)

selection_sound = mixer.Sound('Sounds\menu_selection.wav')
selection_sound.set_volume(.2)



#game assets 
sky = pygame.image.load("Background\Sky\sky1.png").convert()

bg1 = pygame.image.load("Background\Desert\mount.png").convert_alpha()
bg2 = pygame.image.load("Background\Fade BG\\bg2.png").convert_alpha()
bg3 = pygame.image.load("Background\\forest\\forest.png").convert_alpha()
fade_bg = pygame.image.load("Background\Fade BG\\fade-bg-1.png").convert_alpha()
fade_bg_2 = pygame.image.load("Background\Fade BG\\fade-bg-2.png").convert_alpha()
bg = bg1 #initializing bg ............. # change bg

road = pygame.image.load("Background\Road\\road.png").convert_alpha()
road_rect = road.get_rect(midbottom = (0, 420))

endcard = pygame.image.load("Menu\Cards\end-card.jpg").convert()  

home_button = hb = pygame.image.load("Menu\Button Images\Home-Button.png").convert_alpha()
home_button_dark = pygame.image.load("Menu\Button Images\Home-Button_dark.png").convert_alpha()
home_button_rect = home_button.get_rect(midbottom = (318,352))

restart_button = rb = pygame.image.load("Menu\Button Images\\restart-button.png").convert_alpha()
restart_button_dark = pygame.image.load("Menu\Button Images\\restart-button_dark.png").convert_alpha()
restart_button_rect = restart_button.get_rect(midbottom = (498, 352))

cac = pygame.image.load("Obstacles\cactile.png").convert_alpha()
# cac = pygame.transform.scale(cac, (52,88))
cac_rect = cac.get_rect(midbottom = (800,324))

cac2 = pygame.image.load("Obstacles\obstacle2.png").convert_alpha()
cac2_rect = cac2.get_rect(midbottom = (800, 324))

cac3 = pygame.image.load("Obstacles\obstacle1.png").convert_alpha()
cac3_rect = cac3.get_rect(midbottom = (800, 324))
 
cac4 = pygame.image.load("Obstacles\obstacle3.png").convert_alpha()
cac4_rect = cac4.get_rect(midbottom = (800, 324))

cac5 = pygame.image.load("Obstacles\obstacle4.png").convert_alpha()
cac5_rect = cac5.get_rect(midbottom = (800, 324))

mashroom = pygame.image.load("Obstacles\obstacle5.png").convert_alpha()
mashroom_rect = mashroom.get_rect(midbottom = (800, 338))

# initializing obstacle...................................................
obstacle = cac
obstacle_rect = cac_rect


# starting menu ..........................................................
menu_bg = pygame.image.load("Menu\Cards\Opening-card.jpg").convert_alpha()

player1 = p1 = pygame.image.load("Menu\Player Selection Images\player1_selection.png").convert_alpha()
player1_rect = player1.get_rect(midbottom = (100,330))
player1_darken = pygame.image.load("Menu\Player Selection Images\player1_selection_dark.png").convert_alpha()

player2 = p2 = pygame.image.load("Menu\Player Selection Images\player2_selection.png").convert_alpha()
player2_rect = player2.get_rect(midbottom = (300,330))
player2_darken = pygame.image.load("Menu\Player Selection Images\player2_selection_dark.png").convert_alpha()

player3 = p3 = pygame.image.load("Menu\Player Selection Images\player3_selection.png").convert_alpha()
player3_rect = player3.get_rect(midbottom = (500,330))
player3_darken = pygame.image.load("Menu\Player Selection Images\player3_selection_dark.png").convert_alpha()

player4 = p4 = pygame.image.load("Menu\Player Selection Images\player4_selection.png").convert_alpha()
player4_rect = player4.get_rect(midbottom = (700,330))
player4_darken = pygame.image.load("Menu\Player Selection Images\player4_selection_dark.png").convert_alpha()



font = pygame.font.Font("Fonts\WoodlistRegular.ttf", 40)
end_font = pygame.font.Font("Fonts\DUSTY Muffin.ttf", 55)

c3 = font.render("3", "FORTE.TTF", (255, 255, 255))
c3_rect = c3.get_rect(midbottom = (400,200))


# rabbit image in list for running
rabbit_list = sprite_cutout(8, "sprites\Bunny\\rabbit")
rabbit_index = 0
rabbit_run = rabbit_list[rabbit_index]
rabbit_rect = rabbit_run.get_rect(midbottom = (200, 312))

# dinasour image in list for running
dinasour_list = sprite_cutout(8, "sprites\Dinasour\Run")
dinasour_index = 0
dinasour_run = dinasour_list[dinasour_index]
dinasour_rect = dinasour_run.get_rect(midbottom = (200, 338))

# fox image in list for running
fox_list = sprite_cutout(9, "sprites\\Fox\\fox")
fox_index = 0
fox_run = fox_list[fox_index]
fox_rect = fox_run.get_rect(midbottom = (200, 325))

# ninja image in list for running
ninja_list = sprite_cutout(10, "sprites\\Ninja\Run") 
ninja_index = 0
ninja_run = ninja_list[ninja_index]
ninja_rect = ninja_run.get_rect(midbottom = (200, 328))

# initialize
dinasour_gravity = 0
rabbit_gravity = 0
fox_gravity = 0
ninja_gravity = 0

bg_x = 0
sky_x = 0
copy_bg_x = 0
copy_bg_x_2 = 0
start_time = 0 
fade_position = 3 # increasing it will delay the new bg's || Multiplying distances


clock = pygame.time.Clock()
menu = True
running = False
game_active = True

active = True

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #game quit 
            active = False
    

# menu ----------------------------------------------------------------   
    while menu:   # code for menu & player selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #game quit 
                menu = False
                active = False
        
        window.blit(menu_bg, (0,0))
        window.blit(player1, player1_rect)
        window.blit(player2, player2_rect)
        window.blit(player3, player3_rect)
        window.blit(player4, player4_rect)
        

        # player selection ----------------------------------------------
        mouse_pos = pygame.mouse.get_pos()
        if player1_rect.collidepoint(mouse_pos):
            player1 = player1_darken
            if pygame.mouse.get_pressed()[0]:
                start_time = int(pygame.time.get_ticks()/200)
                # countdown()
                selection_sound.play()
                pygame.time.delay(200)
                environment_speed = 1
                obstacle = cac   # change obs
                obstacle_rect.x = 800 # so it doesn't colide immediately
                road_rect.x = 0
                ninja_gravity = 0
                ninja_rect.bottom = 328
                bg = bg1 # change bg
                bg_x = 0
                copy_bg_x = 0
                copy_bg_x_2 = 0
                character_no = 1
                menu = False          
                running = True
                game_active = True
        else: 
            player1 = p1
        
        if player2_rect.collidepoint(mouse_pos):
            player2 = player2_darken
            if pygame.mouse.get_pressed()[0]:
                start_time = int(pygame.time.get_ticks()/200)
                selection_sound.play()
                pygame.time.delay(200)
                environment_speed = 1
                fox_gravity = 0
                fox_rect.bottom = 325
                obstacle = cac
                obstacle_rect.x = 800 # so it doesn't colide immediately
                road_rect.x = 0
                bg = bg1
                bg_x = 0
                copy_bg_x = 0
                copy_bg_x_2 = 0
                character_no = 2
                menu = False
                running = True
                game_active = True
        else: 
            player2 = p2

        if player3_rect.collidepoint(mouse_pos):
            player3 = player3_darken
            if pygame.mouse.get_pressed()[0]:
                start_time = int(pygame.time.get_ticks()/200)
                selection_sound.play()
                pygame.time.delay(200)
                environment_speed = 1
                obstacle = cac
                obstacle_rect.x = 800 # so it doesn't colide immediately
                road_rect.x = 0
                dinasour_gravity = 0
                dinasour_rect.bottom = 338
                bg = bg1
                bg_x = 0
                copy_bg_x = 0
                copy_bg_x_2 = 0
                character_no = 3
                menu = False
                running = True
                game_active = True
        else: 
            player3 = p3

        if player4_rect.collidepoint(mouse_pos):
            player4 = player4_darken
            if pygame.mouse.get_pressed()[0]:
                start_time = int(pygame.time.get_ticks()/200)
                selection_sound.play()
                pygame.time.delay(200)
                environment_speed = 1
                obstacle = cac
                obstacle_rect.x = 800 # so it doesn't colide immediately
                road_rect.x = 0
                rabbit_gravity = 0
                rabbit_rect.bottom = 312
                bg = bg1
                bg_x = 0
                copy_bg_x = 0
                copy_bg_x_2 = 0
                character_no = 4
                menu = False
                running = True
                game_active = True
        else: 
            player4 = p4
    
        #---------------------------------------------------------------

        clock.tick(30)
        pygame.display.update()
            

# game play code -------------------------------------------------------
    while running:   # code for main game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #game quit 
                running = False
                active = False

            if game_active: # if game active and space pressed then gravity is initialized(jumped)
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_h)  and (character_rect.bottom >= character_bottom):  # add up arrow K_UP
                        jump_sound.play()
                        dinasour_gravity = -20
                        rabbit_gravity = -20
                        fox_gravity = -20
                        ninja_gravity = -20

            else: # if showing end card ................................
                mouse_pos_endcard = pygame.mouse.get_pos()
                if home_button_rect.collidepoint(mouse_pos_endcard):
                    home_button = home_button_dark
                    if pygame.mouse.get_pressed()[0]:
                        selection_sound.play()
                        menu = True
                        running = False
                        pygame.time.delay(200)                        
                else:
                    home_button = hb
                
                # Restart Button ........................................
                if restart_button_rect.collidepoint(mouse_pos_endcard):
                    restart_button = restart_button_dark
                    if pygame.mouse.get_pressed()[0]:
                        selection_sound.play()
                        pygame.time.delay(200)
                        game_active = True
                        environment_speed = 1
                        obstacle = cac
                        obstacle_rect.x = 800 # so it doesn't colide immediately
                        road_rect.x = 0
                        ninja_gravity = 0
                        ninja_rect.bottom = 328
                        fox_gravity = 0
                        fox_rect.bottom = 325
                        dinasour_gravity = 0
                        dinasour_rect.bottom = 338
                        rabbit_gravity = 0
                        rabbit_rect.bottom = 312 
                        bg = bg1 # change bg
                        bg_x = 0 
                        copy_bg_x = 0
                        copy_bg_x_2 = 0
                        start_time = int(pygame.time.get_ticks()/200)   
                else:
                    restart_button = rb
                    

        if game_active:
            
            # Placing game elements on screen .............................
            window.blit(sky, (sky_x,0))
            window.blit(sky, (sky_x+800,0))
            window.blit(bg, (bg_x,0))
            window.blit(bg, (bg_x+1400, 0))
            window.blit(fade_bg, (copy_bg_x+1400*fade_position, 0))  # change bg
            window.blit(fade_bg_2, (copy_bg_x_2+1400*fade_position*2, 0)) # change bg
            window.blit(road, road_rect)
            window.blit(road, (road_rect.x+W, road_rect.y))
            window.blit(obstacle, obstacle_rect)
            # ..............................................................


            game_score() # calling game score function.....................
            

            # game speed increment relative to score ......................
            if final_score%50 == 0:
                environment_speed += .03
            # .............................................................
            

            # character animation call ------------------------------------
            if character_no == 1:
                ninja_animation()
                window.blit(ninja_run, ninja_rect)
                character_rect = ninja_rect
                character_bottom = 328
                ninja_gravity += 1
                ninja_rect.y += ninja_gravity
                if ninja_rect.bottom >= 328:
                    ninja_rect.bottom = 328
            elif character_no == 2:
                fox_animation()
                window.blit(fox_run, fox_rect)
                character_rect = fox_rect
                character_bottom = 325
                fox_gravity += 1
                fox_rect.y += fox_gravity
                if fox_rect.bottom >= 325:
                    fox_rect.bottom = 325
            elif character_no == 3:
                dinasour_animation()
                window.blit(dinasour_run, dinasour_rect)
                character_rect = dinasour_rect
                character_bottom = 338
                dinasour_gravity += 1
                dinasour_rect.y += dinasour_gravity
                if dinasour_rect.bottom >= 338:
                    dinasour_rect.bottom = 338
            else:
                rabbit_animation()
                window.blit(rabbit_run, rabbit_rect)
                character_rect = rabbit_rect
                character_bottom = 312
                rabbit_gravity += 1
                rabbit_rect.y += rabbit_gravity
                if rabbit_rect.bottom >= 312:
                    rabbit_rect.bottom = 312
            # --------------------------------------------------------------



            # ---------------------
            fade_1 = True # change bg
            fade_2 = True # change bg
            # background fade ---------------------------------------------------------------------
            if copy_bg_x > -(fade_position*1400+1400):
                copy_bg_x -= 4 * environment_speed
            if copy_bg_x < -(fade_position*1400-800+1400) and fade_1 == True: # -2000 till -3400 
                bg = bg2
                fade_1 = False
            if copy_bg_x_2 > -(fade_position*2*1400+1400):
                copy_bg_x_2 -= 4 * environment_speed
            if copy_bg_x_2 < -(fade_position*2*1400-800+1400) and fade_2 == True: # -2000 till -3400 
                bg = bg3
                fade_2 = False
            # ---------------------------------------------------------------------------------------


            # Obstacle change -----------------------------------------
            if obstacle_rect.x < -5:
                if final_score>50 and final_score<70 :
                    obstacle = cac2
                    obstacle_rect = cac2_rect
                elif final_score>100 and final_score<130 :
                    obstacle = cac3
                    obstacle_rect = cac3_rect
                elif final_score>150 and final_score<200 :
                    obstacle = cac4
                    obstacle_rect = cac4_rect
                elif final_score>300 and final_score<400 :
                    obstacle = mashroom
                    obstacle_rect = mashroom_rect
                elif final_score>500 and final_score<700 :
                    obstacle = cac5
                    obstacle_rect = cac5_rect
                else:
                    obstacle = cac # change obs
                    obstacle_rect = cac_rect # change obs
            # -----------------------------------------------------------


            # game elements movement ------------------------------------
            bg_x -= 4 * environment_speed
            if bg_x < -1400:
                bg_x = 0

            sky_x -= 2 * environment_speed
            if sky_x < -800:
                sky_x = 0

            road_rect.x -= 10 * environment_speed
            if road_rect.right <= 0:
                road_rect.x = 0

            obstacle_rect.x -= 10 * environment_speed
            if obstacle_rect.right <= 0:
                obstacle_rect.x = 800
            #------------------------------------------------------------
            

            # collision -------------------------------------------------------------------
            if character_rect.colliderect(obstacle_rect):
                crash_sound.play()
                game_active = False
            #------------------------------------------------------------------------------

        else: # if crashed, shows end card and final score
            window.blit(endcard, (0,0))
            window.blit(home_button, home_button_rect)
            window.blit(restart_button, restart_button_rect)
            final_score_endcard()

        clock.tick(30)
        pygame.display.update()