
import pygame 
import Bricks
import copy
import random
import powers
import paths

pygame.init() 
  
level=1
WHITE = (255, 255, 255) 
BLACK= (0,0,0)

score=0

  
game_started=False

ballmvx=2
ballmvy=10

ball_img= pygame.image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/PNG/ball2.png')
bat_img = pygame.image.load(paths.cwd+'/BrickBreaker/Pics/bat2.png')
lives_img=pygame.image.load(paths.cwd+'/BrickBreaker/Pics/bat.png')
bricks=copy.deepcopy(Bricks.levels[level])
#bricks.extend(Bricks.levels[level])

rows= len(bricks)
bricks_color= Bricks.level_bricks[level]
brw= bricks_color[0].get_width()
allbw=(brw*10)+(len(bricks[0])-1)
total_bricks= Bricks.no_of_bricks[level]
players_left=4



powers_present=[]

gaps_between_powers=[6,5,4,3,2,1]

get_power_after=gaps_between_powers[random.randrange(0,len(gaps_between_powers))]
fire_ball=False
magnet = False




class Bat_Segment(pygame.sprite.Sprite):
    """ Class to represent Bat. """
    
    def __init__(self, x, y):
        
        super().__init__()
 
        
        self.image= bat_img
       
        
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center=[x,y]
        self.wd= self.image.get_width()
        self.hg=self.image.get_height()
        
        



class Ball_Segment(pygame.sprite.Sprite):
    """ Class to represent Ball. """
    
    def __init__(self, x, y):
        super().__init__()
        self.image= ball_img
        #self.image.set_colorkey(BLACK)
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center=[x,y]
        self.wd= self.image.get_width()
        self.hg=self.image.get_height()





class Bricks_Segment(pygame.sprite.Sprite):
    """ Class to represent Bricks. """
    def __init__(self,x,y,img):
        super().__init__()
        self.image=img
        self.image.set_colorkey(BLACK)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft=[x,y]
                




class Lives_Segment(pygame.sprite.Sprite):
    """Class to represent lives"""
    def __init__(self,x,y,img):
        super().__init__()
        self.image=img
        self.rect =self.image.get_rect()
        self.rect.topleft=[x,y]

class Power_Segment(pygame.sprite.Sprite):
    """Class to represent powers"""
    def __init__(self,x,y,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.topleft=[x,y]


display_surface = pygame.display.set_mode((0,0 ),pygame.FULLSCREEN) 
  

pygame.display.set_caption('Arkanoid') 
  
images=[paths.cwd+'/BrickBreaker/Pics/space.jpg',paths.cwd+'/BrickBreaker/Pics/background2.png',paths.cwd+'/BrickBreaker/Pics/background3.jpg',paths.cwd+'/BrickBreaker/Pics/background4.jpg']

image = pygame.image.load(images[random.randrange(0,4)]) 

w, h = pygame.display.get_surface().get_size()


allspriteslist = pygame.sprite.Group()

wid=bat_img.get_width()
hie= bat_img.get_height()
ballw=ball_img.get_width()
ballh=ball_img.get_height()

coords=[w/2,h-25]
bcoords= [coords[0],coords[1]-ballh/2-hie/2]

tcoords=[w/2,h-25]
tbcoords=[tcoords[0],tcoords[1]-ballh/2-hie/2]



live_x=10
live_y=h-10


clock = pygame.time.Clock()
background_change, for_every= pygame.USEREVENT+1,70000
power_stays=pygame.USEREVENT+2
pygame.time.set_timer(background_change,for_every)
bat_power_stays=pygame.USEREVENT+3

allspriteslist.draw(display_surface)



font = pygame.font.Font('freesansbold.ttf', 32) 
font2=pygame.font.Font('freesansbold.ttf', 12)
  
green=(60, 255, 70)
red=(255, 41, 0)
blue=(0, 181, 249)

text_level = font.render('LEVEL COMPLETED', True, WHITE, BLACK) 
text_gameover=font.render('GAME OVER', True, red, blue) 

  

textRect_level = text_level.get_rect()  
textRect_gameover=text_gameover.get_rect()

  

textRect_level.center=(w // 2, h // 2) 
textRect_gameover.center=(w//2,h//2)




def keys_press(keys,wd,hg):
    
    global game_started
    
  
    if(keys[pygame.K_RIGHT]):
        if(coords[0]+ (wd/2) < (w-2)):
            coords[0] = coords[0]+10
            if game_started== False:
                bcoords[0]=coords[0]
                bcoords[1]=coords[1]-ballh/2-hie/2
                

    if(keys[pygame.K_LEFT]):
        if(coords[0]- (wd/2) > 2):
            coords[0] = coords[0]-10
            if game_started == False:
                bcoords[0]=coords[0]
                bcoords[1]=coords[1]-ballh/2-hie/2
   
    

def life_lost():
    global game_started
    global coords
    global bcoords
    global ballmvy
    global ballmvx
    global bat_img
    global fire_ball
    global magnet
    global wid,hie
    ballmvx=2
    game_started=False
    ballmvy=-ballmvy
    coords.clear()
    bcoords.clear()
    coords.extend(tcoords)
    bcoords.extend(tbcoords)
    ballmvy=10
    bat_img=pygame.image.load(paths.cwd+'/BrickBreaker/Pics/bat2.png')
    fire_ball=False
    magnet= False
    wid=bat_img.get_width()
    hie=bat_img.get_height()

def ball_movement():
    global ballmvx
    global ballmvy 
    global players_left
    if(game_started == True):
        bcoords[0]= bcoords[0]+ballmvx;
        bcoords[1]=bcoords[1]-ballmvy;

        if(bcoords[0] > (w-2) or bcoords[0] < 2):
            ballmvx=-ballmvx
        if(bcoords[1] < 4):
            ballmvy= -ballmvy
        if bcoords[1] >= coords[1]:
            players_left=players_left-1
            life_lost()

   
diffbr=w-allbw
strtp=diffbr/2
bx=strtp
by=Bricks.level_y_start[level]
coll_begin= rows * Bricks.bricks_h + by


def side_check(j,bricks,i=None,fbricks=None):
    global ballmvx
    global ballmvy
    if(ballmvx<0):
        
        if(j!=len(bricks)-1 and bricks[j+1]==-1):
            
            ballmvx=-ballmvx
        elif j==len(bricks)-1:
            
            ballmvx=-ballmvx
        else:
            
            ballmvy=-ballmvy
            #top_bottom(i,j,fbricks)
    elif(ballmvx >0):
        
        if(j!=0 and bricks[j-1]==-1):
            
            ballmvx=-ballmvx
        elif j==0:
            
            ballmvx=-ballmvx
            
        else:
            
            ballmvy=-ballmvy
            #top_bottom(i,j,fbricks)



ind=0
def collision_detection():
    global ballmvx
    global ballmvy
    global total_bricks
    global players_left
    global score
    global get_power_after
    global game_started    
    global ind
    brx=bx
    bry=by
    parts =list(range(0,wid+wid//5,wid//5))
    ball_rect=pygame.Rect(bcoords[0]-ballw/2,bcoords[1]-ballh/2,ballw,ballh)
    bat_rect=pygame.Rect(coords[0]-wid/2,coords[1]-hie/2,wid,hie)
    
    
    if game_started == True:
        if(magnet == True and ball_rect.colliderect(bat_rect)):
                game_started=False
        if(bcoords[1]+ ballh/2) >= coords[1]-hie/2:
            
            if bcoords[0] == coords[0]-wid/2 :
                ballmvy = -ballmvy
                ballmvx= -8
            elif bcoords[0] == coords[0]+wid/2:
                ballmvy = -ballmvy
                ballmvx=8
            elif bcoords[0] > (coords[0] - wid/2) and bcoords[0] < (coords[0]-wid/2)+parts[1]:
                ballmvy = -ballmvy
                ballmvx=-6

            elif bcoords[0] > (coords[0] - wid/2)+parts[1] and bcoords[0] < (coords[0]-wid/2)+parts[2]:
                ballmvy = -ballmvy
                ballmvx=-4

            elif bcoords[0] > (coords[0] - wid/2)+parts[2] and bcoords[0] < (coords[0]):
                ballmvy = -ballmvy
                ballmvx=-2
                
                
            elif bcoords[0] > (coords[0]+wid/2) -parts[1] and bcoords[0]< (coords[0]+wid/2):
                ballmvy = -ballmvy
                ballmvx=6
                

            elif bcoords[0] > (coords[0]+wid/2)-parts[2] and bcoords[0]< (coords[0]+wid/2)-parts[1]:
                ballmvy = -ballmvy
                ballmvx=4
            elif bcoords[0] > coords[0] and bcoords[0]< (coords[0]+wid/2)-parts[2]:
                ballmvy = -ballmvy
                ballmvx=2
            elif bcoords[0] == coords[0]:
                ballmvy=-ballmvy
                
            
            
        
        
        if(bcoords[1] <= coll_begin):
            #
            for i in range(rows):
                
                for j in range(len(bricks[i])):
                    
                    if(bricks[i][j]==1):
                        
                        
                        brick_rect=  pygame.Rect(brx,bry,Bricks.bricks_w,Bricks.bricks_h)

                        #abs((bcoords[0]+ballw/2) - brx)<6.6 or abs((bcoords[0]-ballw/2) - (brx+Bricks.bricks_w))<6.6

                        if(brick_rect.colliderect(ball_rect)):
                            if(fire_ball==False):
                                if(ballmvy >0 and (bcoords[1] <= bry+Bricks.bricks_h and bcoords[1] >=bry)):

                                    if(ballmvx >0 and abs((bcoords[0]+ballw/2) - brx)<6.6 ):
                                        side_check(j,bricks[i],i,bricks)


                                    elif(ballmvx <0 and abs((bcoords[0]-ballw/2)-(brx+Bricks.bricks_w)) < 6.6):
                                        side_check(j,bricks[i],i,bricks)
                                        
                                    else:

                                        ballmvy=-ballmvy
                                        #top_bottom(i,j,bricks)
                                    ind=1
                                    
                                elif(ballmvy < 0 and( bcoords[1] >=bry and bcoords[1] <=bry+Bricks.bricks_h)): 

                                    if(ballmvx >0 and abs((bcoords[0]+ballw/2) - brx)<6.6 ):
                                        side_check(j,bricks[i],i,bricks)


                                    elif(ballmvx <0 and abs((bcoords[0]-ballw/2)-(brx+Bricks.bricks_w)) < 6.6):
                                        side_check(j,bricks[i],i,bricks)

                                    else:
 
                                        
                                        ballmvy=-ballmvy
                                       #top_bottom(i,j,bricks)
                                    ind=1 
                                    
                                else:

                                    if(ind==0):
                                        
                                        ballmvy=-ballmvy
                                        
                                        
                                        
                                        break
                                    else:
                                        break
                                    
                                    
                            
                            get_power_after=get_power_after-1
                            bricks[i][j]=-1
                            check_and_add_power(brx,bry)
                            total_bricks=total_bricks-1
                            score=score+Bricks.level_scores[level][i]
                            break
                        
                                
                    brx=brx+Bricks.bricks_w
                bry=bry+Bricks.bricks_h
                brx=bx
                            
                        
                
        brx=bx
        bry=by

def check_and_add_power(x,y):
    global powers_present
    global get_power_after
    if(get_power_after == 0):
        powers_present.append([x,y,powers.powers[random.randrange(0,len(powers.powers))]])
        get_power_after=gaps_between_powers[random.randrange(0,len(gaps_between_powers))]


def bricks_draw():
    global bx
    global by

    for i in range(rows):
        for j in bricks[i]:
            if(j == 1):
                brk =Bricks_Segment(bx,by,bricks_color[i])
                display_surface.blit(brk.image,brk.rect)
            bx=bx+Bricks.bricks_w
            

        by=by+Bricks.bricks_h
        bx=strtp   
    bx=strtp
    by=Bricks.level_y_start[level]     


def reset(lvl=1):
    global level
    global bricks                 
    global rows                   
    global bricks_color                                
    global allbw                
    global total_bricks           
    global players_left            


    global diffbr                 
    global strtp                  
    global bx                     
    global by                     
    global coll_begin     
    global coords
    global bcoords
    global game_started      
    global ballmvy
    global ballmvx  
    global powers_present
    global get_powers_after
    global bat_img
    global fire_ball
    global magnet
    global wid,hie
    level=lvl
    bricks=copy.deepcopy(Bricks.levels[level])
    rows= len(bricks)
    bricks_color= Bricks.level_bricks[level]
    brw= bricks_color[0].get_width()
    allbw=(brw*10)+(len(bricks[0])-1)
    total_bricks= Bricks.no_of_bricks[level]
    diffbr=w-allbw
    strtp=diffbr/2
    bx=strtp
    by=Bricks.level_y_start[level]
    coll_begin= rows * Bricks.bricks_h + by
    game_started=False
        
    coords.clear()
    bcoords.clear()
    coords.extend(tcoords)
    bcoords.extend(tbcoords)
    powers_present=[]
    get_power_after=gaps_between_powers[random.randrange(0,len(gaps_between_powers))]
    ballmvy=10
    ballmvx=2
    bat_img=pygame.image.load(paths.cwd+'/BrickBreaker/Pics/bat2.png')
    fire_ball=False
    magnet= False
    wid=bat_img.get_width()
    hie=bat_img.get_height()
    
    

def level_completed():
    global level
     

    write_text("Level "+str(level),x=w/2,y=20)
    if(total_bricks==0 and players_left>0):
        
        display_surface.blit(text_level, textRect_level) 
        
        
        level=level+1
        bricks.clear()
        reset(level)
        
        
        return 0

    return 1
        
        
        

def game_over():
    global players_left
    global bricks
    if(players_left==0):
        display_surface.blit(text_gameover,textRect_gameover)
        players_left=4
        bricks.clear()
        reset()
        
        


    
def count_lives():
    

    write_text('x'+str(players_left),x=live_x+60,y=live_y,center=True)

def write_score():
    
    write_text(text=str(score),x=w-112,y=20)

def write_text(text,font_name='freesansbold.ttf',size=14,color=WHITE,x=0,y=0,center=False):
    font=pygame.font.Font(font_name, size) 
    text=font.render(text,True,color)
    text_rect=text.get_rect()
    if(center== False):
        text_rect.topleft=(x,y)
    else:
        text_rect.center=(x,y)
    display_surface.blit(text,text_rect)


def draw_powers():
    global powers_present
    
    popped=[]
    bat_rect=pygame.Rect(coords[0]-wid/2,coords[1]-hie/2,wid,hie)
    if(len(powers_present)!=0):
        for cords in range(len(powers_present)):
                pw=Power_Segment(powers_present[cords][0],powers_present[cords][1],powers_present[cords][2])
                display_surface.blit(pw.image,pw.rect)
                powers_present[cords][1] += 5
                
                if(bat_rect.colliderect(pw.rect)):
                    powers_present[cords][1] =- 1
                    popped.append(cords)
                    give_powers(powers_present[cords][2])
                if(powers_present[cords][1] > coords[1]+hie/2+1):
                    popped.append(cords)
        for rem in popped:
            powers_present.pop(rem)
                

def give_powers(power):
    global players_left
    global bat_img
    global ballmvy
    global fire_ball
    global magnet
    global wid,hie
    if power == powers.powers[0]:
        bat_img=pygame.image.load(powers.big_bat_pow)  
        wid=bat_img.get_width()
        hie=bat_img.get_height()      
        
    elif power == powers.powers[1]:
        pygame.time.set_timer(power_stays,10000)
        fire_ball=True

    elif power == powers.powers[2]:
        pygame.time.set_timer(power_stays,30000)
        if(ballmvy <0):
            ballmvy=-15
        else:
            ballmvy=15
        

    elif power == powers.powers[3]:
        pygame.time.set_timer(power_stays,15000)
        if(ballmvy <0):
            ballmvy=-6
        else:
            ballmvy=6

    elif power == powers.powers[4]:
        bat_img=pygame.image.load(powers.small_bat_pow) 
        wid=bat_img.get_width()
        hie=bat_img.get_height()       


    elif power == powers.powers[5]:
        players_left=players_left+1

    elif power == powers.powers[6]:
        pygame.time.set_timer(bat_power_stays,40000)
        bat_img=pygame.image.load(powers.magnet_bat_pow)
        wid=bat_img.get_width()
        hie=bat_img.get_height()
        magnet=True

def event_handling(event):
    global ballmvy
    global game_started
    global fire_ball
    global bat_img
    global magnet
    global wid,hie
    global image
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key==pygame.K_SPACE:
                
                if(game_started==False):
           
                    game_started=True
                else:
                    game_started=False
            
    if event.type == background_change:
            image=pygame.image.load(images[random.randrange(0,4)])   
            pygame.time.set_timer(background_change,for_every)  
    if event.type == power_stays:
            if(ballmvy<0):
                ballmvy=-10
            else:
                ballmvy=10    
            fire_ball=False    
    if event.type == bat_power_stays:
            if magnet==True:
                bat_img=pygame.image.load(paths.cwd+'/BrickBreaker/Pics/bat2.png')
                wid=bat_img.get_width()
                hie=bat_img.get_height()
                magnet=False
     
    if event.type == pygame.QUIT : 
  
           
            pygame.quit() 
  
            
            quit() 


while True : 
    

    display_surface.fill(WHITE) 
  
    
    display_surface.blit(image, (0, 0)) 

    bat= Bat_Segment(coords[0],coords[1])
    display_surface.blit(bat.image,bat.rect)
    
       
    
    
    ball= Ball_Segment(bcoords[0],bcoords[1])
    display_surface.blit(ball.image,ball.rect)
    
    
    
    lives= Lives_Segment(live_x,live_y,lives_img)
    display_surface.blit(lives.image,lives.rect)

    count_lives()
    write_score()
    bricks_draw()
   
    
    keys= pygame.key.get_pressed()
          
    keys_press(keys,wid,hie)
    ball_movement()
    collision_detection()
    draw_powers()
    comp=level_completed()

    
    game_over()
    allspriteslist.draw(display_surface)
    for event in pygame.event.get() : 
        event_handling(event)
        
    
    
    pygame.display.flip()
        
 
    
    clock.tick(30)
       
    pygame.display.update()  
    
    if(comp==0):
        pygame.time.delay(1000)
    
  
