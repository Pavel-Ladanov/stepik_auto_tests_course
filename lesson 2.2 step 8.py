from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time, os
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'new.txt')  # добавляем к этому пути имя файла

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    pole1 = browser.find_element(By.CSS_SELECTOR, ".form-group input:nth-child(2)")
    pole2 = browser.find_element(By.CSS_SELECTOR, ".form-group input:nth-child(4)")
    pole3 = browser.find_element(By.CSS_SELECTOR, ".form-group input:nth-child(6)")
    pole1.send_keys('o')
    pole2.send_keys('oo')
    pole3.send_keys('ooo')
    polefile = browser.find_element(By.ID,'file')
    polefile.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()



finally:
    time.sleep(10)
    browser.quit()
