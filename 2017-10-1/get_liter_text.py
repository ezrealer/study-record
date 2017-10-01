import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'#假设的网址
total_page = 20 #假设网页有20页

f = open('../txt/text.txt','r')
html = f.read()
f.close()
#提取部分文字
ul = re.findall('<ul>(.*?)</ul>',html,re.S)[0]#先获取包含我们想要得到的文本信息的大框架
a_text = re.findall('">(.*?)</a>',ul,re.S)#从得到的大框架中再获取文本信息，避免获得不想要的内容
for text in a_text:
    print(text)