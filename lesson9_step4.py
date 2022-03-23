from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()
    
    # принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    
    time.sleep(1)
    
    # считаем выражение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    place = browser.find_element_by_id("answer")
    place.send_keys(str(y))
    
    # нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()