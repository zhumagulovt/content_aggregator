from . import scrap_24kg, scrap_akipress

def parse():
    result = {}
    result['24_kg'] = scrap_24kg.Scrap24kg().get_news()
    result['akipress'] = scrap_akipress.ScrapAkipress().get_news()
    return result