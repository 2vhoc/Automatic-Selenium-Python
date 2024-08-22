#Library SELENIUM:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#Libreary SYSTEM:
import os
import time

#Source:
WChromeOP = webdriver.ChromeOptions()
pref = {
    "profile.managed_default_content_setting.images": 2
}
#Main
if __name__ == "__main__":
    try:
        WChromeOP.add_experimental_option("prefs", pref)
        driver_path = r'D:\chromedriver.exe' #address chrome driver
        service1 = Service(driver_path)
        driver = webdriver.Chrome(service=service1, options=WChromeOP)
        driver.get(url='http://facebook.com') # get link : google.com, fb.com...
#ID_PASS:
        time.sleep(1)
        css_id = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]') # css 
        css_id.send_keys('012345678') #login account user numberphone
        time.sleep(0.5)
        css_pass = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
        css_pass.send_keys('xxxxxxxxx') #pass account
        css_button_login = driver.find_element(By.CSS_SELECTOR, 'button[name="login"]')
        css_button_login.click()
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Messenger"]')))
#Body:
        css_messenger_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Messenger"]')
        css_messenger_button.click()
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//span[contains(text(), "Vu Hoc")]'))
        )
        element.click()

        div_element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"]'))
    )
#Auto:
        time.sleep(1)
        for _ in range(1000):
            div_element.click()
            div_element.send_keys("Ôi ôi ôi, mất quyền kiểm soát, mất quyền kiểm soát, ôi ôi ôi") # contents send
            time.sleep(0.5)
            div_element.send_keys(Keys.ENTER)
    except:
        pass
    



#Keep webchrome
    while True:
        time.sleep(10)
    
