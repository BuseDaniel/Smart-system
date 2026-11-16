from tkinter import *
import json
from pathlib import Path

weather_path = Path(__file__).with_name("weather.json")

with weather_path.open(encoding="utf-8") as file:
    weather_data = json.load(file)

first_temperature = weather_data["hourly"]["temperature_2m"][0]

root = Tk()

root.title("EcoSmartHome")
root.geometry("400x300")

label = Label(
    master=root,
    text="Smart Home Dashboard",
    font=("Arial", 18, "bold")
)
label.pack(pady=20)

temperatuur = Label(
    master=root,
    text=f"Buitentemperatuur: {first_temperature} °C" ,
    font=("Arial", 14)
)
temperatuur.pack(pady=10)

def toon_dagoverzicht():
    temperaturen = weather_data["hourly"]["temperature_2m"]
    laagste = min(temperaturen)
    hoogste = max(temperaturen)
    overzicht.config(text=f"Laagste: {laagste} °C | Hoogste: {hoogste} °C")


overzicht_knop = Button(root, text="Toon dagoverzicht", command=toon_dagoverzicht)
overzicht_knop.pack(pady=10)

overzicht = Label(root, text="")
overzicht.pack()

def toon_temperatuurgrafiek():
    temperaturen = weather_data["hourly"]["temperature_2m"]
    tijden = weather_data["hourly"]["time"]

    laagste = min(temperaturen)
    hoogste = max(temperaturen)

    venster = Toplevel(root)
    venster.title("Buitentemperatuur per uur")

    grafiek = Canvas(venster, width=460, height=260, bg="white")
    grafiek.pack()

    links = 65
    onder = 210
    breedte = 360
    hoogte = 180

    grafiek.create_line(links, onder, links + breedte, onder)
    grafiek.create_line(links, onder, links, onder - hoogte)
    grafiek.create_text(links, onder + 20, text=tijden[0][-5:])
    grafiek.create_text(links + breedte, onder + 20, text=tijden[-1][-5:])

    afstand_per_uur = breedte / max(len(temperaturen) - 1, 1)
    temperatuurverschil = max(hoogste - laagste, 1)
    pixels_per_graad = hoogte / temperatuurverschil

    punten = []
    for uur, temperatuur in enumerate(temperaturen):
        x = links + uur * afstand_per_uur
        y = onder - (temperatuur - laagste) * pixels_per_graad
        punten.extend([x, y])

    if len(punten) >= 4:
        grafiek.create_line(*punten, fill="royalblue", width=2)
    else:
        x, y = punten
        grafiek.create_oval(x - 3, y - 3, x + 3, y + 3, fill="royalblue")

    grafiek.create_text(links - 10, onder, text=f"{laagste} °C", anchor="e")
    if hoogste != laagste:
        y_hoogste = onder - (hoogste - laagste) * pixels_per_graad
        grafiek.create_text(
            links - 10, y_hoogste, text=f"{hoogste} °C", anchor="e"
        )
grafiek_knop = Button(
    master=root,
    text="Toon temperatuurgrafiek",
    command=toon_temperatuurgrafiek,
)
grafiek_knop.pack(pady=10)

root.mainloop()

