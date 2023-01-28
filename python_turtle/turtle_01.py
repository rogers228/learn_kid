import turtle
def test1():
	paper = turtle.Screen() #paper 建立紙
	paper.setup(500, 400) # 紙大小
	t = turtle.Turtle()   # 叫一隻烏龜
	# 烏龜預設在 0,0 頭向東
	t.forward(150) #前進
	t.left(90) # 想左轉
	t.forward(75) #前進
	paper.exitonclick() #按一下才離

def test2():
	paper = turtle.Screen() #paper 建立紙
	paper.setup(500, 400) # 紙大小
	t = turtle.Turtle()   # 叫一隻烏龜
	t.speed(1) #速度
	# 烏龜預設在 0,0 頭向東
	t.forward(50) #前進
	t.left(100) # 想左轉
	t.forward(10) #前進
	# t.circle(20)
	paper.exitonclick() #按一下才離開
def test3():
	paper = turtle.Screen() #paper 建立紙
	paper.setup(600, 600) # 紙大小
	t = turtle.Turtle()   # 叫一隻烏龜
	t.speed(4) #速度
	t.fillcolor('white') # 填充顏色 https://libraries.io/pypi/string-color
	t.begin_fill() # 開始填充
	t.circle(100)
	t.end_fill() # 結束填充
	paper.exitonclick() #按一下才離開

def test3():
	paper = turtle.Screen() #paper 建立紙
	paper.setup(600, 600) # 紙大小
	t = turtle.Turtle()   # 叫一隻烏龜
	t.speed(4) #速度
	t.fillcolor('white') # 填充顏色 https://libraries.io/pypi/string-color
	t.begin_fill() # 開始填充
	t.circle(100)
	t.end_fill() # 結束填充
	paper.exitonclick() #按一下才離開

def test4():
	paper = turtle.Screen() #paper 建立紙
	paper.setup(600, 600) # 紙大小
	t = turtle.Turtle()   # 叫一隻烏龜
	t.speed(7) #速度
	t.fillcolor('white') # 填充顏色 https://libraries.io/pypi/string-color
	t.begin_fill() # 開始填充
	t.circle(100)
	t.end_fill() # 結束填充
	t.up()
	t.goto(25,125)
	t.down()
	t.circle(30)
	t.up()
	t.goto(-35,125)
	t.down()
	t.circle(30)
	paper.exitonclick() #按一下才離開
test4()