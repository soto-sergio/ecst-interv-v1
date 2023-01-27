# Import packages and files
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from private.credentials import username, password
from private.homeroom_roster import homeroom_roster

# Homeroom Roster - Dictionary ID:First Name
homeroom_roster = homeroom_roster

# Credentials
user= username
pasw= password

# Date (Do not change)
date = datetime.today().strftime('%m/%d/%Y')

# Instruction Plan and Minutes
instruction_plan = input("Today is 'math' or 'reading' intervention?: ")
minutes = 30

# Attendance
final_attendance = []
attendance = []
j=0
for i in homeroom_roster:
    attendance.append(input("Is "+ homeroom_roster[i] +" here today? (y/n):" ))
    
    if attendance[j] == "y":
        final_attendance.append(i)
        j = j+1
    else:  
        j = j+1    

print(final_attendance)

# Accesing ecst
driver = webdriver.Chrome('chromedriver.exe')
wait = WebDriverWait(driver, 3)
website = driver.get("https://access.austinisd.org/ACM/agreement.htm") 
driver.find_element_by_xpath('//*[@id="uname"]').send_keys(user)  # Pass username
time.sleep(3)
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(pasw)    # Pass password
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ecstSubmit"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="inner"]/form/input[1]').click()

# Math Intervention
if instruction_plan == "math":
    for i in final_attendance:
        driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[3]/td/input').send_keys(i)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[7]/th/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="inner"]/table[4]/tbody/tr[2]/td[1]/div[5]/ul/li[2]/a').click()
        time.sleep(2)

        # Check for empty box
        k = 0
        check_box = driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate')
        check_value = check_box.get_attribute('value')
        
        
        if (check_value == ""):
             driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate').send_keys(date) # Date Box
             driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutes').send_keys(minutes)  # Minutes Box  
             time.sleep(3)
             driver.find_element_by_xpath('//*[@id="aipForm"]/div[3]/input').click()   # Save
             driver.find_element_by_xpath('//*[@id="logo"]').click()     # Go to student search page   
        else:
            k = k+1
            while (check_value !=""):
                 check_box = driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate')
                 check_value = check_box.get_attribute('value')
                 k = k+1
            else:
                driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate').send_keys(date) # Date Box
                driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutes').send_keys(minutes)  # Minutes Box  
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="aipForm"]/div[3]/input').click()   # Save
                driver.find_element_by_xpath('//*[@id="logo"]').click()     # Go to student search page   

# Reading Intervention
if instruction_plan == "reading":
    for i in final_attendance:
        driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[3]/td/input').send_keys(i)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[7]/th/input').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="inner"]/table[4]/tbody/tr[2]/td[1]/div[5]/ul/li[1]/a').click()
        time.sleep(2)

        # Check for empty box
        k = 0
        check_box = driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate')
        check_value = check_box.get_attribute('value')
        
        
        if (check_value == ""):
             driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate').send_keys(date) # Date Box
             driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutes').send_keys(minutes)  # Minutes Box  
             time.sleep(3)
             driver.find_element_by_xpath('//*[@id="aipForm"]/div[3]/input').click()   # Save
             driver.find_element_by_xpath('//*[@id="logo"]').click()     # Go to student search page   
        else:
            k = k+1
            while (check_value !=""):
                 check_box = driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate')
                 check_value = check_box.get_attribute('value')
                 k = k+1
            else:
                driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutesDate').send_keys(date) # Date Box
                driver.find_element_by_name('aipMeetingMinutesDateList[' + str(k) + '].aipMeetingMinutes').send_keys(minutes)  # Minutes Box  
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="aipForm"]/div[3]/input').click()   # Save
                driver.find_element_by_xpath('//*[@id="logo"]').click()     # Go to student search page  

driver.close()

