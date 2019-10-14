import requests
from bs4 import BeautifulSoup as bs


def requests_webpage(link):
    a = requests.get(link)
    return a

def parse_html(html):
    parsed_html = bs(html.text, features = 'html.parser')
    return parsed_html

def create_movie_database(parsed_html):
    elements = parsed_html.select('.post-box-title a')
    movie_links=[]
    movie_names=[]
    for element in elements:
        movie_names.append(element.getText())
        movie_links.append(element.get('href'))
    # print(movie_names)
    # print(movie_links)
    return[movie_names,movie_links]
def click_gd(parsed_html2):
    elements = parsed_html2.select(".purple")
    
    return elements[-1].get('href')

    


