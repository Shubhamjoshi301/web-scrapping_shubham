from selenium import webdriver
# import sys
import re
import time
import os
from requests import get

def real_site(gd_links):
    
    
    if (gd_links.find('intercelestial.com/') != -1):
        ip = get('https://api.ipify.org').text
        os.startfile(r'C:\Users\91735\Downloads\psiphon3.exe')
        while (get('https://api.ipify.org').text == ip):
            pass
    browser = webdriver.Firefox()    
    browser.get(gd_links)
    # if (gd_links.find('intercelestial.com/') != -1):
    #     time.sleep(30)
    #     site_name = re.search('https://(.+?)/wp-content/uploads/2019/09/button_im-not-a-robot.png',browser.page_source).group(1)
    #     link_elem = browser.find_element_by_css_selector('img["src="https://' + site_name + '/wp-content/uploads/2019/09/button_im-not-a-robot.png"]')


    # else:
    time.sleep(30)
    # print(browser.page_source)
    site_name = re.search('https://(.+?)/wp-content/uploads/2019/09/button_im-not-a-robot.png',browser.page_source).group(1)
    # site_name = site_name.group(1)
    # print(site_name)
    #link_elem = browser.search_element_by_css_selector('img[src="https://'+ site_name +'/wp-content/uploads/2019/09/button_im-not-a-robot.png"]')
    #link_elem = browser.search_element_by_css_selector('img[src="https://'+ site_name +'/wp-content/uploads/2019/09/button_im-not-a-robot.png"]')
    # link_elem = browser.find_element_by_css_selector('img[src="https:// '+ site_name +' /wp-content/uploads/2019/09/button_im-not-a-robot.png"]')
    link_elem = browser.find_element_by_css_selector('img[src="https://' + site_name + '/wp-content/uploads/2019/09/button_im-not-a-robot.png"]')
    link_elem.click()
    time.sleep(10)
    link_elem1 = browser.find_element_by_css_selector('img[src="https://' + site_name + '/wp-content/uploads/2019/09/button_generate-link.png"]')
    link_elem1.click()
    time.sleep(5)
    link_elem2 = browser.find_element_by_css_selector('img[src="https://' + site_name + '/wp-content/uploads/2019/09/button_download.png"]')
    link_elem2.click()
    time.sleep(10)
    main_window = browser.current_window_handle
    for window_handle in browser.window_handles:
        if window_handle != main_window:
            browser.switch_to_window(window_handle)
            break
    time.sleep(15)
    print(browser.current_url)
    # return browser.current_url
    browser.get("https://drive.klop.me/file/8925cc")
    link_elem3 = browser.find_element_by_link_text('Continue')
    link_elem3.click()
    time.sleep(10)
