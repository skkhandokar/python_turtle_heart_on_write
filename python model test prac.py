
import turtle
from turtle import *
wn=Screen()
wn.bgcolor('black')

t=turtle.Turtle()
#you can choose any color
t.pencolor('yellow')
#you can choose any size
t.pensize(8)
def curve():
    for i in range (200):
        t.rt(1)
        t.fd(1)
col=['red','pink','blue','green','gray']
i=0
def heart():
    t.fillcolor(col[i])
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()
heart()
t.ht()
def write(msg,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    #CHOOSE COLOR OF WRITTING
    t.color('white')
    style=('FF Blur',15,'bold')
    #Stencil Std
    t.write(msg,font=style)
    
 # YOU CAN WRITE ANYTHING 
# write(' ',(-68,95))
# write('S',(-55,95))
# write('K',(-42,95))
# write('K',(-27,95))
# write('H',(-14,95))
# write('A',(10,95))
# write('N',(22,95))
# write('D',(38,95))
# write('O',(38,95))
# write('K',(38,95))
# write('A',(38,95))
# write('R',(38,95))

#bold
write('I',(-92,95))
write('L',(-80,95))
write('O',(-69,95))
write('V',(-54,95))
write('E',(-41,95))
write('M',(-19,95))
write('Y',(-3,95))
write('F',(15,95))
write('R',(27,95))
write('I',(41,95))
write('E',(45,95))
write('N',(58,95))
write('D',(70,95))
write('S',(83,95))
#italic
# write('I',(-92,95))
# write('L',(-80,95))
# write('O',(-70,95))
# write('V',(-56,95))
# write('E',(-43,95))
# write('M',(-21,95))
# write('Y',(-4,95))
# write('F',(14,95))
# write('R',(26,95))
# write('I',(41,95))
# write('E',(45,95))
# write('N',(58,95))
# write('D',(71,95))
# write('S',(83,95))
wn.mainloop()
