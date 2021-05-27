import scrapy

company_name = scrapy.read_company_name()

company_names = ['airtel']

for company_name in company_names:

    twitter_link = scrapy.get_raw_data(company_name)

    twitter_markup = scrapy.get_twitter_page(twitter_link, company_name)

    contact_website_link = scrapy.edit_link_to_contact(company_name)

    company_email = scrapy.get_company_website(contact_website_link)

    scrapy.write_company_contact(company_email, company_name)
