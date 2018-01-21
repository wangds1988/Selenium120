#coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://127.0.0.1/index.php?m=user&c=public&a=login')
driver.find_element_by_id('username').send_keys('changcheng')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_class_name('login_btn').click()
time.sleep(5)
##driver.find_element_by_link_text('进入商城购物').click()
driver.find_element_by_link_text('账号设置').click()
driver.find_element_by_partial_link_text('个人资料').click()
#driver.find_element_by_xpath('//*[@id=\"true_name\"]')
#Xpath 缺点查找慢
#cssSelector有点：快，定位简单，准确
driver.find_element_by_css_selector('#true_name').clear()

driver.find_element_by_css_selector('#true_name').send_keys('张三')
driver.find_element_by_css_selector("[value=\'2\']").click()
driver.execute_script(r'document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id('date').clear()
driver.find_element_by_id('date').send_keys('1999-01-01')
driver.find_element_by_id('qq').clear()
driver.find_element_by_id('qq').send_keys('123456')
driver.find_element_by_css_selector(".btn4").click()
time.sleep(3)
driver.switch_to_alert().accept()
#driver.quet()
'''
Css 中id属性前面加#
class属性前面加  。
其他属性就加（）
对弹窗操作;在处理弹出框操作前，一定要加一个固定等待时间

'''



#1账号设置
#2个人资料
#3修改具体信息
#保存