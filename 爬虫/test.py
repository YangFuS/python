import os
import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
options.add_argument('--start-maximized')  # 浏览器窗口最大化
web = Chrome(options=options)

web.get("http:www.baidu.com")
print(web.title)


# button_sz = web.find_element(by=By.XPATH, value='//*[@id="changeCityBox"]/ul/li[6]/a')
# button_sz.click()
#
# time.sleep(2)
# search_input = web.find_element(by=By.XPATH, value='//*[@id="search_input"]')
# search_input.send_keys("python", Keys.ENTER)

# web.quit()
# if __name__ == "__main__":
#     main()
