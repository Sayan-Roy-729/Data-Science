from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def browser_function(url="https://www.google.com"):
    # define the driver path
    driver_path = Service("../drivers/chromedriver.exe")
    # set the different options for the browser
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # ignore the certificate and SSL errors
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    # maximize the browser window
    chrome_options.add_argument("start-maximized")
    # define with the driver and open the browser
    chrome_driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    # open the Google search page, for Google search engine
    chrome_driver.get(url)
    # then return the driver object
    return chrome_driver
