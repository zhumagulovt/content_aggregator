from .base import Scraper


class ScraperVesti(Scraper):

    url = "https://vesti.kg"

    def get_main_news(self):
        result = []
        
        main_news = self.soup.find('ul', {'class': 'nspList active nspCol4'}).find_all('li')[:5]

        for news in main_news:
            result.append({
                'link': self.url + news.find('a').get('href'),
                'title': news.text
            })

        return result

    def get_latest_news(self):
        result = []

        latest_news = self.soup.find('div', {'id': 'itemListLeading'})\
            .find_all('div', {'class': 'itemBlock'})[:5]

        for news in latest_news:
            image = news.find('img')
            # print(image)
            title = news.find('div', {'class': 'itemBody'}).find('a').text.strip()
            # print(title)
            result.append({
                'time': news.find('span').text.strip()[13:],
                'image': self.url + news.find('img').get('data-src'),
                'link': self.url + news.find('div', {'class': 'itemBody'}).find('a').get('href'),
                'title': news.find('div', {'class': 'itemBody'}).find('a').text.strip(),
                'description': news.find('p').text
            })

        return result

