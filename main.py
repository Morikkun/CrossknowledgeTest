import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox('..\\Crossknowledge')
driver.get('https://teamshift-qa.crossknowledge.com/')

loginButton = driver.find_element_by_css_selector('body > main > header > nav > div.visible-lg-block > div > div > button')
loginButton.click()

emailInputBox = driver.find_element_by_xpath('//*[@id="login-form__login"]')
emailInputBox.send_keys("diego.f.dias@outlook.com")

nextButton = driver.find_element_by_xpath('/html/body/main/div[5]/div/div/div[3]/button[2]')
nextButton.click()

time.sleep(3)

passwordInputBox = driver.find_element_by_xpath('/html/body/main/div[5]/div/div/div[2]/div/div/form/div[2]/input')
passwordInputBox.send_keys("WLS2020qa")

login = driver.find_element_by_css_selector('#js-modal-login-member > div > div > div.modal__footer > button.button-default.js-login-form-submit')
login.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "member-result__text-greeting"))
    )
    driver.quit()
except:
    driver.quit()

