import tkinter as tk
import gameManager as model
import scraper

manager = model.GameMananger()

root = tk.Tk()
root.geometry("200x200")
root.title("RetroGuessr")

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


root.mainloop()
