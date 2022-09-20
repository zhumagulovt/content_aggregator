from . import akipress, vesti, _24kg, kaktus

def parse():
    result = {}
    result['akipress'] = akipress.ScrapAkipress.as_scraper()
    result['24_kg'] = _24kg.Scrap24kg.as_scraper()
    result['vesti'] = vesti.ScraperVesti.as_scraper()
    result['kaktus'] = kaktus.ScrapKaktus.as_scraper()

    return result