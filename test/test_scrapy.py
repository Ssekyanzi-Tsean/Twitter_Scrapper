import scrapy


def test_read_company_name():
    ''' Test Company Reader'''

    company_name = scrapy.readCompanyName()

    assert company_name == 'unilever'


def test_compose_twitter_handler():
    ''' Twitter Link Composer'''
    company_name = 'glovo'
    twitter_url = scrapy.compose_twitter_handler(company_name)
    assert twitter_url == 'https://twitter.com/glovo?'


def test_edit_link_to_contact():
    ''' forms a contact link to the company website'''
    company_name = 'cafejavas'
    contact_link = scrapy.edit_link_to_contact(company_name)
    assert contact_link == 'https://www.cafejavas.com/contact/'
