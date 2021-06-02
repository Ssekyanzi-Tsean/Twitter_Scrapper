from socket import SOL_UDP
from bs4 import BeautifulSoup
from selenium import webdriver
import scrapy


def test_read_company_name():
    ''' Test Company Reader'''

    company_name = scrapy.read_company_name()

    assert company_name == 'crestfoamuganda\n'


def test_google_search_handler():
    '''Test Google Search Results'''
    company_name = 'MovitProductsUg'
    company_link = scrapy.google_search_handler(company_name)
    assert company_link == 'https://www.google.com/search?q=MovitProductsUg'


def test_get_raw_data():
    '''Tests Get Raw Data'''
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    assert driver.quit


def test_turn_to_soup():
    '''Test Twitter Link Grabber'''
    multiline_markup = """
    <!DOCTYPE html>
<html>
<body>
<h2>The target Attribute</h2>
<a href="https://www.twitter.com" target="_blank">Visit our HTML tutorial!</a>
<a class="a-no-hover-decoration" href="https://twitter.com/MovitProductsUg?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;
url=https://twitter.com/MovitProductsUg%3Fref_src%3Dtwsrc%255Egoogle%257Ctwcamp%255Eserp%257Ctwgr%255Eauthor&amp;ved=2ahUKEwiRzpuFvfHwAhVITBoKHRdFCUUQ6F56BAgCEAI&amp;cshid=1622380378317895"><br><h3 class="NsiYH">Movit (@MovitProductsUg) · Twitter</h3><div class="V0XQK"><cite class="ellip iUh30">https://twitter.com/MovitProductsUg</cite></div></a>
<p>If you set the target attribute to "_blank", the link will open in a new browser window or tab.</p>
</body>
</html>"""
    soup = BeautifulSoup(multiline_markup, 'lxml')
    soup.get_text()
