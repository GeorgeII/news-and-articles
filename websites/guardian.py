from bs4 import BeautifulSoup
import requests
from model.article import Article


def get_link() -> str:
    """
    This method extracts and builds a link for the most relevant article on https://www.theguardian.com/international
    Everything here is hardcoded.
    :return: A complete URL to an article
    """

    url = 'https://www.theguardian.com/international'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h3 = soup.find('h3', class_='fc-item__title')
    a = h3.find('a')
    path_of_article = a.get('href')

    return path_of_article


def parse_article() -> Article:
    """
    This function gets an article from the top of 'https://www.theguardian.com/international' and parses it into the model.
    :return: Model of type Article
    """

    url = get_link()
    # For example:
    #url = 'https://www.theguardian.com/world/2020/jan/05/donald-trump-vows-to-hit-52-sites-very-hard-if-iran-retaliates-for-suleimani-killing'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    headline = soup.find('h1', class_='content__headline').text
    date = soup.find('time', class_='content__dateline-wpd')["datetime"]

    article_body = ''
    paragraphs = soup.find(class_='content__article-body').find_all('p')
    for paragraph in paragraphs:
        article_body += paragraph.text + '\n\n'

    article_model = Article(headline, article_body, "Guardian", url, date)

    return article_model
