import time
from selenium import webdriver         
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {'download.default_directory': '/home/cjw/Downloads'})

driver = webdriver.Chrome('/home/cjw/Desktop/chromedriver') 
driver.get('https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=441')

export = driver.find_element_by_xpath('/html/body/div/button')
export.click()
time.sleep(5)
driver.close()
