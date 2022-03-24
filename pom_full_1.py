import pytest
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from .pages.basket_page import BasketPage
#from .pages.login_page import LoginPage
#from .pages.product_page import ProductPage

browser = webdriver.Chrome()
browser.maximize_window()
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
browser.get(link)

print('\nTest is OK!')
submit_btn = browser.find_element(By.XPATH, "//*[@value='Add to basket']").click()

alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
try:
 alert = browser.switch_to.alert
 alert_text = alert.text
 print(f"Your code: {alert_text}")
 alert.accept()
except:
 print("No second alert presented")

find_h1 = browser.find_element(By.XPATH, '//h1[contains(text(), "The shellcoder")]')
print(find_h1.text)

time.sleep(3)
#pom_full_1.py
