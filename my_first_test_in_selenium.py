from selenium import webdriver
import time

# Zastosowanie Webdriver Manager:
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# Inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

driver.get('https://www.google.com')

driver.maximize_window()

accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
accept.click()

time.sleep(60)

# Zamkniecie wszystkich okien przegladarki
# driver.quit()

# Zamkniecie danego okna przegladarki
driver.close()
