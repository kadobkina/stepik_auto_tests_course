from selenium import webdriver
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем поля
    place1 = browser.find_element_by_name("firstname")
    place1.send_keys("Ответ")
    place2 = browser.find_element_by_name("lastname")
    place2.send_keys("Ответ")
    place3 = browser.find_element_by_name("email")
    place3.send_keys("Ответ")
    
    # загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')        
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn[type='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()