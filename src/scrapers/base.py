from bs4 import BeautifulSoup

from .client import parse_site

class Scraper:

    url = None

    soup = None

    def __init_subclass__(cls) -> None:
        # Create BeautifulSoup when new Scraper class was inherited
        url = cls.url
        html = parse_site(url)
        cls.soup = BeautifulSoup(html, 'html.parser')

    def make_request(self, path):
        """Make second request and update soup"""
        url = self.url
        html = parse_site(url + path)
        self.soup = BeautifulSoup(html, 'html.parser')

    @classmethod
    def as_scraper(cls, **kwargs):
        """"""
        def scrap():
            self = cls()
            return self.get_news()
        
        return scrap()

    def get_main_news(self):
        """Get list of main or popular news"""

        return None

    def get_latest_news(self):
        """Get list of latest news"""

        return None

    def get_news(self):
        """Return a dict with main and latest news"""

        result = {}
        result['main_news'] = self.get_main_news()
        result['latest_news'] = self.get_latest_news()
        # print()
        return result
