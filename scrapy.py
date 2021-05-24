def readCompanyName(filename="companies.txt"):
    with open(filename, "r") as companies:
        for company in companies:
            return company


def getRawData(company_name):
    searchUrl = f'https://www.google.com/search?q={company_name}'
