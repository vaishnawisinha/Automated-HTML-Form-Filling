import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

with open('test.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)


    for line in csv_reader:
        # print(line)

        driver = webdriver.Chrome(executable_path='C:\\Users\\91916\\Downloads\\chromedriver_win32\\chromedriver')
        driver.get('https://www.veteransindia.com/form/')
        

        time.sleep(1)

        name = driver.find_element_by_xpath('//*[@id="first_name"]') 
        name.send_keys(line[2])
        print("------------------NAME-----------------------------------",line[2])


        sem = driver.find_element_by_xpath('//*[@id="awa"]') 
        sem.send_keys(line[3])

        email = driver.find_element_by_xpath('//*[@id="email"]') 
        email.send_keys(line[0])

        
        phone = driver.find_element_by_xpath('//*[@id="phone_number"]') 
        phone.send_keys(line[1])

        phone = driver.find_element_by_xpath('//*[@id="app"]') 
        phone.send_keys("Karunya Institute of Technology and Sciences")

        
        phone = driver.find_element_by_xpath('//*[@id="chequeno"]') 
        phone.send_keys("641114")

        drp = Select(driver.find_element_by_id("state-dropdown"))
        drp.select_by_visible_text('Tamil Nadu')
        time.sleep(1.5)

        drp = Select(driver.find_element_by_id("city-dropdown"))
        drp.select_by_visible_text('Coimbatore')

        time.sleep(1.5)

        drp = Select(driver.find_element_by_id("legislativeassembly"))
        drp.select_by_visible_text('Coimbatore (South)')
        time.sleep(1.5)

        submit = driver.find_element_by_xpath('//*[@id="submit"]') 
        submit.click()

      

