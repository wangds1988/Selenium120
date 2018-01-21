# -*- coding=utf-8 -*-
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #通过成员变量名保存页面元素定位信息
    url = 'http://127.0.0.1/index.php?m=user&c=public&a=login'
    username_input_loc = (By.ID, 'username')
    password_input_loc = (By.ID, 'password')
    login_button_loc = (By.CLASS_NAME, 'login_btn')

    #构造方法    init初始化
    def __init__(self, driver):
        self.driver = driver

    #打开登录页面
    def open(self):
        self.driver.get(self.url)
    #输入用户名方法
    def input_username(self, username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self, password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()
    def login(self, username, password):
        self.open()
        self.input_username(username)#输入用户名
        self.input_password(password)#输入密码
        self.click_login_button()#点击按钮
        self.driver.quit()
        #封装思路
    # def input_username2(self):
    #     driver = webdriver.Chrom()
    #
    #     driver.find_element_by_id('username').send_keys('changcheng')
    #     #第一次优化
    #     driver.find_element(By.ID, 'username').send_keys('changcheng')
    #     #第二次优化
    #     username_input_loc = (By.ID, 'username')
    #     #*号把元素拆开
    #     driver.find_element(*username_input_loc, 'username').send_keys('changcheng')
