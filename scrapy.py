from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup


def readCompanyName(filename="companies.txt"):
    with open(filename, "r") as companies:
        for company in companies:
            return company


def getRawData(company_name):
    searchUrl = f'https://www.google.com/search?q={company_name}'

    driver = webdriver.Chrome()

    driver.get(searchUrl)
    time.sleep(15)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.findAll('a', attrs={'href': re.compile("a")}):
        href = link.get('href')
        if "twitter" in href:
            return href


def compose_twitter_handler(company_name):
    twitter_url = f'https://twitter.com/{company_name}?'
    return twitter_url


def get_twitter_page(twitter_url, company_name):
    driver = webdriver.Chrome()
    driver.get(twitter_url)
    time.sleep(15)
    html = driver.page_source
    company_link = (
        driver.find_element_by_partial_link_text(company_name).text)
    driver.quit
    return company_link


def edit_link_to_contact(company_name):
    new_company_link = f'https://www.{company_name}.com/contact/'
    return new_company_link


def get_company_website(new_company_link):
    driver = webdriver.Chrome()
    driver.get(new_company_link)
    time.sleep(15)
    company_data = driver.page_source
    company_email = (driver.find_element_by_partial_link_text('@').text)
    return company_email


def writeCompanyContact(company_email, company_name):

    companyName = company_name.strip()
    info = f"{companyName}:{company_email}"
    contact = info.strip()
    with open("contactinfo.txt", "w") as contactinfo:
        contactinfo.write(contact)
