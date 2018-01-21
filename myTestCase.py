#coding=utf-8
#这个类的作用是吧setup方法和teardow方法，从测试用例中分离出来
#以后创建测试用例时不需要每次都写setup和teardown
#13681477136常成
#这个类如何实现？
#原来的测试用例类继承了unittest.TestCase，所以他需要重写teardown方法
#现在我们写一个类，也继承这个类，并且重写teardown方法
#以后所有的测试用例类只需要继承这个类myTestCase,自动继承父类的方法
import time
from selenium import webdriver
#导包的快捷键 alt+回车
import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('这个方法类似于java中的beforemethod')

        # 一般打开浏览器
        self.driver = webdriver.Chrome()
        # 隐士等待 优点：会自动的加载进行时间的等待，自动判断网页是否加载好，一旦网页加载好后会自动执行下面的语句
        self.driver.implicitly_wait(30)  # 一般加窗口最大化  # driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print('这个方法类似于java中的aftermethod')
        time.sleep(15)
        # 变量改成成员变量
        self.driver.quit()
