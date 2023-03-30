import os
import sys
import emoji
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import zipfile
import shutil


def get_emoji_hex(emoji_char):
    return '-'.join([f"{ord(c):X}" for c in emoji_char])

def download_png(emoji_char, resolution):
    emoji_code = get_emoji_hex(emoji_char)
    url = f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/{resolution}/emoji_u{emoji_code.lower()}.png"
    response = requests.get(url)

    if response.status_code == 200:
        return response.content
    else:
        return None

def create_gradient_background(width, height, start_color, end_color):
    start_color = Image.new("RGBA", (width, height), start_color)
    end_color = Image.new("RGBA", (width, height), end_color)
    
    gradient = Image.new("RGBA", (width, height))
    
    for y in range(height):
        alpha = y / (height - 1)
        row = Image.blend(start_color, end_color, alpha)
        gradient.paste(row, (0, y))
    
    gradient = gradient.resize((width, height), Image.LANCZOS)
    return gradient



def resize_image(image_data, size):
    img = Image.open(BytesIO(image_data))
    img = img.resize((size, size), Image.LANCZOS)
    img = img.convert("RGBA")

    output = BytesIO()
    img.save(output, format="PNG")
    return output.getvalue()


def convert_emoji_to_iconset(emoji_char, output_folder):
    resolutions = [1024, 512, 256, 128, 64, 32]
    original_png_data = download_png(emoji_char, 512)

    if not original_png_data:
        print(f"Error: Unable to fetch PNG for emoji: {emoji_char}")
        sys.exit(1)

    for size in resolutions:
        resized_png_data = resize_image(original_png_data, size)
        output_path = os.path.join(output_folder, f"icon_{size}x{size}.png")

        try:
            with open(output_path, "wb") as png_file:
                png_file.write(resized_png_data)
        except Exception as e:
            print(f"Error: Unable to save PNG: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python emoji_to_icon.py [emoji]")
        sys.exit(1)

    emoji_char = sys.argv[1]
    output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "iconset")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    convert_emoji_to_iconset(emoji_char, output_folder)
    print(f"Successfully saved emoji as icon set at {output_folder}")

if __name__ == "__main__":
    main()
