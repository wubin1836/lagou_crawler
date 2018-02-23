from selenium import webdriver

url = "https://easy.lagou.com/search/result.htm?pageNo=1&keyword=%E7%BD%91%E7%AB%99%E5%89%8D%E6%AE%B5&city=%E5%8C%97%E4%BA%AC"

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
)
dcap["phantomjs.page.settings.loadImages"] = False
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs/bin/phantomjs', desired_capabilities=dcap)
driver.maximize_window()

cookies =

for cookie in cookies:
    try:
        driver.add_cookie(cookie_dict=cookie)
    except:
        pass
from bs4 import BeautifulSoup

import time
driver.get(url)
source = driver.page_source
print source
result_list = BeautifulSoup(source).find_all("div", class_="result_list_item")
for item in result_list:
    print item.strip()
    time.sleep(5)