
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
options=Options()

options.add_argument("--disable-notifications")      #disable the notifications
options.add_argument("--disable-geolocations")

user_name=input("enter your email id:")
password=input("enter password:")

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.facebook.com/")                 #opens facebook page


user=driver.find_element_by_name("email")        #email id
user.send_keys(user_name)
time.sleep(4)
user=driver.find_element_by_name("pass")        #password
user.send_keys(password)
time.sleep(4)
user.send_keys(Keys.RETURN)                    #login
time.sleep(3)



driver.get('https://www.facebook.com/stories/create')     #updating status (using text only)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[2]').click()
time.sleep(8)
status= driver.find_element_by_xpath('//*[@id="jsc_c_k"]')
status.send_keys("hello")
time.sleep(4)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div/span/span').click()


