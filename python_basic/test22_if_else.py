import PySimpleGUI as sg
def myinput(question):
	sg.theme('SystemDefault')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Text(question)],
	            [sg.Text('請回答'), sg.InputText()],
	            [sg.Button('Ok'), sg.Button('Cancel')] ]

	window = sg.Window('PySimpleGUI', layout)
	while True:
	    event, values = window.read()
	    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
	        break
	    # print('You entered ', values[0])
	    return values[0]
	window.close()

def test1():
	a = myinput('請問你幾歲?')
	if a != "":
		sg.Popup(f'我知道你{a}歲')
		print(a)

def test2():
	I_get_up_time = myinput('請問你今天幾點起床?')
	ut = 7.2 # 正常起床的時間
	if  (float(I_get_up_time) >ut):
		# pribnt('遲到')
		sg.Popup(f'你會遲到喔，快點拉!')
	else:
		# print('沒遲到')
		sg.Popup(f'今天很好，可以輕鬆慢慢來。')

def test3():
	a = int(myinput('請問你的盆子有幾個洞?'))
	b = a*2   #種子數量
	sg.Popup(f'那你要拿{b}個種子')

def test4():
	a = int(myinput('請問你有幾罐八寶粥'))
	b = 15*a  #紅豆數量
	sg.Popup(f'那全部有{b}顆紅豆')

def test5():
	print('Enter your name:')
	x = input()
	print('Hello, ' + x)
test5e()

