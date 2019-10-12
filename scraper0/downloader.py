from csv import reader
import time
from selenium import webdriver         
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#add headless mode


def main(handler):
    with open('/home/cjw/Documents/scraper/scraper0/old_bw_2018.csv') as file:       #old_bw_2018.csv or new_bw_2019.csv
        start_urls = [line.strip() for line in file]
        driver = webdriver.Chrome('/home/cjw/Desktop/chromedriver') 
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {'download.default_directory': '/home/cjw/Downloads/iwf_results'})
        for row in handler:
            driver.get(str(row[0]))
            export = driver.find_element_by_xpath('/html/body/div/button')
            export.click()
            time.sleep(5)



if __name__ == '__main__':
    with open('/home/cjw/Documents/scraper/scraper0/old_bw_2018.csv') as file:       #old_bw_2018.csv or new_bw_2019.csv
        handler = reader(file)
        next(handler,None)
        main(handler)