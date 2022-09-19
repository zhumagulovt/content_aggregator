from .base import Scraper


class Scrap24kg(Scraper):

    url = "https://24.kg"

    def get_main_news(self):
        result = []

        main_news = self.soup.find('div', {'class': 'mainNewsList'}).find_all('div')

        for news in main_news:
            result.append({
                'link': self.url + news.a.get('href'),
                'title': news.span.text
            })
        return result

    def get_latest_news(self):
        result = []

        latest_news = self.soup.find('div', {'id': 'newslist'}).find_all('div', {'class': 'one'})[:10]

        for news in latest_news:

            time = news.find('div', {'class': 'time'}).text
            title_div = news.find('div', {'class': 'title'})

            result.append({
                'time': time,
                'link': self.url + title_div.a.get('href'),
                'title': title_div.a.text
            })
        return result

# def scrap():
    # return Scrap_24kg().

# from bs4 import BeautifulSoup as Bs

# from .client import parse_site

# URL = "https://24.kg/"

# def scrap():
    
#     html = parse_site(URL)
#     host = "https://24.kg"

#     soup = Bs(html, 'html.parser')
    
#     result = {
#         'main_news': [],
#         'latest_news': []
#     }
#     # Main news
#     main_news = soup.find('div', {'class': 'mainNewsList'})

#     # Scrap every div from mainNewsList
#     for news in main_news.find_all('div'):
#         result['main_news'].append({
#             'link': host + news.a.get('href'),
#             'title': news.span.text
#         })

#     # Latest news

#     latest_news = soup.find('div', {'id': 'newslist'})

#     all_latest_news = latest_news.find_all('div', {'class': 'one'})[:10]

#     for news in all_latest_news:

#         time = news.find('div', {'class': 'time'}).text
#         title_div = news.find('div', {'class': 'title'})

#         result['latest_news'].append({
#             'time': time,
#             'link': host + title_div.a.get('href'),
#             'title': title_div.a.text
#         })

#     return result
