from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)

# Jesli nie znaleziono elementu - poczekaj 10 sekund
# driver.implicitly_wait(10)



driver.get('https://www.w3schools.com')
print("Open:", driver.title)

driver.maximize_window()

accept = driver.find_element('id', 'accept-choices')
accept.click()

html_menu = driver.find_element('xpath', '//*[@id="subtopnav"]/a[1]')
html_menu.click()

# Uzycie waita dla danego elementu przy uzyciu tupli tzn. krotki
wait.until(expected_conditions.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')))

# Wait z wlasnym zdefiniowanym warunkiem (wykorzystujemy lambde i niezerowa dlugosc listy)
# wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')))

html_forms = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')
html_forms.click()

time.sleep(5)

driver.quit()
