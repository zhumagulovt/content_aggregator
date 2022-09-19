from . import scrap_24kg, scrap_akipress, scrap_vesti

def parse():
    result = {

    }
    result['akipress'] = scrap_akipress.ScrapAkipress.as_scraper()
    result['24_kg'] = scrap_24kg.Scrap24kg.as_scraper()
    result['vesti'] = scrap_vesti.ScraperVesti.as_scraper()

    return result