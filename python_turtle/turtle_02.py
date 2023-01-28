import turtle
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

def g_line(x1, y1, x2, y2, pencolor = 'black'):
	global my_turtle; t = my_turtle
	t.pencolor(pencolor)
	t.up()
	t.goto(x1, y1)
	t.down()
	t.goto(x2, y2)

def first(): #設定
	global paper, my_turtle
	paper = turtle.Screen() #paper 建立紙
	paper.setup(500, 400) # 紙大小
	my_turtle = turtle.Turtle()   # 建立一隻烏龜
	my_turtle.speed('fastest')
	my_turtle.width(2)

def test1():
	first()
	g_line(0,0, 100,50, 'red') # 畫線
	g_circle(10,10,30,'black','red') # 畫圓
	paper.exitonclick() #按一下才離
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
	my_turtle.up()
	my_turtle.goto(-250,-200)
	paper.exitonclick() #按一下才離

test2()
