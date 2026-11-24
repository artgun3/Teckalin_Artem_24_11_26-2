import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root = Tk()
root.title("Химия вокруг нас")
root.geometry("600x1080")
logo = PhotoImage(file="logo.png")
picture = Label(image=logo)
picture.pack()
logo = PhotoImage(file="logo.png")
picture = Label(image=logo)
picture.pack()

label_title = Label(text="Таблица Менделеева")
label_title.pack()

img = Image.open("Mendeleev.png")
img_resized = img.resize((500, 300), Image.Resampling.LANCZOS)
tk_img = ImageTk.PhotoImage(img_resized)
label = tk.Label(root, image=tk_img)
label.image = tk_img
label.pack()
Window = tk.Frame(root)
def go_to_page2():
    Window.pack(fill="both", expand=True)

btn = tk.Button(root, text="Открыть карточки элементов", command=go_to_page2)
btn.pack(pady=20)

elements = [
    [1, "H", "Водород", "Самый легкий газ без цвета и запаха.", "Ракетное топливо, химия."],
    [6, "C", "Углерод", "Неметалл (алмаз, графит).", "Металлургия, электроника."],
    [8, "O", "Кислород", "Газ, поддерживает горение.", "Медицина, сварка."],
    [13, "Al", "Алюминий", "Легкий металл, не ржавеет.", "Самолеты, фольга, посуда."],
    [26, "Fe", "Железо", "Прочный металл, притягивается магнитом.", "Сталь, чугун, машины."],
    [29, "Cu", "Медь", "Мягкий металл розового цвета.", "Провода, трубы."],
]
canvas = tk.Canvas(Window)
scrollbar = tk.Scrollbar(Window, orient="vertical", command=canvas.yview)
cards_frame = tk.Frame(canvas)

cards_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=cards_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

r = 0 
c = 0 

for el in elements:

    card = tk.Frame(cards_frame, bd=2, relief="groove", padx=10, pady=10, bg="white")
    card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")


    tk.Label(card, text=f"{el[1]} (№ {el[0]})", font=("Arial", 16, "bold"), bg="white", fg="blue").pack(anchor="w")
    tk.Label(card, text=el[2], font=("Arial", 13, "bold"), bg="white").pack(anchor="w")
    tk.Label(card, text="Свойства: " + el[3], font=("Arial", 10), bg="white", wraplength=250, justify="left").pack(anchor="w")
    tk.Label(card, text="Применение: " + el[4], font=("Arial", 10), bg="white", wraplength=250, justify="left").pack(anchor="w")

 
    c = c + 1
    if c == 2:
        c = 0
        r = r + 1
root.mainloop()