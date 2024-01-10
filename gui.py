from os import path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.messagebox import showerror
from pathlib import Path
import requests


api_key = "7e26fee9663087f9c0a3e904ff0f5764"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def change_button_image(file):
    try:
        image = PhotoImage(file=relative_to_assets(file))
        button_1.config(image=image)
        button_1.image = image  # نگهداری از مرجع به تصویر تا از مشکل garbage collection جلوگیری شود
    except tk.TclError as e:
        print(f"Error loading image: {e}")


def change_canvas_color(color):
    canvas.itemconfig(canvas_rect, fill=color)


def send():
    cityname = entry_1.get()
    url = base_url + cityname + "&appid=" + api_key

    result = requests.get(url)
    data = result.json()

    if data["cod"] == "404":
        entry_2.delete("1.0", tk.END)  
        entry_2.insert(tk.END, "ERROR!") 
        showerror(title="Error",message="City not found!")
    else:
        a = data["main"]

        t = a["temp"]
        tc = t - 273.15
        p = a["pressure"]
        h = a["humidity"]
        b = data["wind"]
        s = b["speed"]
        w = data["weather"]
        d = w[0]["description"]



        
        entry_2.delete("1.0", tk.END)  
        entry_2.insert(tk.END, f"Temp: {round(tc, 2)} C\n")
        entry_2.insert(tk.END, f"Pressure: {p} HPA\n")
        entry_2.insert(tk.END, f"Humidity: {h} %\n")
        entry_2.insert(tk.END, f"Speed: {s} M/S\n")
        entry_2.insert(tk.END, f"Description: {d}")


window = tk.Tk()

window.geometry("600x400")
window.configure(bg = "#FFFFFF")
window.title("LABZ weather")
window.iconbitmap(relative_to_assets("if-weather-2-2682849_90781.ico"))


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas_rect = canvas.create_rectangle(
    0.0,
    0.0,
    200.0,
    400.0,
    fill="#0038FF",
    outline="")



image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    90.0,
    image=image_image_1
)

canvas.create_text(
    50.0,
    191.0,
    anchor="nw",
    text="LABZ weather",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    29.0,
    233.0,
    anchor="nw",
    text="       Developer By\nAli Karimi Moghadam",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    330.0,
    34.0,
    anchor="nw",
    text="Enter your own City: ",
    fill="#000000",
    font=("Inter", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    402.0,
    80.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=259.5,
    y=63.0,
    width=285.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: send(),
    relief="flat"
)
button_1.place(
    x=352.0,
    y=110.0,
    width=100.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    402.0,
    242.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=257.0,
    y=167.0,
    width=290.0,
    height=148.0
)

canvas.create_text(
    12.0,
    374.0,
    anchor="nw",
    text="Ver 1.2",
    fill="#FFFFFF",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    221.0,
    336.0,
    anchor="nw",
    text="background color:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas_color("#0038FF") or change_button_image("button_1.png"),
    relief="flat"
)
button_2.place(
    x=235.0,
    y=366.0,
    width=15.0,
    height=15.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas_color("#00FFB2") or change_button_image("button_1_2.png"),
    relief="flat"
)
button_3.place(
    x=270.0,
    y=366.0,
    width=15.0,
    height=15.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas_color("#FF006B") or change_button_image("button_1_3.png"),
    relief="flat"
)
button_4.place(
    x=300.0,
    y=366.0,
    width=15.0,
    height=15.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas_color("#BD00FF") or change_button_image("button_1_4.png")
)
button_5.place(
    x=330.0,
    y=366.0,
    width=15.0,
    height=15.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_canvas_color("#FF8A00") or change_button_image("button_1_5.png"),
    relief="flat"
)
button_6.place(
    x=362.0,
    y=366.0,
    width=15.0,
    height=15.0
)


lblcitynotfound = tk.Label(master=window)
lblt = tk.Label(master=window)
lblp = tk.Label(window)
lblh = tk.Label(window)
lbls = tk.Label(window)
lbld = tk.Label(window)


window.resizable(False, False)
window.mainloop()
