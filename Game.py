import turtle as t
import os



player_a_score = 0
player_b_score = 0

win = t.Screen()    
win.title("pong ping")
win.bgcolor('black')    
win.setup(width=800,height=600)  
win.tracer(0)   



key_left = t.Turtle()
key_left.speed(0)
key_left.shape('square')
key_left.color('red')
key_left.shapesize(stretch_wid=5,stretch_len=1)
key_left.penup()
key_left.goto(-350,0)



key_right = t.Turtle()
key_right.speed(0)
key_right.shape('square')
key_right.shapesize(stretch_wid=5,stretch_len=1)
key_right.color('red')
key_right.penup()
key_right.goto(350,0)






pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))




def key_left_up():
    y = key_left.ycor()
    y = y + 15
    key_left.sety(y)



def key_left_down():
    y = key_left.ycor()
    y = y - 15
    key_left.sety(y)



def key_right_up():
    y = key_right.ycor()
    y = y + 15
    key_right.sety(y)



def key_right_down():
    y = key_right.ycor()
    y = y - 15
    key_right.sety(y)



win.listen()
win.onkeypress(key_left_up,"w")
win.onkeypress(key_left_down,"s")
win.onkeypress(key_right_up,"Up")
win.onkeypress(key_right_down,"Down")






while True:
    win.update() 

    


    


        
    
    
        

   



    


    
 
