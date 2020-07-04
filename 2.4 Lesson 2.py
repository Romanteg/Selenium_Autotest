from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    start_browser = webdriver.Chrome()
    start_browser.get("http://suninjuly.github.io/explicit_wait2.html")


    message = WebDriverWait(start_browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = start_browser.find_element_by_id("book")
    button.click()

    number = start_browser.find_element_by_id("input_value")
    print(number.text)
    sum = calc(number.text)
    print(sum)
    entry = start_browser.find_element_by_id("answer")
    entry.send_keys(sum)
    button = start_browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)
    start_browser.quit()
