from operator import truediv
from leaderBoardIO import LeaderBoardIO
import scraper
import random
from datetime import date

class GameMananger:

    #categoriesList = ["world", "sports", "us", "arts", "books", "movies"]
    #Stores the months
    months = [
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June", 
        "July", 
        "August", 
        "September", 
        "October",
        "November", 
        "Decemeber"
    ]
    #Stores how many days are in a month
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
    #stores the categories
    categories = {
        "world" : True,
        "sports" : True,
        "us" : True,
        "arts" : True,
        "books" : True,
        "movies" : True
    }
    #The year to guess
    year = 1970
    #A dictionary in format headline:[date,url]. Used to reveal extra information after game has been won.
    headlineWData = {}
    #Instance of scraper
    scraper = scraper.Scraper()
    #Number of guesses by the user
    guesses = 0
    #status of the current game
    gameOver = False
    #status of if hints were used
    hintsOn = False
    #the leaderboad manager
    leaderBoard = LeaderBoardIO()

    def __init__(self):
        self.newGame()

    def newGame(self):
        self.gameOver = False
        self.hintsOn = False
        self.guesses = 0
        self.year = random.choice(range(self.scraper.firstYear,self.scraper.lastYear+1))
        #print(self.year)
        self.headlineWData = {}
        self.addHeadline()
        

    def addHeadline(self):
        #Pick category
        choices = []

        for category in self.categories.keys():
            if self.categories[category]:
               choices.append(category)
        
        while True:
            try:
                line = self.scraper.getHeadlineByYear(self.year, random.choice(choices))
                break
            except SyntaxError:
                pass

        #update data
        print(line[2])
        self.headlineWData[line[0]] = [line[1],line[2]]
        #return the new list of headlines
        return list(self.headlineWData.keys())

        """
        self.headline = line[0]
        self.date = line[1]
        self.url = line[2]
        """


    #Make sure the date is in MM/DD/YYYY
    def validateDate(self, date):
        try:
            comps = date.strip().split("/")
            month = int(comps[0])
            day = int(comps[1])
            year = int(comps[2])

            if month < 0 or month > 12:
                return False
            
            if day < 0 or day > self.monthToDays(month):
                return False

            if year < 1970 or year > 2011:
                return False

            return True

        except:
            return False

    #
    def checkDateGuess(self, year):
        if(self.gameOver):
            return

        self.guesses += 1

        self.gameOver = self.year == year

        if(self.gameOver):
            self.leaderBoard.addToLeaderBoard([self.guesses,self.year,date.today().strftime("%b-%d-%Y"),self.hintsOn])

        return self.gameOver

        