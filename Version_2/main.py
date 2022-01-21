from _ast import mod

from google_play_scraper import Sort, reviews_all
from app_pakage_scrapper import AppScrapper
from datetime import datetime

obj = AppScrapper()
file = open('data.txt', 'w')

# for app in obj.GetAppNames():
# print(str({'userName': info['userName'], 'content': info['content'], 'score': info['score']}) + '\n' +count)
# file.close()

count = 0

for i in reviews_all(
    'com.zong.customercare',
    sleep_milliseconds = 0,  # defaults to 0
    lang = 'en',  # defaults to 'en'
    country = 'pk',  # defaults to 'us'
    sort = Sort.RATING,  # defaults to Sort.MOST_RELEVANT
    filter_score_with = 1,  # defaults to None(means all score)
):
    CurrentMonth=int(datetime.now().month)
    CurrentYear=int(datetime.now().year)
    LastThirdMonth=int(CurrentMonth-3)
    ScrapperMonth=int(str(str(i["at"]).rsplit(' ')[0]).rsplit('-')[1])
    ScrapperYear=int(str(i["at"]).rsplit(' ')[0].rsplit('-')[0])

    if ((ScrapperMonth <= CurrentMonth) and (ScrapperMonth >= LastThirdMonth)) and ScrapperYear == CurrentYear:
        print({'userName': i['userName'], 'content': i['content'], 'score': i['score'],'date':i['at']})
        count+=1

print(count)