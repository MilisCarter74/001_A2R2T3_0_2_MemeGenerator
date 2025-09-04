import random
import os
from PIL import Image, ImageDraw, ImageFont

# Шляхи до папок з емоціями відносно розташування цього файлу
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "DataBase")
FONTS_DIR = os.path.join(BASE_DIR, "fonts")

emotions_folders = {
    "smile": os.path.join(DB_DIR, "smile"),
    "angry": os.path.join(DB_DIR, "angry"),
    "surprised": os.path.join(DB_DIR, "surprise"),
}

texts = {
    "smile": [
        "When you woke up and still hadn't started the day",
        "When you always have a reason to laugh"
    ],
    "angry": [
        "When you are not heared",
        "When you are wainting for results",
        "When you wake up abruptly, you have to go to some school"
    ],
    "surprised": [
        "When you found out you were having a day off",
        "When your code works",
        "When you decided to explore the new library completely",
        "When your code doesnt work"
    ]
}

def generate_meme(photo):
    emotion = random.choice(list(emotions_folders.keys()))

    folder = emotions_folders[emotion]
    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_file = random.choice(image_files)
    image_path = os.path.join(folder, image_file)

    text = random.choice(texts[emotion])

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font_path = os.path.join(FONTS_DIR, "comic.ttf")
    try:
        font = ImageFont.truetype(font_path, size=28)
    except IOError:
        font = ImageFont.load_default()

    color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])

    image_width, image_height = image.size

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    position = ((image_width - text_width) / 2, image_height - text_height - 10)

    draw.text(position, text, font=font, fill=color)

    return image