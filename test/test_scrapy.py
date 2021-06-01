import scrapy


def test_read_company_name():
    ''' Test Company Reader'''

    company_name = scrapy.read_company_name()

    assert company_name == 'crestfoamuganda\n'


def test_get_raw_data():
    '''Test Selenium Raw Data'''
    movit_url = 'https://t.co/dhCPLeZcms?amp=1'
    movit_data = scrapy.get_raw_data(movit_url)
    assert len(movit_data) == 1


# def test_compose_twitter_handler():
#     ''' Twitter Link Composer'''
#     company_name = 'glovo'
#     twitter_url = scrapy.compose_twitter_handler(company_name)
#     assert twitter_url == 'https://twitter.com/glovo?'


# def test_edit_link_to_contact():
#     ''' forms a contact link to the company website'''
#     company_name = 'cafejavas'
#     contact_link = scrapy.edit_link_to_contact(company_name)
#     assert contact_link == 'https://www.cafejavas.com/contact/'
