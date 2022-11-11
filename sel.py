from selenium import webdriver
from selenium.webdriver.common.by import By 
import os

os.environ['PATH'] += "D:\working"
driver = webdriver.Firefox() 

def linked(value): 
    
    driver.get("https://in.linkedin.com/jobs/search?keywords={0}&location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0".format(value)) 
    number = int(driver.find_element(By.CLASS_NAME, "results-context-header__job-count").text)
    post = driver.find_elements(By.CLASS_NAME, "base-search-card__title")  
    location = driver.find_elements(By.CLASS_NAME, "job-search-card__location") 
    
    for i in range(number):  
        print("post : ",post[i].text,"\n","location : ", location[i].text,"\n","link : ", driver.find_element(By.LINK_TEXT, str(post[i].text)).get_attribute("href"),"\n")  
        

 
driver.get("https://www.careerguide.com/career-options") 
elements = driver.find_elements(By.CLASS_NAME, "col-md-4") 
for value in elements:  
    field = value.find_elements(By.CLASS_NAME, "c-font-bold")  
    for value2 in field:
        #print(value2.text, ":")  
        element2 = value.find_elements(By.TAG_NAME, "ul")  
        #print(value.text, "<-")   
        for value3 in element2:  
            value4 = value3.text   
            value5 = value4.split('\n')
            for value6 in value5:
                #print(value5)  
                #print("going") 
                linked(value6) 
                print("\n"*2)

    print("\n"*3) 
    
driver.close()
        