import pygame.image as image
import paths


levels = {
0: [[1,-1,-1,-1,-1,-1,-1,-1,-1,-1]],
1: [[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]],

2: [[1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]],

3: [[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]],


4:[[-1,-1,-1,-1,1,-1,-1,-1,-1,-1],[-1,-1,-1,1,-1,1,-1,-1,-1,-1],[-1,-1,1,-1,-1,-1,1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1,1,-1,-1],[-1,1,-1,-1,-1,-1,-1,1,-1,-1],[-1,-1,1,-1,-1,-1,1,-1,-1,-1],[-1,-1,-1,1,-1,1,-1,-1,-1,-1],[-1,-1,-1,-1,1,-1,-1,-1,-1,-1]]



}



red_brick = image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/tiles/red.png')
yellow_brick= image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/tiles/yellow.png')
blue_brick= image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/tiles/blue.png')
black_brick= image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/tiles/black.png')
green_brick= image.load(paths.cwd+'/BrickBreaker/Pics/Breakout Tile Set Free/tiles/green.png')


level_bricks=[[red_brick],[red_brick,blue_brick,yellow_brick], [red_brick,blue_brick,yellow_brick,black_brick,green_brick],

[black_brick,blue_brick,yellow_brick,0,0,0,yellow_brick,blue_brick,red_brick],
  [red_brick,blue_brick,yellow_brick,black_brick,black_brick,yellow_brick,blue_brick,red_brick] ]

bricks_w=red_brick.get_width()
bricks_h=red_brick.get_height()

no_of_bricks= {0:1,1:30,2:30,3:60,4:14}

level_scores={0:[0],1:[15,10,5],2:[25,20,15,10,5],3:[30,25,20,0,0,0,15,10,5],4:[35,30,25,20,15,10,5,5]}

level_y_start= {0:100,1:100,2:300,3:100,4:100}






