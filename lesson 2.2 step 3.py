from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    z = str (int(x.text) + int(y.text))
    print (z)
    spisok = Select ( browser.find_element(By.ID, "dropdown"))
    spisok.select_by_value(z)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()




finally:
    time.sleep(15)
    browser.quit()