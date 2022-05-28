from bs4 import BeautifulSoup

with open("basic.html", "r") as html_file:
    content = html_file.read()
    
    # create soup object
    soup = BeautifulSoup(content, "lxml")
    # search the 1st tag and stop the execution there. Don't search the next others.
    tags = soup.find("h5")
    # return a list of all the tags we need
    courses_html_tags = soup.find_all("h5")
    
    # Next, we can do further operations with our selected tags
    for course in courses_html_tags:
        # return the text only (not the html content)
        print(course.text)
        

    print("\n")
    # you can filter the html content using class also
    course_cards = soup.find_all("div", class_="card")
    
    for course in course_cards:
        course_name = course.h5.text  # can search the tag by this method also
        course_price = course.a.text.split()[-1]

        print(f"{course_name} costs {course_price}")
