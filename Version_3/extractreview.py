
from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.hb.dialer.free',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.RATING, # defaults to Sort.MOST_RELEVANT
    filter_score_with=1 # defaults to None(means all score)
)
for ite in result:
  print(ite["content"])