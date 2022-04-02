import tkinter as tk
import gameManager as model
import scraper

manager = model.GameMananger()

def onGuess():
    guess = months_clicked.get() + "/" + days_clicked.get() + "/" + years_clicked.get()
    print(guess)
    if guess == "January/1/1970": #manager.checkDate(guess):
        urlLabel.config(text = manager.url)


root = tk.Tk()
root.geometry("200x200")
root.title("RetroGuessr")


headlineString = manager.headline
headlineLabel = tk.Label(root, text=headlineString)
headlineLabel.pack()


years = list(range(scraper.Scraper().firstYear, scraper.Scraper().lastYear+1))
years_clicked = tk.StringVar()
years_clicked.set(str(1970))
year_drop = tk.OptionMenu(root, years_clicked, *years)
year_drop.pack()
months = manager.months
months_clicked = tk.StringVar()
months_clicked.set("January")
months_drop = tk.OptionMenu(root, months_clicked, *months)
months_drop.pack()
days = range(1,31)
days_clicked = tk.StringVar()
days_clicked.set("1")
days_drop = tk.OptionMenu(root,days_clicked,*days)
days_drop.pack()

guessButton = tk.Button(root, text="Guess!", command = onGuess)
guessButton.pack()

urlLabel = tk.Label(root)
urlLabel.pack()



root.mainloop()

