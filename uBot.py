from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

input1= input("paste your youtube video link: ")


driver= webdriver.Firefox()
driver.get('https://www.y2mate.com/en61')

btn1= driver.find_element_by_name('query')
btn1.send_keys(input1)
time.sleep(1)

bclick=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div[2]/form/button/span[1]')
bclick.click()
time.sleep(3)

btn2= driver.find_element_by_xpath('//*[@id="mp4"]/table/tbody/tr[1]/td[3]/a').click()
time.sleep(2)

btn3= driver.find_element_by_xpath('//*[@id="process-result"]/div/a').click()
time.sleep(2)
#closing advertisement window
window_name = driver.window_handles[1]
driver.switch_to.window(window_name=window_name)
driver.close()