from operator import truediv
import scraper
import random

class GameMananger:

    #categoriesList = ["world", "sports", "us", "arts", "books", "movies"]

    categories = {
        "world" : True,
        "sports" : True,
        "us" : True,
        "arts" : True,
        "books" : True,
        "movies" : True
    }

    headline = ""
    date = ""
    url = "" 

    def __init__(self):
        self.newGame()

    def newGame(self):
        self.guessesRemaining = 3
        self.selectHeadline()

    def selectHeadline(self):
        #Pick category
        choices = []

        for category in self.categories.keys:
            if self.categories(category):
               choices.append(category)
        
        line = scraper.getHeadline(random.choice(choices))

        self.headline = line[0]
        self.date = line[1]
        self.url = line[2]

    #Make sure the date is in MM/DD/YYYY
    def validateDate(self, date):
        try:
            monthToDays = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
            }

            comps = date.strip().split("/")
            month = int(comps[0])
            day = int(comps[1])
            year = int(comps[2])

            if month < 0 or month > 12:
                return False
            
            if day < 0 or day > monthToDays(month):
                return False

            if year < 1970 or year > 2011:
                return False

            return True

        except:
            return False

    def checkDateGuess(self, date):
        if (self.guessesRemaining > 0 and self.validateDate(date)):
            return date == self.date