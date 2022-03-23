from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считаем выражение
    treasure_value = browser.find_element_by_id("treasure")
    x = treasure_value.get_attribute("valuex")
    y = calc(x)
    
    # заполняем поле
    place = browser.find_element_by_id("answer")
    place.send_keys(y)
    
    # checkbox
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    # radiobutton
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()