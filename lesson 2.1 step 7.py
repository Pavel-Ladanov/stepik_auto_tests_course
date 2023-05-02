from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    ingelem = browser.find_element(By.ID, "treasure")
    valuex = ingelem.get_attribute('valuex')
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(valuex))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()




finally:
    time.sleep(15)
    browser.quit()