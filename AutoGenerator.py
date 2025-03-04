import tkinter as tk
import random
import os
from PIL import Image, ImageDraw, ImageFont, ImageTk

emotions_folders = {
    "smile": r"C:\\Users\\dmytr\\PycharmProjects\\pythonProject\\Lessons\\MemeGenerator\\DataBase\\smile",
    "angry": r"C:\\Users\\dmytr\\PycharmProjects\\pythonProject\\Lessons\\MemeGenerator\\DataBase\\angry",
    "surprised": r"C:\\Users\\dmytr\\PycharmProjects\\pythonProject\\Lessons\\MemeGenerator\\DataBase\\surprise"
}

texts = {
    "smile": [
        "Коли ти прокинувся і все ще не почав день",
        "Коли в тебе завжди є привід посміятись"
    ],
    "angry": [
        "Коли тебе не чують",
        "Коли ти чекаєш результатів",
        "Коли різко розбудили і треба йти в якусь школу"
    ],
    "surprised": [
        "Коли дізнався, що у тебе буде день відпочинку",
        "Коли твій код працює з першого разу",
        "Коли вирішив вивчити нову бібліотеку повністю",
        "Коли до дедлайну 1 день а ти нічого не робив"
    ]
}


def generate_meme(photo):
    emotion = random.choice(list(emotions_folders.keys()))

    folder = emotions_folders[emotion]
    image_files = os.listdir(folder)
    image_file = random.choice(image_files)
    image_path = os.path.join(folder, image_file)

    text = random.choice(texts[emotion])

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\comic.ttf", size=15)
    except IOError:
        font = ImageFont.load_default()

    color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

    image_width, image_height = image.size

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    position = ((image_width - text_width) / 2, image_height - text_height - 10)

    draw.text(position, text, font=font, fill=color)

    return image