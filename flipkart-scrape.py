import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk

# URL taken
url = "https://www.flipkart.com/search?q=monitor&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

master = Tk()
master.title("Scrape Data")
master.config(bg="black")
master.geometry("500x400")

# Function What we Require
def getMonitor():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    monitor = soup.find('div', class_="col col-7-12").text   # getting info in TEXT format
    ratings = soup.find('div', class_="hGSR34").text

    monitorLabel.config(text=monitor)  # Configuration on UI
    ratingsLabel.config(text=ratings)
    print(monitor,ratings)




monitorLabel = Label(master, text="Description: ",fg="Green", bg="Black")
monitorLabel.place(x=15, y=100)

ratingsLabel = Label(master, text="Ratings: ",fg="Green", bg="Black")
ratingsLabel.place(x=17, y=150)

note1 = Label(master, text="Description *", fg="Green", bg="black") # Description Notes
note1.place(x=13, y=80)

note2 = Label(master, text="Ratings *", fg="Green", bg="black")
note2.place(x=16, y=130)

getMonitor() # in Loop
master.mainloop()
