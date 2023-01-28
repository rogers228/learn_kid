#' 單行文字 '
#" 單行文字 "
#'''  多行文字 '''

dog = 200; cat= 35;  dc=dog+cat
four= 4;
foft=four*dog; fofn=four*cat
dfcf= foft + fofn

print(
f'''小狗有{dog}隻,小貓有{cat}隻,總共有{dc}隻
小狗有{dog}隻,總共有{foft}隻腳
小貓有{cat}隻,總共有{fofn}隻腳
總共有{dfcf}隻腳''')

#-----------------
student_name = '葉大同'
chinese = 38
english = 5
ce=chinese+english
print(f'''同學{student_name}的考試成績,
英文{english}分,
中文{chinese}分,
總共有{ce}分''')