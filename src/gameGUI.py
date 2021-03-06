import tkinter as tk
from turtle import color, width
import gameManager as model
import scraper
from tkinter import PhotoImage, Toplevel, ttk
import webbrowser

manager = model.GameMananger()

def onGuess():
    if (manager.gameOver):
        return
    year = int(years_clicked.get())

    if not manager.checkDateGuess(int(year)):
        if hintsOn.get():
            hint.grid()
            manager.hintsOn = True
        else:
            hint.grid_remove()

        if year < manager.year:
            hint.config(text = "Your Guess Was Too Early")
        elif year > manager.year:
            hint.config(text = "Your Guess Was Too Late")
        manager.addHeadline()
    else:
        hint.grid_remove()
    
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

def table_click_handler(event):
    selected = table.item(table.focus())
    row = table.identify_row(event.y)
    col = table.identify_column(event.x)
    if row == "#1":
        return
    if(manager.gameOver and col == "#3"):
        url = list(selected.values())[2][2]
        webbrowser.open(url)

def openLeaderBoard():
    top = Toplevel(root)
    top.title("Leaderboard")
    cols = ("Guesses","Year","Date Achieve","Hints On")
    leaderBoardTable = ttk.Treeview(top, columns = cols, show="headings")
    #set the column headings
    for col in cols:
        leaderBoardTable.heading(col, text = col)
    for rowData in manager.leaderBoard.leaderBoard:
        leaderBoardTable.insert("","end",value = rowData)

    leaderBoardTable.pack()


def openHelpMenu():
    top = Toplevel(root)
    top.title("How To Play")
    tk.Label(top, text = """Welcome to RetroGuessr! The rules are simple: select a year with the 
    drop down menu in the bottom left and confirm it by pressing 'Guess!' Try to guess the year from
    news headlines provided in as few guesses as possible. Each wrong guess reveals another headline 
    from the same year. The headlines are taken from archived New York Times articles. After the game
    is over, click on the url next to a headline to open the article in your browser (a NYT subscription may
    be necessary).""").pack()

def reset():
    manager.newGame()
    updateTable()
    updateGuessCount()


#The root window
root = tk.Tk()
root.geometry("1060x400")
root.resizable(False,False)
root.title("RetroGuessr")
root.iconphoto(True, PhotoImage(file = "rg_icon.png"))

#The Menu Bar
menuBar = tk.Menu(root)


bg = tk.PhotoImage(file="src/newspapers2.gif")
bgLabel = tk.Label(root, image = bg)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

#Options Menu Bar
hintsOn = tk.BooleanVar()
hintsOn.set(False)
optionsMenu = tk.Menu(menuBar, tearoff = 0)
optionsMenu.add_checkbutton(label = "Show Hints", onvalue = True, offvalue = False, variable = hintsOn)
menuBar.add_cascade(label = "Options", menu = optionsMenu)
#Leaderboard Button
menuBar.add_command(label = "Leaderboard", command = openLeaderBoard)
#Help Button
menuBar.add_command(label="Help", command = openHelpMenu)

#The Theme
s = ttk.Style()
s.theme_use("classic")
label = tk.Label(root, text = "RetroGuessr", font = ("Bernard MT Condensed",45)).grid(row = 0, columnspan = 2)

#create Treeview/table
cols = ("Headline","Date","Article URL")
table = ttk.Treeview(root, columns = cols, show="headings")
#set the column headings
for col in cols:
    table.heading(col, text = col)

table.column("#1", width=350)
table.column("#2", width=350)
table.column("#3", width=350)
updateTable()

table.bind('<ButtonRelease-1>', table_click_handler)

table.grid(row = 1, column = 0, columnspan=2)



years = list(range(scraper.Scraper().firstYear, scraper.Scraper().lastYear+1))
years_clicked = tk.StringVar()
years_clicked.set(str(1970))
year_drop = tk.OptionMenu(root, years_clicked, *years)
year_drop.grid(row = 4, column = 0)

hint = tk.Label(root, text = "")
#preps the label, but removes it. A Simple hint.grid() will bring it back with proper positioning
hint.grid(row = 7, column = 0, columnspan=2)
hint.grid_remove()

guessButton = tk.Button(root, text="Guess!", command = onGuess)
guessButton.grid(row = 4, column = 1)


gameOverLabel = tk.Label(root, text="Guesses: " + str(manager.guesses))
gameOverLabel.grid(row = 5, column = 0, columnspan=2)

playAgainButton = tk.Button(root, text = "New Articles", command = reset)
playAgainButton.grid(row = 6, column = 0, columnspan = 2) 

root.config(menu=menuBar)
root.mainloop()

