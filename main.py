import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import AutoGenerator as ag

photo = None
file_path = None
Edited_image = None
image_meme = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, "fonts")

def F1():
    global photo
    global file_path

    file_path = filedialog.askopenfilename(title="Select a File",
                                           filetypes=(("Image files", "*.jpg;*.png;*.jpeg"), ("All files", "*.*")))
    if file_path:
        image_cv2 = cv2.imread(file_path)
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        photo = ImageTk.PhotoImage(image_pil)
        Label1.config(image=photo)
        Label1.image = photo
        print("Done")

def F2():
    global file_path
    global Edited_image

    frame4 = tk.Frame(Wmain, bg="#4A4A4A", width=260, height=300)
    frame4.place(x=100, y=150)

    entry1 = tk.Entry(frame4)
    entry1.place(x=110, y=20)
    entry2 = tk.Entry(frame4)
    entry2.place(x=110, y=70)
    entry3 = tk.Entry(frame4)
    entry3.place(x=110, y=120)
    entry4 = tk.Entry(frame4)
    entry4.place(x=110, y=170)
    entry5 = tk.Entry(frame4)
    entry5.place(x=110, y=220)

    Label11 = tk.Label(frame4,text="Position (x, y)", bg="#2B2B2B", fg="white")
    Label11.place(x=20, y=20, width=80, height=20)
    Label22 = tk.Label(frame4, text="Text", bg="#2B2B2B", fg="white")
    Label22.place(x=20, y=70, width=80, height=20)
    Label33 = tk.Label(frame4, text="Font file", bg="#2B2B2B", fg="white")
    Label33.place(x=20, y=120, width=80, height=20)
    Label44 = tk.Label(frame4, text="Color", bg="#2B2B2B", fg="white")
    Label44.place(x=20, y=170, width=80, height=20)
    Label55 = tk.Label(frame4, text="Size", bg="#2B2B2B", fg="white")
    Label55.place(x=20, y=220, width=80, height=20)

    def des():
        frame4.destroy()

    def F21():
        global Edited_image

        position = entry1.get()
        text = entry2.get()
        Efont = entry3.get()  # Тепер очікується filename типу Arial.ttf
        color = entry4.get()
        size = int(entry5.get())

        font_path = os.path.join(FONTS_DIR, Efont)

        try:
            font = ImageFont.truetype(font_path, size=size)
        except IOError:
            font = ImageFont.load_default()

        try:
            color = tuple(map(int, color.split(',')))
        except ValueError:
            color = (0, 0, 0)

        Edited_image = Image.open(file_path).convert("RGBA")
        draw = ImageDraw.Draw(Edited_image)
        draw.text(tuple(map(int, position.split(','))), text, font=font, fill=color)

        image_tk = ImageTk.PhotoImage(Edited_image)
        Label1.config(image=image_tk)
        Label1.image = image_tk

    buttonDes = tk.Button(frame4, text="Cancel", bg="black", fg="white", command=des)
    buttonDes.place(x=130, y=260, width=80, height=27)

    submit_button = tk.Button(frame4, text="Apply", bg="black", fg="white", command=F21)
    submit_button.place(x=40, y=260, width=80, height=27)

def F3():
    global Edited_image
    global image_meme

    file_path_save = filedialog.asksaveasfilename(
        title="Save the file",
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
    )

    if Edited_image:
        if file_path_save:
            Edited_image.save(file_path_save)
    elif image_meme:
        if file_path_save:
            image_meme.save(file_path_save)

def F4():
    global image_meme

    image_meme = ag.generate_meme(photo)
    meme_tk = ImageTk.PhotoImage(image_meme)
    Label1.config(image=meme_tk)
    Label1.image = meme_tk
    return meme_tk

Wmain = tk.Tk()
Wmain.geometry('1080x540')
Wmain.configure(bg='#1F1F1F')

frame1 = tk.Frame(Wmain, bg="#2B2B2B", width=720, height=480)
frame1.pack()
frame1.place(x=310, y=30)

Label1 = tk.Label(Wmain, bg="#3D3D3D")
Label1.pack()
Label1.place(x=320, y=40, width=700, height=460)

frame2 = tk.Frame(Wmain, bg="#2B2B2B", width=240, height=230)
frame2.pack()
frame2.place(x=40, y=80)

button1 = tk.Button(Wmain, text="Upload image", bg="black", fg="white", bd=5, command=F1)
button1.pack()
button1.place(x=60, y=100, width=200, height=40)

button2 = tk.Button(Wmain, text="Add text", bg="black", fg="white", bd=5, command=F2)
button2.pack()
button2.place(x=60, y=150, width=200, height=40)

button3 = tk.Button(Wmain, text="Save image", bg="black", fg="white", bd=5, command=F3)
button3.pack()
button3.place(x=60, y=200, width=200, height=40)

button4 = tk.Button(Wmain, text="Auto Generation", bg="black", fg="white", bd=5, command=F4)
button4.pack()
button4.place(x=60, y=250, width=200, height=40)

Wmain.mainloop()