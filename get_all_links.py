from bs4 import BeautifulSoup


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    spans = soup.find_all('div', class_='col-md-12 news-item')
    links = []
    for span in spans:
        a = span.find('a').get('href')
        link = 'http://www.volgograd.ru' + a
        links.append(link)

    return links
