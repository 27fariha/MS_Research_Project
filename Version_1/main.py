from google_play_scraper import app
from app_pakage_scrapper import AppScrapper
import csv, os
from dotenv import load_dotenv

try:
    load_dotenv()

    obj = AppScrapper()

    count = 0
    for info in obj.GetAppNames():
        result = app(
            '' + info,
            lang='en',  # defaults to 'en'
            country='pk'  # defaults to 'us'
        )
        # for info in result:
        count += 1
        DataMap = {'App_Id': result["appId"],
                   'App_Name': result["title"],
                   'App_Genre_Id': result["genreId"],
                   'App_Genre': result["genre"],
                   'Number_of_Reviews': result["reviews"],
                   'Number_Downloads': result["installs"],
                   }
        with open(os.getenv("CSV_PATH"), mode='a') as csv_file:
            fieldnames = ['App_Id', 'App_Name', 'App_Genre_Id', 'App_Genre', 'Number_of_Reviews', 'Number_Downloads']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(DataMap)

        print(f'{count} : {DataMap}')

        if count == 15:
            break

except:
    print("Error")
