import tkinter as tk
import gameManager as model
import scraper
from tkinter import ttk

manager = model.GameMananger()

def onGuess():
    if (manager.gameOver):
        return
    year = years_clicked.get()
    if not manager.checkDateGuess(int(year)):
        manager.addHeadline()
    updateTable()
    updateGuessCount()

def updateGuessCount():
    if (manager.gameOver):
        gameOverLabel.config(text = "Game over. Guesses: " + str(manager.guesses))
    else:
        gameOverLabel.config(text = "Guesses: " + str(manager.guesses))

def updateTable():
    children = table.get_children()
    for child in children:
        table.delete(child)

    for headline in list(manager.headlineWData.keys()):
        if(manager.gameOver):
            table.insert("","end",value=(headline,manager.headlineWData[headline][0],manager.headlineWData[headline][1]))
        else:
            table.insert("","end",value=(headline,"?","?"))




root = tk.Tk()
#root.geometry("400x400")
root.title("RetroGuessr")

label = tk.Label(root, text = "Guess The Year", font = ("Arial",30)).grid(row = 0, columnspan = 2)

#create Treeview/table
cols = ("Headline","Date","Article URL")
table = ttk.Treeview(root, columns = cols, show="headings")
#set the column headings
for col in cols:
    table.heading(col, text = col)

updateTable()

table.grid(row = 1, column = 0, columnspan=2)



years = list(range(scraper.Scraper().firstYear, scraper.Scraper().lastYear+1))
years_clicked = tk.StringVar()
years_clicked.set(str(1970))
year_drop = tk.OptionMenu(root, years_clicked, *years)
year_drop.grid(row = 4, column = 0)

guessButton = tk.Button(root, text="Guess!", command = onGuess)
guessButton.grid(row = 4, column = 1)


gameOverLabel = tk.Label(root, text="Guesses: " + str(manager.guesses))
gameOverLabel.grid(row = 5, column = 0, columnspan=2)

root.mainloop()

