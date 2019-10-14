import functions
import webpages
import webbrowser
import real_weppage

from functions import makeurl
movie_name = functions.takeinput()
url = functions.makeurl(movie_name)
# webbrowser.open(url)
html = webpages.requests_webpage(url)
parsed_html = webpages.parse_html(html)
# print(parsed_html)
webpages.create_movie_database(parsed_html)
[movie_names,movie_links]=webpages.create_movie_database(parsed_html)
# print(movie_links)
choice = functions.menu(movie_names)
html2 = webpages.requests_webpage(movie_links[int(choice)-1])
parsed_html2 = webpages.parse_html(html2)
links=webpages.click_gd(parsed_html2)
real_weppage.real_site(links)









# print(url)



# import webbrowser
# import requests


# webbrowser.open("http://www.google.com")
# requests.get("https://www.google.com")


# print(makeurl("iron man"))