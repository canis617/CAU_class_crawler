from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import class_classify
import insertResult

delay = 1

driver = webdriver.Chrome('chromedriver')

#login
driver.get('https://mportal.cau.ac.kr/common/auth/SSOlogin.do?redirectUrl=/main.do')

driver.find_element_by_name('userID').send_keys('r.find_element_by_name('password').send_keys('.find_element_by_xpath('//*[@id="form1"]/div/div/div[2]/a').click();

driver.implicitly_wait(delay)
driver.implicitly_wait(delay)


driver.get('https://mportal.cau.ac.kr/std/usk/sUskSif001/index.do?type=1')

select =Select(driver.find_element_by_id('sel_camp'))
select.select_by_value("1")
time.sleep(delay)

classinfo = []

select = Select(driver.find_element_by_id('sel_shtm'))
select.select_by_index(0)
driver.implicitly_wait(delay)

#select university
select = Select(driver.find_element_by_id('sel_colg'))
for index in range(18, len(select.options)):
    select = Select(driver.find_element_by_id('sel_colg'))
    select.select_by_index(index)
    time.sleep(delay)
    if index != 0:
        #select major
        select2 = Select(driver.find_element_by_id('sel_sust'))
        for index2 in range(len(select2.options)):
#            print(index2)
            if index2 != 0:
                select2 = Select(driver.find_element_by_id('sel_sust'))
                select2.select_by_index(index2)
                time.sleep(delay)
                #implement crawling
                driver.find_element_by_xpath('//*[@id="nbContext"]/div[2]/div/div[1]/section[1]/div[2]/div/div/button').click()
                time.sleep(delay*3)
                
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                    
                row = soup.select('#nbContext > div.nb-contents > div > div.BO_system.nb-q.ng-scope > section.section-gap > div > div > div > div.sp-grid-body > div > div')
                count = 1
                for n in row:
                    result = []
                    classnumber = n.select('div:nth-child(6) > div.sp-grid-data.text-center > div > span > a')
                    classID = classnumber[0].get_text().split('-',1)[0]
                    classNum = classnumber[0].get_text().split('-',1)[1]
#                   print(classID)
#                   print(classNum)
                    className = n.select('div:nth-child(7) > div.sp-grid-data.text-center > div > span > a')
#                   print(className[0].get_text())
                    classTime = n.select('div:nth-child(8) > div.sp-grid-data.text-center > span > span')
#                   print(classTime[0].get_text())
                    classLocation = n.select('div:nth-child(11) > div.sp-grid-data.text-center > div > span')
                    info = classLocation[0].get_text().split(' ')
                    splited = class_classify.classify(info)
                    result =[classID, classNum, className[0].get_text(), classTime[0].get_text(), splited]
#                   print(result);
                    insertResult.insertResult(result)
