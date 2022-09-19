import requests

def parse_site(url):
   
   headers = {
      'accept': '*/*',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
      'Accept-Language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
      'referer': 'https://www.google.com/',
   }

   session = requests.Session()

   response = session.get(url, headers=headers)

   if response.status_code == 200:
      html = response.text
      return html

   return None

