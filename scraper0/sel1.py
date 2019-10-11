from selenium import webdriver
# Using Chrome to access web
options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=C:/home/cjw/Desktop/chromedriver") # Set the download Path
driver = webdriver.Chrome(options=options)
# Open the website
try:
    driver.get('https://iwf.net/new_bw/results_by_events/?event=472/') # Your Website Address
    password_box = driver.find_element_by_xpath('//*[@id="cleft"]/div[2]/iframe')
    password_box.send_keys('xxxx') #Password
    download_button = driver.find_element_by_class_name('link_w_pass')
    download_button.click()
    driver.quit()
except:
    driver.quit()
    print("Faulty URL")