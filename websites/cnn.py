from bs4 import BeautifulSoup
import requests
from model.article import Article


def get_link() -> str:
    """
    This method extracts and builds a link for the most relevant article on https://edition.cnn.com/world
    Everything here is hardcoded.
    :return: A complete URL to an article
    """

    url = 'https://edition.cnn.com/world'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    h3 = soup.find('h3', class_='cd__headline')
    a = h3.find('a')
    path_of_article = a.get('href')

    # return without 'world' in the path
    return 'https://edition.cnn.com' + path_of_article


def parse_article() -> Article:
    """
    This function gets an article from the top of https://edition.cnn.com/world and parses it into the model.
    :return: Model of type Article
    """

    url = get_link()
    # For example:
    #url = 'https://edition.cnn.com/2020/01/03/business/carlos-ghosn-escape-jet/index.html'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    headline = soup.find('h1', class_='pg-headline').text
    date = soup.find('p', class_='update-time').text

    article_body = ''
    paragraphs = soup.find_all(class_='zn-body__paragraph')
    for paragraph in paragraphs:
        article_body += paragraph.text + '\n\n'

    article_model = Article(headline, article_body, "CNN", url, date)

    return article_model
