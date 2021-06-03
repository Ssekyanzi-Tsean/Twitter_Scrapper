
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
    url = 'https://twitter.com'
    markup = scrapy.get_raw_data(url)
    assert len(markup) > 100


def test_turn_to_soup():
    '''Test Soup Object Transformer'''
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
    soup_object = scrapy.turn_to_soup(multiline_markup)
    assert len(soup_object)


def test_get_twitter_link():
    html = """
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
    make_soup = scrapy.turn_to_soup(html)
    twitter = scrapy.get_twitter_link(make_soup)
    assert 'twitter' in twitter


def test_draw_company_url():
    html = """
    <!DOCTYPE html>
<html>
<body>
<h2>The target Attribute</h2>
<a href="https://www.twitter.com" target="_blank">Visit our HTML tutorial!</a>
<a href='https://t.co/'</a>
<a class="a-no-hover-decoration" href="https://twitter.com/MovitProductsUg?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;
url=https://twitter.com/MovitProductsUg%3Fref_src%3Dtwsrc%255Egoogle%257Ctwcamp%255Eserp%257Ctwgr%255Eauthor&amp;ved=2ahUKEwiRzpuFvfHwAhVITBoKHRdFCUUQ6F56BAgCEAI&amp;cshid=1622380378317895"><br><h3 class="NsiYH">Movit (@MovitProductsUg) · Twitter</h3><div class="V0XQK"><cite class="ellip iUh30">https://twitter.com/MovitProductsUg</cite></div></a>
<p>If you set the target attribute to "_blank", the link will open in a new browser window or tab.</p>
</body>
</html>"""

    make_soup = scrapy.turn_to_soup(html)
    match = scrapy.draw_company_url(make_soup)
    assert 't.co' in match


def test_get_email_address():
    html = """
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
    make_soup = scrapy.turn_to_soup(html)
    twitter = scrapy.get_twitter_link(make_soup)
    assert 'twitter' in twitter


def test_draw_company_url():
    html = """
    <!DOCTYPE html>
<html>
<body>
<h2>The target Attribute</h2>
<a href="https://www.twitter.com" target="_blank">Visit our HTML tutorial!</a>
<a href = "info@cafejavas.co.ug"
<a href='https://t.co/'</a>
<a class="a-no-hover-decoration" href="https://twitter.com/MovitProductsUg?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;
url=https://twitter.com/MovitProductsUg%3Fref_src%3Dtwsrc%255Egoogle%257Ctwcamp%255Eserp%257Ctwgr%255Eauthor&amp;ved=2ahUKEwiRzpuFvfHwAhVITBoKHRdFCUUQ6F56BAgCEAI&amp;cshid=1622380378317895"><br><h3 class="NsiYH">Movit (@MovitProductsUg) · Twitter</h3><div class="V0XQK"><cite class="ellip iUh30">https://twitter.com/MovitProductsUg</cite></div></a>
<p>If you set the target attribute to "_blank", the link will open in a new browser window or tab.</p>
</body>
</html>"""
    make_soup = scrapy.turn_to_soup(html)
    soup_object = scrapy.get_email_address(make_soup)
    assert 'Movit' in soup_object
