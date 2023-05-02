
from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time, os
browser = webdriver.Chrome()
def calc(x):
    result = math.log(abs(12*math.sin(int(x))))
    return str(result)

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button1.click()
    accept = browser.switch_to.alert
    accept.accept()

    findx = browser.find_element(By.ID, "input_value")
    pole = browser.find_element(By.ID, "answer")

    tosend = calc(findx.text)
    print(tosend)
    pole.send_keys(tosend)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()





finally:
    time.sleep(10)
    browser.quit()
