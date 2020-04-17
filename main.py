from selenium import webdriver
from time import sleep    
import os
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

dirpath = os.getcwd()

driver = webdriver.Chrome(
    executable_path=r"{}\chromedriver.exe".format(dirpath))

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("disable-infobars")
options.add_argument("--allow-file-access-from-files")
options.add_argument("--allow-file-access")
options.add_argument("--allow-cross-origin-auth-prompt")

driver = webdriver.Chrome(options=options)
url = "https://accounts.google.com/ServiceLogin/identifier?flowName=GlifWebSignIn&flowEntry=AddSession"
driver.maximize_window()
driver.get(url)
wait = WebDriverWait(driver, 10)
main_window = driver.current_window_handle

def get_all_titles():
    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//*[@id='identifierId']")) > 0)
    bet_fa = driver.find_element_by_id("identifierId")
    user_login =  os.getenv('USER_LOGIN')
    bet_fa.send_keys(user_login)
    bet_fa.send_keys(u'\ue007')

def password():
    WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")) > 0)
    input_pass = driver.find_element_by_name("password")
    user_pass =  os.getenv('USER_PASS')
    input_pass.send_keys(user_pass)
    input_pass.send_keys(u'\ue007')

try:
    driver.switch_to.window
    get_all_titles()
    sleep(2)
    password()
    # import pdb; pdb.set_trace()

except Exception as ex:
    print(ex)
    driver.quit()

# finally:






