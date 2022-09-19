from . import scrap_24kg, scrap_akipress

def parse():
    result = {}
    result['24_kg'] = scrap_24kg.scrap()
    result['akipress'] = scrap_akipress.scrap()
    return result