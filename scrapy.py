from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup


def read_company_name(filename="companies.txt"):
    '''Reads in Company Name'''
    try:
        with open(filename, "r") as companies:
            pass
    except FileNotFoundError as err:
        print("Company File Not Found")
        print(f'key: {err}')
    else:
        with open(filename, "r") as companies:
            contents = companies.readlines()
            for lines in contents:
                return lines


def get_raw_data(url):
    '''Uses Selenium to get webpage and returns a Soup Object'''
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    data_page = soup.text
    return data_page


def google_search_handler(company_name):
    '''function forms google search link'''
    google_link = f'https://www.google.com/search?q={company_name}'
    return google_link


def get_twitter_link(soup):
    '''Pulls out The Twitter Link out of the Google Search Soup Object'''

    for link in soup.findAll('a', attrs={'href': re.compile("a")}):
        href = link.get('href')
        if "twitter" in href:
            return href


def draw_company_url(soup):
    '''Gets Company Url Out of Twitter SOup Object'''
    for link in soup.findAll('a', {'href': re.compile(r'https://t.co/')}):
        match = link.get('href')
        return match


def get_email_address(soup):
    '''Gets the Email Link out of our Soup Object'''
    for company_email in soup.find_all("a"):
        if "@" in company_email.text:
            return company_email.text
    return company_email


def write_company_contact(company_email, company_name):
    ''' writes contact information to a txt file'''
    company_name = company_name.strip()
    info = f"{company_name}:{company_email}"
    contact = info.strip()
    with open("contactinfo.txt", "a") as contactinfo:
        contactinfo.write(contact)
