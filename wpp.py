from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('user-data-dir=selenium')

print('WhatsApp Jarvis by GUILHERME DINAMARCO')
print('Print any key to continue')
input('')

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com')
input("After Scanning press any key to continue")

def name_input():
    user_name = input('Whon do you want to send a message: ')
    chat = driver.find_element_by_xpath('//span[text()="%s"]' % (user_name))
    chat.click()

def texter():
    lane = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
   # i = 1
   # ranger = int(input('How many time to send a message: '))
    typo = input('Enter the message to send:  ')
    #while i < ranger:
    lane.send_keys(typo)
    lane.send_keys(Keys.RETURN)
    #i = i+1

while True:
    name_input()
    texter()

