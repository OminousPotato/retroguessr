import json
class LeaderBoardIO:
    def __init__(self) -> None:
        self.leaderBoard = self.loadLeaderBoard()
    def loadLeaderBoard(self):
        try:
            f = open("leaderboard.json")          
            jsonData = json.load(f)
            f.close()
            return list(jsonData)     
        except FileNotFoundError:
            g = open("leaderboard.json", "w")
            g.write("[]")
            g.close() 
            return self.loadLeaderBoard()
    #takes in a row in format [guesses, year, date achieved, "hintsOn"]
    def addToLeaderBoard(self, row):
        added = False
        for i in range(0,len(self.leaderBoard)):
            if (row[0] < self.leaderBoard[i][0]):
                self.leaderBoard.insert(i, row)
                added = True
                break

        if(not added):
            self.leaderBoard.append(row)

        while len(self.leaderBoard) > 10:
            self.leaderBoard.remove(self.leaderBoard[10])

        f = open("leaderboard.json", "w")
        json.dump(self.leaderBoard, f)
        f.close()

