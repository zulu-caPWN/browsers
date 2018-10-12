from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


###########
# Browser #
###########
binary = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp,
                           executable_path=r'C:\Users\PK\Desktop\VM_Shared_Folder\01Jan\upload_vid_youtube\geckodriver.exe')
wait = WebDriverWait(driver,20)
print 'Starting Browser'
