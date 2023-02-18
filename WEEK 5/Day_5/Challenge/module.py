import time
import requests

def measure_req_completion_time(url):
    try:
        start = time.time()
        r = requests.get(url)
        roundtrip = time.time() - start
    except:
        print("Something is wrong with your url. Make sure ist starts with https:// or http://.")
    else:
        print(round(roundtrip, 2), 's')

url1 = 'https://api.chucknorris.io/jokes/random'
url2 = 'https://google.com'
url3 = 'http://google.com'
url4 = 'https://imdb.com'

for url in [url1, url2, url3, url4]:
    print(url)
    measure_req_completion_time(url)

while True:
    url = input("Enter a valid url (nothing to exit): ")
    if len(url) == 0:
        print("n\Program ends... Thanks for playing with us.\n")
        break
    measure_req_completion_time(url)