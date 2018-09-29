# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options

#display = Display(visible=0, size=(800, 800))  
#display.start()
'''
chrome启动，需要一个浏览器driver,
我是linux64位，下载了2.42版本
https://sites.google.com/a/chromium.org/chromedriver/downloads
下载后解压，把可执行文件放到usr/bin目录下，就和WINDOS添加path一样。

启动浏览器参考了
https://blog.csdn.net/u011541946/article/details/67633536
https://blog.csdn.net/daocaoren92wq/article/details/80155595
linux下的bug依靠第二个链接的方式解决了，
问题是，好像浏览器无法显示出来，因为headless的选项,已解决，headless只管有没有显示，不是我bug原因

'''


def chromestart():
	#chrome_options = Options()
	#chrome_options.add_argument('--headless')
	#chrome_options.add_argument('--disable-gpu')
	#chrome_options.add_argument("window-size=1024,768")
	#chrome_options.add_argument("--no-sandbox")
	#driver = webdriver.Chrome(chrome_options=chrome_options)
	driver = webdriver.Chrome('/usr/bin/chromedriver')
	driver.maximize_window()  # 最大化浏览器
	driver.implicitly_wait(8) # 设置隐式时间等待

	driver.get("https://www.baidu.com")


	print(driver.page_source)
	driver.quit()


chromestart()
