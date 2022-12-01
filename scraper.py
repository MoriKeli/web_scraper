from bs4 import BeautifulSoup
import requests

with open('index.html') as html:
    soup = BeautifulSoup(html, 'lxml')


# print in an pretty format
# print(soup.prettify())

# grab info from html file
# match = soup.title
# print(match)

# Get the text of a given tag
# match = soup.title.text
# print(match)

# using find method

# using html class attribute
# match = soup.find('div', class_='navbar-nav')   # class_ is used to avoid conflicts since "class" is a keyword in Python

# using html id attribute
# match = soup.find('div', id='navbarToggle')
# print(match)

# Grabbing an article headline
# article = soup.find('div', class_='col-12')
# headline = article.h2
# article_content = article.p
# print(headline)
# print(article_content)


# looping through all articles
# for article in soup.find_all('div', class_='col-12'):
#     headline = article.h2
#     article_content = article.p
#     print(f'Article headline: {headline}')
#     print(f'Content: {article_content}')
#     print()

