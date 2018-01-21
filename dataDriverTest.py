# -*- coding = utf-8 -*-
'''
#数据驱动测试，首先要读取数据文件
#数据类型
#数据库、excel（手工操作），csv（是excel的一种），txt
#如何读取csv数据
1、准备csv文档
2、想要读取csv文件必须引入csv代码库
3、必须知道文件的目录结构
4、字符串前面 加r最简单，反斜线该正斜线可以跨平台
5、打开member_info.csv文件  open方法
6、因为文件中的内容属于csv文件格式，需要用到reader方法读取其中内容
7、用fro循环
8、吧table中的每一行取出打印表格每一行
9、程序里面不能用绝对路径  应该改成相对路径，便于携程相对工作
'''
import csv
path = r'D:\Selenium120\data\member_info.csv'
file = open(path, 'r')
table = csv.reader(file)
for item in table:
    print (item)
