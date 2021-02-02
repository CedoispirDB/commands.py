from googlesearch import search
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

query = "Martin Luther"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
