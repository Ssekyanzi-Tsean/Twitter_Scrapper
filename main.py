import scrapy

company_name = scrapy.read_company_name()


# company_names = ['airtel']

# for company_name in company_names:

#     twitter_link = scrapy.get_raw_data(company_name)

#     twitter_markup = scrapy.get_twitter_page(twitter_link, company_name)

#     contact_website_link = scrapy.edit_link_to_contact(company_name)

#     company_email = scrapy.get_company_website(contact_website_link)

#     scrapy.write_company_contact(company_email, company_name)

linker = scrapy.google_search_handler(company_name)

soup_object = scrapy.get_raw_data(linker)

twitter_link = scrapy.get_twitter_link(soup_object)
print(twitter_link)
twitter_page = scrapy.get_raw_data(twitter_link)

company_url = scrapy.draw_company_url(twitter_page)
print(company_url)
company_mark_up = scrapy.get_raw_data(company_url)
company_email = scrapy.get_email_address(company_mark_up)
scrapy.write_company_contact(company_email, company_name)
