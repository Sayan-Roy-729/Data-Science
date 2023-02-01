from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

from utils import browser_function

# Constants
delay = 3  # make delay upto 3 seconds

# open the browser and the SpartPrix website
driver = browser_function(url="https://www.smartprix.com/")

# click on the mobile tab to go to the mobile page
driver.find_element(by=By.XPATH, value='/html/body/div[1]/nav/ul/li[1]/a').click()

time.sleep(2)

# from the filters (left side available), grap the options "availability" -> "Exclude out of stock"
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()

time.sleep(2)

# similar also, check the "Exclude Upcoming" option from the "availability"
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/aside/div/div['
                                                                             '5]/div[2]/label[2]/input'))).click()

# until all the phones are not loaded, continue to load the page
old_height = driver.execute_script("return document.body.scrollHeight")
# count how many times we have scrolled
count = 1
while True:
    # Now we got our desired page. Now have to load all the data. For that have to click the button "Load More"
    try:
        button_xpath = '//*[@id="app"]/main/div[1]/div[2]/div[3]'
        driver.find_element(by=By.XPATH, value=button_xpath).click()
        time.sleep(delay)  # short delay

        # calculate the new height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # the old height is same with the new height, then it seems that no scrolling is possible
        if old_height == new_height:
            break

        print(old_height, new_height, count)

        # now store the new height as the old height
        old_height = new_height
        # also increase the count number
        count += 1

    except TimeoutException:
        print("Took too much time to click the button 'Load More'")
    except Exception as e:
        print(e)

# while all the content of the page loaded; save that in a html file
with open("smartprix-mobiles.html", "w", encoding="UTF-8") as f:
    f.write(driver.page_source)
