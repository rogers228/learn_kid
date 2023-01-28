'''
電腦的判斷
boolean布林
True, False
if 如果 else 否則
if Treue

'''

def test1():
	print('a')
	print(True)
	print(False)

def test2():
	if True:
		print('早上出門')
	else:
		print('晚上出門')

def test3():
	you_sleep_time = 100
	st = 21
	# print(you_sleep_time <= st)
	if (you_sleep_time <= st):
		print('早上出門') #true
	else:
		print('晚上出門') #frue
#-----------------
def test4():
	I_get_up_time = 7.0
	ut = 7.2
	if  (I_get_up_time >ut):
		print('遲到')
	else:
		print('沒遲到')


test4() #執行method 自己改