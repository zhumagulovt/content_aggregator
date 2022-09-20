from .base import Scraper


class ScrapKaktus(Scraper):

    url = "https://kaktus.media"

    def get_main_news(self):
        result = []

        main_news = self.soup.find('div', {'class': 'Dashboard--group-boards'})\
                            .find_all('a', 
                            {'class': lambda x: x in [
                                                        'Dashboard-Content-Card--name', 
                                                        'Dashboard-Content-LineBig--name'
                                                    ]
                            })[:5]

        for news in main_news:
            result.append({
                'link': news.get('href'),
                'title': news.text.strip()
            })
        return result
    
    def get_latest_news(self):

        self.make_request('/?lable=8&date=2022-09-20&order=time')

        result = []

        latest_news = self.soup.find_all('div', {'class': 'ArticleItem'})[:5]

        for news in latest_news:

            result.append({
                'time': news.find('div', {'class': 'ArticleItem--time'}).text.strip(),
                'link': 'https:' + news.find('a', {'class': 'ArticleItem--name'}).get('href'),
                'title': news.find('a', {'class': 'ArticleItem--name'}).text.strip()
            })

        return result