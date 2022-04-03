from bs4 import BeautifulSoup

# with open('neweggScrape.html', 'r') as html_file: 
# default encoding didnt work 
# had to change encoding to "uft8"
with open('neweggScrape.html', encoding="utf8") as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml') #make html look better
    #print(soup.prettify())


    #courses_html_tags = soup.find_all('div')    # tags to look for
    #for course in courses_html_tags:            # find all tags
    #    print(course.text)

    #course_cards = soup.find_all('div', class_='item-info') # class_ not class
    #for course in course_cards:
    #    print(course.a)

    #div_apps = soup.find_all('div', id='app') # class_ not class
    #for apps in div_apps:
            