import turtle
t = turtle.Turtle() 
turtle.bgcolor("black") 
              

screen = turtle.Screen()
t.pensize(4)
graphic_size = 95                           
n = 16                                     
def pattern():                              
    t.pencolor("orange")                    
    t.circle(0.5 * graphic_size, 90)        
    t.pencolor("blue")                     
    t.circle(-graphic_size, 90)             
    t.right(180)                            
    t.circle(0.5 * graphic_size, 90)        
    t.pencolor("orange")                    
    t.circle(-graphic_size, 90)             
t.penup()                           
t.forward(0.5 * graphic_size)               
t.right(45)                                 
t.pendown()                                 
for i in range(n):                         
    pattern()                               
    t.pencolor("blue")                    
    t.circle(0.5 * graphic_size, 360 / n)  
    t.right(135)
t.hideturtle()
screen.exitonclick()