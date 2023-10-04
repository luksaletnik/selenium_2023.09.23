from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.w3schools.com')
print("Open:", driver.title)

driver.maximize_window()

accept = driver.find_element('id', 'accept-choices')
accept.click()

html_menu = driver.find_element('xpath', '//*[@id="subtopnav"]/a[1]')
html_menu.click()

html_forms = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')
html_forms.click()

time.sleep(5)

driver.quit()
