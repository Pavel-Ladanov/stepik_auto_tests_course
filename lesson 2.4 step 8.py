
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math, time, os
browser = webdriver.Chrome()

def calc(x):
    result = math.log(abs(12*math.sin(int(x))))
    return str(result)

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()


    findx = browser.find_element(By.ID, "input_value")
    pole = browser.find_element(By.ID, "answer")
    tosend = calc(findx.text)
    pole.send_keys(tosend)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()




finally:
    time.sleep(40)
    browser.quit()
