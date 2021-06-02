import scrapy

company_name = scrapy.read_company_name()


# company_names = ['airtel']

# for company_name in company_names:

linker = scrapy.google_search_handler(company_name)

html_object = scrapy.get_raw_data(linker)

soup_object = scrapy.turn_to_soup(html_object)

twitter_link = scrapy.get_twitter_link(soup_object)

twitter_page = scrapy.get_raw_data(twitter_link)


twitter_soup = scrapy.turn_to_soup(twitter_page)
company_url = scrapy.draw_company_url(twitter_soup)

company_mark_up = scrapy.get_raw_data(company_url)
company_soup_object = scrapy.turn_to_soup(company_mark_up)


company_email = scrapy.get_email_address(company_soup_object)
print(company_email)
scrapy.write_company_contact(company_email, company_name)
