from ast import keyword
from bs4 import BeautifulSoup
import requests
import sys
import re #lib to ignore case

        #### current attributes ####
# 1) takes in a command line arg as a "keyword"
# 2) searches though product description for that keyword
# 3) ignores command line case
# 4) if match, prints product description and cost

        #### do this #####
# search specs of products using link on page, 
# build a db of some sort, then use a python web 
# framework to create and serve the web pages
listItems = []

def scrape(keyword):
    
    html_text = requests.get('https://www.newegg.com/todays-deals?cm_sp=Homepage_dailydeal-_--_-10272021&quicklink=true').text # url will go here
    soup = BeautifulSoup(html_text, 'lxml')
    element_table = soup.find('div', class_ = 'item-cells-wrap tile-cells five-cells')
    elements = element_table.find_all('div', class_ ='item-info')
    
    for this_element in elements:
        element_description = this_element.find('a', class_ = 'item-title').text
        #if keyword in element_description: #keyword = 'monitor'
        if re.search(keyword, element_description, re.IGNORECASE):
            element_price = this_element.find('ul').find('li', class_ = 'price-current').text
            
            # put all elements in a list then return the list
            listItems.append('{}\ncosts: {}\n'.format(element_description, element_price))

            

    if len(listItems) == 0:
        return "not found" 
    else:
        print ("list length: " , len(listItems))
        return listItems   
           



        