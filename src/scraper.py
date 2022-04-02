from tkinter import EXCEPTION
import requests
import random
from bs4 import BeautifulSoup

class Scraper:
    monthToDays = {
    "01":31,
    "02":28,
    "03":31,
    "04":30,
    "05":31,
    "06":30,
    "07":31,
    "08":31,
    "09":30,
    "10":31,
    "11":30,
    "12":31
    }

    firstYear = 1970
    lastYear = 2009

    urlFormat = "https://www.nytimes.com/search?dropmab=true&endDate={date}&query=&sections={section}&sort=best&startDate={date}"

    categoryToUrlParameter = {
        "sports":"Sports%7Cnyt%3A%2F%2Fsection%2F4381411b-670f-5459-8277-b181485a19ec",
        "world":"World%7Cnyt%3A%2F%2Fsection%2F70e865b6-cc70-5181-84c9-8368b3a5c34b",
        "us":"U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c",
        "arts":"Arts%7Cnyt%3A%2F%2Fsection%2F6e6ee292-b4bd-5006-a619-9ceab03524f2",
        "books":"Books%7Cnyt%3A%2F%2Fsection%2F550f75e2-fc37-5d5c-9dd1-c665ac221b49",
        "movies":"Movies%7Cnyt%3A%2F%2Fsection%2F62b3d471-4ae5-5ac2-836f-cb7ad531c4cb"
    }

    def getHeadline(self, categoryName):
        try:
            year = random.choice(range(self.firstYear,self.lastYear+1))
            month = random.choice(list(self.monthToDays.keys()))
            day = str(random.choice(range(1,self.monthToDays[month]+1)))
            categoryUrlParameter = self.categoryToUrlParameter[categoryName]
            if len(day) < 2:
                day = "0" + day
            page = requests.get(self.urlFormat.format(date=str(year)+month+day, section = categoryUrlParameter))
            soup = BeautifulSoup(page.content, "html.parser")
            header = soup.find("h4")
            if (header.text == None or len(header.text) == 0):
                raise Exception
            header_url = header.find_parent("a").get("href")
            return [header.text, day+"/"+month+"/"+str(year), header_url]
        except:
            return self.getHeadline(categoryName)




