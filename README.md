# MemeImageEditor

## Description

**MemeImageEditor** is a simple GUI application for Windows that allows you to upload an image, add custom text with selectable position, font, color, and size, and save the edited image. It also features automatic meme generation with random images and captions based on emotions.

---

## Features

- Upload and display images (JPG, PNG, JPEG)
- Add user-defined text to any position with custom font, color, and size
- Save the edited image in PNG or JPEG format
- Automatically generate meme images with random emotion-based captions and styles
- Intuitive Tkinter-based graphical interface

---

## Requirements

- Python 3.8+
- `opencv-python`
- `Pillow` (PIL)
- `tkinter` (usually included with Python)

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mistlp74/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies:**
    ```bash
    pip install opencv-python pillow
    ```

---

## Usage

1. Make sure there are font files in the `fonts` folder and emotion images in the `DataBase` subfolders (`smile`, `angry`, `surprise`).
2. Run the application:
    ```bash
    python main.py
    ```
3. Use the buttons in the interface to:
    - Upload an image
    - Add custom text
    - Save the result
    - Auto-generate a meme

---

## Project Structure

- `main.py` — main GUI application
- `AutoGenerator.py` — automatic meme generation logic
- `fonts/` — folder for TTF font files (e.g., `comic.ttf`)
- `DataBase/` — contains subfolders with emotion images:
    - `smile/`
    - `angry/`
    - `surprise/`

---

## Troubleshooting

- **No fonts available:** Add TTF font files (e.g., `comic.ttf`) to the `fonts` directory.
- **No images for meme generation:** Ensure each emotion folder in `DataBase` contains images.
- **Image not displayed:** Check that dependencies are installed and image formats are supported.

---

## Author

Developed by [mistlp74](https://github.com/MilisCarter74)
