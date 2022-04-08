from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://www.dkfnet.dk/medlemsliste/"
    
    driver.get(url)
    startTime = time.time()
    print("start... ", startTime)
    
    driver.implicitly_wait(100)

    select_all = driver.find_element_by_xpath('//*[@id="kt-layout-id_e715ce-ca"]/div/div/div/div/div[2]/div[3]/select[3]/option[7]')
    select_all.click()
    driver.implicitly_wait(10)

    companies = driver.find_elements_by_class_name("fc-itemcontent-padding")
    count_companies = 0

    arr_company_name =   []
    arr_address      =   []
    arr_phone        =   []
    arr_email        =   []
    arr_homepage     =   []

    for block in companies:
        count_companies += 1

        el_company_name = block.find_element_by_xpath('./div[1]/a')
        el_address = block.find_element_by_xpath('./div[2]')
        el_phone = block.find_element_by_xpath('./div[3]')
        el_email = block.find_element_by_xpath('./div[4]/a')
        el_homepage = block.find_element_by_xpath('./div[5]/a')

        arr_company_name.append(el_company_name.text)
        arr_address.append(el_address.text)
        arr_phone.append(el_phone.text)
        arr_email.append(el_email.text)
        arr_homepage.append(el_homepage.text)

        # print(" ------------ company name => ", el_company_name.text)
        # print(" ------------ address => ", el_address.text)
        # print(" ------------ phone => ", el_phone.text)
        # print(" ------------ email => ", el_email.text)
        # print(" ------------ homepage => ", el_homepage.text)

    df_excel = pd.DataFrame({'Company name': arr_company_name, 'Address': arr_address, 'Phone': arr_phone, 'Email': arr_email, 'Homepage': arr_homepage})    
    df_excel.to_excel('xls/export_companies__' + str(startTime) + '.xlsx', sheet_name='sheet1', index=False)   

    print("exit")
