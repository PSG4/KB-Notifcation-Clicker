import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 15)

base_url = "https://app.iqtrack.com/#review/kb"
browser.get(base_url)

wait.until(EC.element_to_be_clickable((By.ID, "textfield-1013-inputEl")))

username = browser.find_element_by_id("textfield-1013-inputEl")
password = browser.find_element_by_id("textfield-1014-inputEl")
submit_login = browser.find_element_by_id("button-1016-btnIconEl")

username.send_keys("")
password.send_keys("!")
submit_login.click()
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'departmentselector-')]")))
firm_selector = browser.find_element_by_xpath("//input[contains(@id,'departmentselector-')]")

firm_selector.send_keys("")
firm_selector.send_keys("All Intelliteach Clients")
firm_selector.send_keys(Keys.RETURN)
time.sleep(3)

more_kbs = True
while more_kbs:
    try:    
        wait.until(EC.presence_of_element_located((By.XPATH, ".//div[@data-id = 'reviewed']")))
        browser.find_element_by_xpath(".//div[@data-id = 'reviewed']").click()
    except TimeoutException:
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "refresh-link")))
            browser.find_element_by_class_name("refresh-link").click()
        except TimeoutException:            
            print ("Done! No More KB's or refresh button found after 30secs.")
            more_kbs = False
            browser.Quit()
    
    
