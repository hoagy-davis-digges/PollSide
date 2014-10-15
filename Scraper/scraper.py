import urllib
import urllib2

from bs4 import BeautifulSoup
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Scraper.pdf_scrapers import *


def login:
    browser = webdriver.Chrome()
    browser.get('https://scraperwiki.com/login')
    browser.find_element_by_id('username').send_keys(settings.SCRAPERWIKI_USERNAME)
    browser.find_element_by_id('password').send_keys(settings.SCRAPERWIKI_PASSWORD + Keys.RETURN)


def pollster_iterator
    for pollster in Pollster.objects:
        main_page = urllib2.urlopen(pollster.base_url+pollster.poll_home)
        soup = BeautifulSoup(main_page)
        for x in soup.find_all(pollster.poll_regex):
            poll_page_link = x.get('href')
            if not Poll.objects.get(url=poll_page_link):
                poll_page = urllib2.urlopen(pollster.base_url+poll_page_link)
                poll_soup = BeautifulSoup(poll_page)
                pdf_page = poll_soup.find(pollster.pdf_regex).get('href')
                scraperwiki(pdf_page, pollster, poll_page_link)

def scraperwiki(document_address, pollster, poll_page_link):
    browser.get('https://scraperwiki.com/datasets')
    browser.find_element_by_class_name('new-dataset-tile').click()
    browser.find_element_by_class_name('table-xtract').click()
    browser.switch_to.frame('easyXDM_default6171_provider')
    browser.switch_to.frame('toolContent')
    browser.find_element_by_id('source-url').send_keys(pdf_page + Keys.RETURN)
    browser.find_element_by_css_selector('[data-toolname=spreadsheet-download]')
    browser.switch_to.frame('easyXDM_default6175_provider')
    browser.switch_to.frame('toolContent')
    soup = BeautifulSoup(browser.page_source)
    tag = soup.find('a', class_='xlsx')
    link = tag['href']
    downloaded_file = (urllib.urlretrieve(link))[0]
    pollster_function[pollster.name](downloaded_file, poll_page_link)

pollster_function = {'YouGov': yougov}


