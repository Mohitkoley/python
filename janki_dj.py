from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")

bar=driver.find_element_by_name('search_query')
bar.send_keys("shri ram janki dj")
ser = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
ser.click()
time.sleep(3)

vid=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
vid.click()
time.sleep(3)