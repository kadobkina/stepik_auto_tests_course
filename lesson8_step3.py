from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считаем выражение
    input1 = browser.find_element_by_id("num1")
    input2 = browser.find_element_by_id("num2")
    answer = str(int(input1.text)+int(input2.text))
    
    # ищем и выбираем ответ
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(answer)
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()