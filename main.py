from tkinter import *

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
    text="Temperatuur: 22 °C",
    font=("Arial", 14)
)
temperatuur.pack(pady=10)

root.mainloop()
