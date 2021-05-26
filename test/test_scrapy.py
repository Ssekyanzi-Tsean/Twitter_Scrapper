import scrapy


def test_readCompanyName():
    # Test Company Reader

    company_name = scrapy.readCompanyName()

    assert company_name == 'unilever'


def test_compose_twitter_handler():
    # Twitter Link Composer
    company_name = 'glovo'
    twitter_url = scrapy.compose_twitter_handler(company_name)
    assert twitter_url == 'https://twitter.com/glovo?'
