from bs4 import BeautifulSoup
import requests, os
from dotenv import load_dotenv

load_dotenv()


class AppScrapper:
    path = os.getenv("COMMUNICATION")
    path2 = os.getenv("EDUCATION")
    path3 = os.getenv("FINANCE")

    # will return a list of apps names
    def GetAppNames(self):
        result = requests.get(self.path3)
        doc = BeautifulSoup(result.text, "html.parser")
        divs = doc.findAll(class_="JC71ub", href=True)
        return [i['href'].split("id=", 1)[1] for i in divs]


# count = 0
# obj = AppScrapper()
#
# # print(obj.GetAppNames())
# for i in obj.GetAppNames():
#     count += 1
#     print(f'{count}',i)
#
# print(count)
