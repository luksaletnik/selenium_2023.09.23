from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Zastosowanie Webdriver Manager:
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# Inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

driver.get('https://www.google.com')

driver.maximize_window()
driver.set_window_size(1024, 768)

accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
accept.click()

search_box = driver.find_element('name', 'q')

search_box.send_keys('Pinta Hop Selection')
search_box.send_keys(Keys.ENTER)

time.sleep(600)

# Zamkniecie wszystkich okien przegladarki
# driver.quit()

# Zamkniecie danego okna przegladarki
driver.close()
