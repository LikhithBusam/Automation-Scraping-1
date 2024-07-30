import requests
import html5lib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
def main():
    menu()
    
    op1=input("enter the opnion u want: ")


    if op1=='1':
       Extract()
    elif op1=='2':
        view()

    else:
        print("enter a valid condition")
def menu():
     print("what do u wanna want? \n 1.view only the headlines\n 2. view todays newspaper \n ")

def Extract():
        response = requests.get('https://www.nytimes.com/section/todayspaper')
        soup=BeautifulSoup(response.content,"html5lib")
        table_of_cont=soup.findAll("a",attrs={"class","css-1u3p7j1"})
        print("main topics")
        for i in table_of_cont:
            value=i.text.strip()
            
            print("\t"+value)
            
        
        print("sub topics")

        table_of_cont1=soup.findAll("h2",attrs={"class","css-1sd6y0f e1b0gigc0"})
        for i in table_of_cont1:
            j=i.text.strip()
            print("\t"+j)
        time.sleep(10)
def view():
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.nytimes.com/section/todayspaper")
        img=driver.find_element(By.XPATH,'//*[@id="collection-todays-new-york-times"]/div[1]/section[1]/div[2]/section/div/div[2]/button/img')
        img.click()
        view=driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div/div/div/div/div/div[2]/a')
        view.click()
        time.sleep(200)

if __name__ == "__main__":
    main()

