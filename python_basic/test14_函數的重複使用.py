# 函數重複使用
def c_dog_f(dog): #計算狗的腳方法
	# 括號裡面的東西 叫做引數
	# dog 狗的數量
	f_dog = dog*4 #腳的數量
	return f_dog #回傳值

# 重複使用
dog = 20
print(f'小狗有{dog}隻,總共有{c_dog_f(dog)}隻腳')
dog = 200
print(f'小狗有{dog}隻,總共有{c_dog_f(dog)}隻腳')
#-----------------
def c_square_b(square):#計算正方形的方法
	d_square=square*4
	return d_square
square=20000
print(f'''正方形有{square}個,
	總共有{c_square_b(square)}個邊''')