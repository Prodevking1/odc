""" from django.shortcuts import render """

# Create your views here.

# key : Watpu19KBdOjaSv1JtbDxiWso
# key secret Kkj5sCqDymRdFM8dbS4g9BvQYmestK5vKuvhs6NpT40SMQJvMh
# acces token 1470856098387222537-AEuicyiG10ZlmCAe6sZPYSeQcE8Enc
# acces token key PI5MnYbtiwsHY53ztke5baQXc7EsXsiSJiSs2HvRxsG3f
# bearer token AAAAAAAAAAAAAAAAAAAAAMbHlAEAAAAA6BOO2FXn4CxLakgb%2FNh5XglaOII%3DOopz46XfU8Qudxdh2eNF4OiwIz15bNLycq3OiICxKJh
from django.shortcuts import render
from requests_oauthlib import OAuth1
import requests as req

from twitter import Twitter, OAuth


api = Twitter(
    consumer_key="Watpu19KBdOjaSv1JtbDxiWso",
    consumer_secret="Kkj5sCqDymRdFM8dbS4g9BvQYmestK5vKuvhs6NpT40SMQJvMh",
    access_token_key="1470856098387222537-nEpfMAJrB8BB5nEhHJXXwuswoEZbeW",
    access_token_secret="s0rkaZ95wC8COK1RVzbiOJB6xzhn8YfnoTncrDaSbIPVF",
)


query = ""
items_count = 10

tweets = api.GetSearch(term=query, count=items_count)
results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100"
)
for tweet in results:
    print(tweet.text)


def search(request):
    return render(request, "search.html")


def view_tweets(request):
    tweets = [
        {
            "id": "tweet-1",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, mauris at suscipit congue.",
        },
        {
            "id": "tweet-2",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, mauris at suscipit congue.",
        },
    ]
    return render(request, "view.html", {"tweets": tweets})
