import twitter

api = twitter.Api(
    consumer_key='sP2OWvPIG1iyiKavCqFLCDyej',
    consumer_secret='PdXWP1txJQ3Oh3wdBIFp6nu8KCljA47p6sKqAhXqYXORIkBjXg',
    access_token_key='1152431010807631872-waR3H3hwytSSiUb2ykZOCrLUSyTy3L',
    access_token_secret='jDZFEUhMQbvx64SxjwiEK9NGltXpphxL0NnCo3PiBWZ9s'
    )

results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=5")
print(results)
print('\n###########################\n')
print(results[0].AsDict()['id'])
