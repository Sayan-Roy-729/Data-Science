"""
In this code, we are trying to open the https://learnwith.campusx.in website using Selenium. For that, at first we
have chose the drive (here it is chrome driver) which helps to open the browser. After that, using selenium we are
trying to open the Google Search page for Google Search Engine. Here using selenium have types a word "Campusx" and
hit enter. From the search results, we choose our required website. After opening the website, there is a button
"Join the program", so clicked that using the Selenium.

Date: 01/02/2023
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import utils  # Import the driver ready code


# open the browser and the Google Search page
driver = utils.browser_function()
# from the Google home page, go to the search box html code and copy the XPath.

# this is because to make a delay to load the webpage
time.sleep(2)

# fetch the search input box using the XPath
user_input = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div["
                                                    "2]/input")
# in the search field, fill up what you want to search, for our case "Campusx"
user_input.send_keys("Campusx")

# again a delay
time.sleep(1)

# now hit the enter
user_input.send_keys(Keys.ENTER)

# again make a short delay
time.sleep(2)

# now click on our required link, so, the website will be opened
link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a')
link.click()

# again try to click on the "Join the program" button
join_program_button = driver.find_element(by=By.XPATH, value='//*[@id="1668425005116"]/span[2]/a')
join_program_button.click()
