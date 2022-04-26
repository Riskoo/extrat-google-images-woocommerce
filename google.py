from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
file=csv.reader(open('andaluza.csv'), delimiter=',')
f = open('google.csv', 'w')
for line in file:
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q='+line[0]+'brida&tbm=isch&ved=2ahUKEwjfpuiWz7H3AhVT_IUKHfJoBIwQ2-cCegQIABAA&oq=brida&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAELEDEEM6CggAELEDEIMBEEM6BAgAEEM6CwgAEIAEELEDEIMBOggIABCxAxCDAVCuCljQTmDzUGgAcAB4AIABQogB3AKSAQE2mAEAoAEBqgELZ3dzLXdpei1pbWewAQDAAQE&sclient=img&ei=o9ZnYp_JBdP4lwTy0ZHgCA&bih=1248&biw=1251&client=safari')
    title =  driver.find_elements(By.XPATH,'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    
    f.write(line[0]+','+line[1]+','+title[0].get_attribute('src')+'\n')

f.close()
