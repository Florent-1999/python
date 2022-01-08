from selenium import webdriver
import selenium.webdriver.remote.webelement
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options


# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
#
# actions = ActionChains(driver)


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input("Enter the victim name or group: ")
msg = input("Enter your Message : ")
count = int(input("Enter the count of message "))
input("Enter: ")


# user = driver.find_element(By.XPATH,'//span[@title = "{}"]'.format(name))
# user.click()
#
# msg_box = driver.find_element(By.CLASS_NAME,'p3_M1')
#
# for i in range(count):
#     button = driver.find_element(By.CLASS_NAME,'_3HQNh _1Ae7k')




