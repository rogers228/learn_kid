# 區塊 method 先讀取  後來呼叫才會執行
def dog():
	print('拗拗拗')


def cat():
	print('喵喵喵')

#-----------
dog()
cat()
dog()