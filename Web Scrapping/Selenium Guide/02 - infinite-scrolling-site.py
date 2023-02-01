from utils import browser_function
import time

# open the browser and the site
driver = browser_function(url="https://www.ajio.com/men-backpacks/c/830201001")

### scroll the site by using the driver
# Get the height of your browser window by executing JS code
old_height = driver.execute_script('return document.body.scrollHeight')
# also notes how many times we have scrolled
counter = 1

# now scroll the page
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # # make a short delay
    time.sleep(5)

    # again measure the height
    new_height = driver.execute_script('return document.body.scrollHeight')
    # increase our counter by 1
    counter += 1
    # print the heights and the counter
    print(new_height, old_height, counter)

    # check is there any (dynamic )scrolling left
    if new_height == old_height:
        break

    # change the old height will help for the next iteration
    old_height = new_height


# when our scrolling will end, grab the html code of that page
html = driver.page_source
# now save the file
with open("ajio.html", "w", encoding="utf-8") as f:
    f.write(html)
