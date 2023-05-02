from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time
browser = webdriver.Chrome()
def calc(x):
  return str (math.log(abs(12*math.sin(x)),math.e))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID,'input_value')
    answer = calc(int(x.text))
    print(answer)
    foranswer = browser.find_element(By.ID, 'answer')
    foranswer.send_keys(answer)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)

    time.sleep(1)

    radio.click()
    button.click()
finally:
    time.sleep(15)
    browser.quit()
