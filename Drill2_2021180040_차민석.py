from pico2d import*
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
r=0
a=100

while(x<800):
    while(x < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)


    while(x > 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        y=y+3.46
        delay(0.01)

    
    while(x > 200):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        y=y-3.46
        delay(0.01)
    
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)    
    
    while(r < 6):
        x=400-a*math.cos(r)
        y=90+a+a*math.sin(r)
        
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        r=r+0.1
        delay(0.01)  

    r=0


    



