from src.scrapers import 24kg
from . import akipress, vesti, _24kg

def parse():
    result = {}
    result['akipress'] = akipress.ScrapAkipress.as_scraper()
    result['24_kg'] = _24kg.Scrap24kg.as_scraper()
    result['vesti'] = vesti.ScraperVesti.as_scraper()

    return result