from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

driver.get("https://monkeytype.com/")

wait = WebDriverWait(driver, 10)

accept_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cookiePopup"]/div[2]/div[2]/button[1]')))
accept_btn.click()

words = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="words"]')))

words = words.text.replace('\n', ' ')

for word in words.split(' '):
    actions.send_keys(word + " ").perform()