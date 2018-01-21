# -*- coding = utf-8 -*-
import csv
#1、首先找打测试用例文件和数据文件和数据文件的相对位置
#2、dataDriverTest2。py和csv的相对路径
import os
#os 系统、dir目录  __file__双下划线开头双下划线结尾的变量是python内置的变量
#__file__表示当前文件
# 第二个问题 公用的代码封装成独立方法
#def是define 缩写
def readData():
# 多行注释：选中代码 ctrl+/
    path = os.path.dirname(__file__)
    final_path = path + '\data\member_info.csv'
    print (final_path)
#查看源代码 按住ctrl，并且点击左键
    #open(final_path, 'r')
    file = open(final_path, 'r')
#在操作系统中打开文件的数量是有限的，所有每条测试用例都要即使关闭打开的文件
#如果程序中间发生异常，那么就会导致关闭异常
#所有，这种情况一般用with语句
#声明一个空的列表，然后把table数据保存到列表中，最后返回列表
    result = []
    with open(final_path, 'r') as file:
        table = csv.reader(file)
        #这个方法需要有返回值，有了返回值测试用例才可以操作读取到数据
        for item in table:
            result.append(item)
    return result
abcd = readData()
print (abcd[1],[0])

