import time
from lxml import etree
from selenium import webdriver
url1 = 'https://www.expedia.com/'
url2 = 'https://www.expedia.com/cn/Hotels-Crowne-Plaza-Hangzhou-Heda.h22949395.Hotel-Information?rm1=a2&hwrqCacheKey=a995f173-aae0-48f9-9c60-bfd1b591f854HWRQ1568703523167&cancellable=false&regionId=6084457&vip=false&c=e95dcb76-9c3b-4f5e-9994-85bb9f38624e&chkin=2019/09/19&chkout=2019/09/20&'
driver = webdriver.Chrome()
driver.get(url=url1)
time.sleep(3)
driver.find_element_by_id('hotel-destination-hp-hotel').send_keys('杭州')
button_click = driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hp-hotel"]/div[11]/label/button')
button_click.click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
# html_resp = driver.page_source
# resp_elem = etree.HTML(html_resp)
# detail_url = resp_elem.xpath('//article[3]//a[@class="flex-link"]/@href')
# detail_url = detail_url[0]
# driver.get(url=detail_url)
time.sleep(5)
print(driver.get_cookies())
