from select import select
from sys import maxsize
import time
from unicodedata import name
import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

class Orange(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_Orange(self):
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        browser.maximize_window()

        #LOGIN
        browser.find_element(By.NAME,"username").send_keys("admin")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)

        
        #Add employee
        browser.find_element(By.XPATH,"//a[text()='Add Employee']").click()
        time.sleep(1)
        browser.find_element(By.NAME,"firstName").send_keys("Jaden")
        time.sleep(2)
        browser.find_element(By.NAME,"middleName").send_keys("Ham")
        time.sleep(2)
        browser.find_element(By.NAME,"lastName").send_keys("Smith")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)
        
        

        
        #Add Skills
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click() #klik sub menu admin
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click() #
        time.sleep(2)
        browser.find_element(By.XPATH,"//a[text()='Skills']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button").click() #button add
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("Jenkins") #
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("Programming Language") #
        time.sleep(2)
        browser.find_element(By.XPATH,"//button[@Class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click() #save
        time.sleep(6)
        

        
        #Approve/Reject Leave list
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span").click() #sub menu leave
        time.sleep(2)
        browser.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("linda")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/span").click() 
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click() #button search
        time.sleep(2)
        browser.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Reject'])[2]").click() #reject
        time.sleep(2)
        browser.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Approve'])[2]").click() #Aprrove
        time.sleep(4)
        

        
        #Add Timesheet
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span").click() #sub menu time
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click() #menu bar time sheets
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a").click() #menu my timesheets
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button").click() #klik edit
        time.sleep(2)
        browser.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus']").click() #klik icon +
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[2]/td[1]/div/div[2]/div/div/input").send_keys("apache") #keyword
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[2]/td[1]/div/div[2]/div/div[2]/div/span").click() #klik nama
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div").click() #klik nama
        time.sleep(2)

        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[7]/span").click() #select job
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[2]/td[6]/div/div[2]/input").send_keys("10:00")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click()
        time.sleep(2)
        

        
        # Add Candidats
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span").click() #sub menu recurment
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click() #add candidate
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("Chris") #first name
        time.sleep(2)
        browser.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-middlename']").send_keys("Jae") #middle name
        time.sleep(2)
        browser.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-lastname']").send_keys("Cartz") #last name
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div").click() #click position
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[4]").click() #click position
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys("chris@yahoo.com") #email
        time.sleep(2)
        file=browser.find_element(By.XPATH,"//input[@class='oxd-file-input']") #upload file
        file.send_keys("C:/Users/Rizmi/Documents/cobba.docx")
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click()
        time.sleep(2)
        

        
        #Upload/edit foto profil
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@class='orangehrm-edit-employee-image']//img[@alt='profile picture']").click()
        browser.find_element(By.XPATH,"//button[@class='oxd-icon-button employee-image-action']").click()
        time.sleep(3)
        pyautogui.write(r"C:\Users\Rizmi\Pictures\images.jfif")
        pyautogui.press("enter")
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/button").click()
        time.sleep(3)
        


        
        #Search Performance
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a").click() #sub menu performance
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click() # menu bar manage review
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click() #klik manage review
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div").click() #click position
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/div/div[2]/div/div[2]/div[19]").click() #click pstion
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() #click save
        time.sleep(5)
        

        #Search Directory Employee
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a").click() #sub directory
        time.sleep(2)
        browser.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("linda") #input text
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/span").click() 
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() 
        time.sleep(2)
        
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()



        
