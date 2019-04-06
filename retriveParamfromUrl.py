import urllib.parse as urlparse
url = 'https://api.whatsapp.com/send?phone=919750913023&text=HareKrishna!'
parsed = urlparse.urlparse(url)
print(urlparse.parse_qs(parsed.query)['text'])