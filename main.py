from selenium import webdriver

url = "https://easy.lagou.com/search/result.htm?pageNo=1&keyword=%E7%BD%91%E7%AB%99%E5%89%8D%E6%AE%B5&city=%E5%8C%97%E4%BA%AC"
driver = webdriver.Chrome()

cookie = {
    "name": "Hm_lvt_bfa5351db2249abae67476f1ec317000",
    "value": "1518926130,1519366296",
    "domain": ".easy.lagou.com",
    "expirationDate": 1550902295,
    "hostOnly": False,
    "httpOnly": False,
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "id": 3
}

print cookie

driver.add_cookie(cookie_dict=cookie)

driver.get(url)

print driver.page_source