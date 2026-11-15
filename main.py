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

root.mainloop()
