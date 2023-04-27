from playwright.sync_api import sync_playwright
import time

p = sync_playwright().start()
browser = p.chromium.launch(headless=False) #关闭无头模式，方便看到页面加载情况
page = browser.new_page() #创建page对象

js="""
Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
"""

try:
    page.add_init_script(js);
    page.goto("http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml")
    print(page.content())
except Exception as err:
    print(err)
finally:
    time.sleep(1000) #等待1000s防止看不到页面http://mpa.hubei.gov.cn/zfxxgk/fdzdgknr/cpzh/index.shtml