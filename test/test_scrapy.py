import scrapy


def test_readCompanyName():
    # Test Company Reader

    company_name = scrapy.readCompanyName()

    assert company_name == "unilever"
