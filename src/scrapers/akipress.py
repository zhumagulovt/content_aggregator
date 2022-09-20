from .base import Scraper


class ScrapAkipress(Scraper):

    url = "https://akipress.org/"

    def get_main_news(self):
        result = []

        main_news = self.soup.find('div', {'id': 'block-mainnews'}).\
                            find_all('div', {'class': lambda x: x and (
                                x.startswith('nowr_bigimg_elem' or x.startswith('nowr_elem'))
                            )})[:5]

        for news in main_news:
            result.append({
                'time': news.find('div', {'class': 'nowr_date'}).text.strip()[:5],
                'link': news.find('a').get('href'),
                'title': news.find('a').text.strip()
            })
        return result
    
    def get_latest_news(self):
        result = []

        latest_news_table = self.soup.find('table', attrs={'class': 'sections section-last'})

        latest_news = latest_news_table.find_all('tr', {
            'class': lambda x: x and x.startswith('js'),
            'style': lambda x: x != 'display:none;'
        })[:10]

        for news in latest_news:

            result.append({
                'time': news.find('td', {'class': 'datetxt'}).text.strip(),
                'link': 'https:' + news.find('a').get('href'),
                'title': news.find('a').text.strip()
            })

        return result

# from bs4 import BeautifulSoup as Bs

# from .client import parse_site

# URL = "https://akipress.org/"

# def scrap():
    
#     html = parse_site(URL)
#     news_max = 10

#     soup = Bs(html, 'html.parser')
    
#     result = {
#         'main_news': [],
#         'latest_news': []
#     }

#     # Main news
#     main_news = soup.find('div', {'id': 'block-mainnews'}).\
#                         find_all('a', {'class': 'topaddlink'})[:5]
#     for news in main_news:

#         result['main_news'].append({
#             'time': news.span.text,
#             'link': news.get('href'),
#             'title': news.text[6:]
#         })

#     # Latest news
    # latest_news_table = soup.find('table', attrs={'class': 'sections section-last'})
    # latest_news = latest_news_table.find_all('tr', {
    #     'class': lambda x: x and x.startswith('js'),
    #     'style': lambda x: x != 'display:none;'
    # })[:10]

    # for news in latest_news:

    #     result['latest_news'].append({
    #         'time': news.find('td', {'class': 'datetxt'}).text.strip(),
    #         'link': 'https:' + news.find('a').get('href'),
    #         'title': news.find('a').text.strip()
    #     })

    # return result