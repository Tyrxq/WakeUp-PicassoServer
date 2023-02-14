from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''This is a load page strategy so my fuctions excute faster instead of waiting for the whole page to load'''
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"  #  complete


''' 
This how I interact with Chome using their drivers I downloaded on my local device.
Drivers will need to be replaced when Chrome updates again.  
'''
chromeDriverPath = r'C:\Program Files (x86)\chromedriver.exe'
#chromeDriver = webdriver.Chrome(chromeDriverPath)
chromeDriver = webdriver.Chrome(desired_capabilities=caps, executable_path=chromeDriverPath)
