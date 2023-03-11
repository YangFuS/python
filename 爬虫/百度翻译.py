import time

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
options.add_argument('--start-maximized')  # 浏览器窗口最大化
web = Chrome(options=options)
web.get('https://fanyi.baidu.com/#zh/en/')
try:
    web.find_element(by=By.XPATH, value='//*[@id="app-guide"]/div/div/div[2]/span').click()
except Exception as e:
    # 不存在X弹窗
    pass

try:
    web.find_element(by=By.XPATH,
                     value='//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/a').click()
except Exception as e:
    # 待翻译区域不存在内容
    pass
# txt_list = ["ECU解锁失败", "编程日期", "清除故障码失败"]
f = open('files//CN_TEXT.txt', 'r', encoding='utf-8')
txt_list = f.readlines()
f.close()

for txt in txt_list:
    if '\t\t' in txt:
        text_id = txt.split('\t\t')[0]
        txt_value = txt.split('\t\t')[1].strip().strip('"')
        try:
            web.find_element(by=By.XPATH,
                             value='//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/a').click()
        except Exception as e:
            # 待翻译区域不存在内容
            pass
        web.find_element(by=By.XPATH, value='//*[@id="baidu_translate_input"]').send_keys(txt_value)
        while True:
            # 有时候1s加载不出来翻译结果，需要重试
            try:
                time.sleep(1)
                re = web.find_element(by=By.XPATH,
                                      value='//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]').text
                s_write = f'{text_id}\t\t"{re}"'
                print(s_write)
                break
            except Exception as e:
                continue
    else:
        continue

web.close()
