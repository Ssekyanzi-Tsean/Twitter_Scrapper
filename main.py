import scrapy

company_name = scrapy.readCompanyName()

twitter_link = scrapy.getRawData(company_name)

twitter_markup = scrapy.get_twitter_page(twitter_link, company_name)

contact_website_link = scrapy.edit_link_to_contact(company_name)

company_email = scrapy.get_company_website(contact_website_link)

scrapy.writeCompanyContact(company_email, company_name)
