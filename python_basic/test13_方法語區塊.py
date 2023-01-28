#執行的區塊
#區塊 方法 函數
# def 方法():
# 區塊 不會馬上執行 只會讀取 要另外呼叫他
# 可以在同一個檔案執行很多種方法  不用很多檔案

def c_dog(): #計算狗的方法
	dog = 200; cat= 35;  dc=dog+cat
	four= 4;
	foft=four*dog; fofn=four*cat
	dfcf= foft + fofn

	print(
	f'''小狗有{dog}隻,小貓有{cat}隻,總共有{dc}隻
	小狗有{dog}隻,總共有{foft}隻腳
	小貓有{cat}隻,總共有{fofn}隻腳
	總共有{dfcf}隻腳''')

def c_person(): # 計算人的方法
	student_name = '葉大同'
	chinese = 38
	english = 5
	ce=chinese+english
	print(f'''同學{student_name}的考試成績,
	英文{english}分,
	中文{chinese}分,
	總共有{ce}分''')

def c_fish():#計算魚的方法
	yellow=32
	black=47
	yb=yellow+black
	print(f'''小黃有{yellow}隻,
	      小黑有{black}隻,
	      總共有{yb}隻''')

# c_dog()   # 計算狗
# c_person() # 計算人的方法 
c_fish()#計算魚的方法
#---------------
