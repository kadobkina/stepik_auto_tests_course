from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считаем выражение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    place = browser.find_element_by_id("answer")
    place.send_keys(str(y))
    
    # checkbox
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    
    # radiobutton
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn[type='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()