from tkinter import *
import json

weather_file = open("weather.json")
weather_data = json.load(weather_file)
weather_file.close()

temperaturen = weather_data["hourly"]["temperature_2m"]


def toon_dagoverzicht():
    laagste = min(temperaturen)
    hoogste = max(temperaturen)
    overzicht["text"] = f"Laagste: {laagste} °C | Hoogste: {hoogste} °C"


root = Tk()
root.title("EcoSmartHome")
root.geometry("400x300")

titel = Label(master=root, text="EcoSmartHome", font=("Arial", 18, "bold"))
titel.pack(pady=20)

temperatuur = Label(master=root, text=f"Buitentemperatuur: {temperaturen[0]} °C")
temperatuur.pack(pady=10)

knop = Button(master=root, text="Toon dagoverzicht", command=toon_dagoverzicht)
knop.pack(pady=10)

overzicht = Label(master=root, text="")
overzicht.pack()

root.mainloop()