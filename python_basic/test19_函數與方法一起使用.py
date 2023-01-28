# 函數與方法一起使用
def foot4(co): #四隻腳的動物
	foot = 4*co #計算
	return foot #回答

def foot2(co):
	foot = 2*co
	return foot

def main():
	dog_count = 5786
	cat_count = 367
	bah = 35
	bird=1037690
	print(f'狗有{dog_count}隻，共有{foot4(dog_count)}隻腳')
	print(f'貓有{cat_count}隻，共有{foot4(cat_count)}隻腳')
	print(f'烏鴉有{bah}隻,總共有隻{foot2(bah)}腳')
	print(f'小鳥有{bird}隻,總共有隻{foot2(bird)}腳')

main()