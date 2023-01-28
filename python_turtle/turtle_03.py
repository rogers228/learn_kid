import turtle
import math
my_turtle = None
paper = None

def g_circle(x, y, r,
		pencolor = 'black',fillcolor = 'white'): #以圓心座標畫圓
	global my_turtle; t = my_turtle
	t.pencolor(pencolor)
	t.up()
	t.goto(x, y-r)
	t.down()
	t.setheading(0)
	t.fillcolor(fillcolor)
	t.begin_fill() # 開始填充
	t.circle(r)
	t.end_fill() # 結束填充

def g_arc(x, y, r, start_angle, arc_angle,
		pencolor = 'black',fillcolor = 'white'): #畫圓弧
	global my_turtle; t = my_turtle
	t.pencolor(pencolor) # 筆的顏色
	t.up()
	t.goto(x, y)
	t.down()
	t.setheading(start_angle) # 起始角度
	t.fillcolor(fillcolor) #填充色
	t.begin_fill() # 開始填充
	t.circle(r, arc_angle) #圓弧角度
	t.end_fill() # 結束填充

def g_line(x1, y1, x2, y2, pencolor = 'black'):
	global my_turtle; t = my_turtle
	t.pencolor(pencolor)
	t.up()
	t.goto(x1, y1)
	t.down()
	t.goto(x2, y2)

def draw_semicircle( # 畫半圓
    x, y, lenght, radius_ratio, rotation = 'r', angle = 0, pen_color = 'black', fill_color = None):
    '''
        x, y:       起始點絕對座標
        lenght:     邊長度
        radius_ratio 半徑比例 0.1~1 (1等同半徑等同長度的一半)
        height:     半圓高度
        height:     半圓高度 與半徑的筆
        rotation:   畫圓方向 r順時針 l逆時針
        angle:      起始絕對角度
        pen_color:  筆顏色
        fill_color: 填充顏色
        '''
    a = lenght/2
    if radius_ratio < 0.1:
        radius_ratio = 0.1
    if radius_ratio > 1:
        radius_ratio = 1
    height = radius_ratio*(lenght/2) # 半圓高度
    r = (a**2 + height**2)/(2*height) # 半徑
    angle_g= math.degrees(math.acos(a/r)) # 角度
    angle_all= 2*(90-math.degrees(math.acos(a/r))) # 整體角度

    t = my_turtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle) # angle
    t.begin_fill()
    t.forward(lenght)
    if rotation == 'l': # l逆時針
        t.right(90 + angle_g)
        t.circle(-r, angle_all)
    else: # r順時針
        t.left(90 + angle_g) 
        t.circle(r, angle_all)
    t.end_fill()

def first(): #設定
	global paper, my_turtle
	paper = turtle.Screen() #paper 建立紙
	paper.setup(500, 400) # 紙大小
	my_turtle = turtle.Turtle()   # 建立一隻烏龜
	my_turtle.speed('fastest') # fastest
	my_turtle.width(2)

def test2():
	first()
	#g_circle(0,0,10,'black','black') # 畫圓
	g_circle(0,80,80,'black','blue') # 畫圓
	g_circle(25,105,20,'black','white') # 畫圓
	g_circle(-25,105,20,'black','white') # 畫圓
	g_circle(0,80,7,'black','red') # 畫圓
	g_circle(27,107,5,'black','black') # 畫圓
	g_circle(-27,107,5,'black','black') # 畫圓
	g_line(20,65,85,85)
	g_line(0,80,0,10)
	draw_semicircle(-50,-50,100,0.5,'l',0,'black','white')
	draw_semicircle(-50,-10,100,0.5,'l',0,'black','red')


	my_turtle.up()
	my_turtle.goto(-250,-200)
	paper.exitonclick() #按一下才離

test2()
