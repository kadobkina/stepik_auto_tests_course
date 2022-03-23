from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try: 

    # говорим Selenium проверять в течение 12 секунд
    check = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )
    
    # нажимаем на кнопку
    button = browser.find_element_by_id("book")
    button.click()

    # считаем выражение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # заполняем поле
    place = browser.find_element_by_id("answer")
    #place.execute_script("return arguments[0].scrollIntoView(true);", place)
    place.send_keys(str(y))
    
    # нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()