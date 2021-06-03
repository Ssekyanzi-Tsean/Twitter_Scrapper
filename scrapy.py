
from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup


def read_company_name(filename="companies.txt"):
    '''Reads in Company Name'''
    try:
        with open(filename, "r") as companies:
            contents = companies.readlines()
            for lines in contents:
                return lines
    except FileNotFoundError as err:
        print("Company File Not Found")
        print(f'key: {err}')
    else:
        pass


def get_raw_data(url):
    '''Uses Selenium to get webpage and returns a Soup Object'''
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(10)
        html = driver.page_source
        driver.quit()

        return html
    except TypeError as err:
        print(f'key:{err}')
        print("No link Found")
    except Exception as err:
        print(f'key:{err}')
        print("Company Missing Element")
    else:
        pass


def turn_to_soup(html):
    '''Takes get raw function from Selenium and turns it to Soup Object'''
    try:
        soup = BeautifulSoup(html, 'lxml')

        return soup
    except Exception as err:
        print(f'key:{err}')
        print("Company Missing Element")
    else:
        pass


def google_search_handler(company_name):
    '''function forms google search link'''
    try:
        google_link = f'https://www.google.com/search?q={company_name}'
    except TypeError as err:
        print(f'key:{err}')
        print("No link Found")
    else:
        return google_link


def get_twitter_link(soup):
    '''Pulls out The Twitter Link out of the Google Search Soup Object'''
    try:
        for link in soup.findAll('a', attrs={'href': re.compile("a")}):
            href = link.get('href')
            if "twitter" in href:
                return href
    except TypeError as err:
        print(f'key: {err}')
        print('Twitter Link Not Found')
    except Exception as err:
        print(f'key: {err}')
        print("Something Went Wrong")
    else:
        pass


def draw_company_url(soup):
    '''Gets Company Url Out of Twitter SOup Object'''
    try:
        for link in soup.findAll('a', {'href': re.compile(r'https://t.co/')}):
            match = link.get('href')
            return match
    except Exception as err:
        print(f'key:{err}')
    else:
        pass


def get_email_address(soup):
    '''Gets the Email Link out of our Soup Object'''
    try:
        for company_email in soup.find_all("a"):
            if "@" in company_email.text:
                return company_email.text
    # return company_email

    except Exception as err:
        print(f'key:{err}')
    else:
        pass


def write_company_contact(company_email, company_name):
    ''' writes contact information to a txt file'''
    try:
        company_name = company_name.strip()
        info = f"{company_name}:{company_email}"
        contact = info.strip()
        with open("contactinfo.txt", "a") as contactinfo:
            contactinfo.write(contact)
    except Exception as err:
        print(f'key:{err}')
    else:
        pass
