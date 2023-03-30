# Emoji to Icon Converter

The Emoji to Icon Converter is a Python script that allows you to convert any emoji into an icon set. The script fetches the PNG image for the given emoji from Google's Noto Emoji repository, resizes it to different resolutions, and saves the resized PNGs as an icon set on your desktop.

## Prerequisites

Before running the script, make sure you have the following installed on your computer:

- Python 3.6 or higher
- The '**requests**', '**Pillow**', and '**shutil**' Python modules


You can install the Python modules using pip, like so:


`pip install requests Pillow shutil`


## Usage

To use the Emoji to Icon Converter, follow these steps:

1. Clone or download the repository to your computer.
1. Open your terminal and navigate to the repository folder.
1. Run the **'emoji_to_icon.py'** script with the desired emoji as an argument. 
For example:

`python emoji_to_icon.py 😄`

The resulting icon set will be saved in a folder named iconset on your desktop.

## How It Works

The script uses the **'requests'** module to fetch the PNG image for the given emoji from Google's Noto Emoji repository. It then uses the **'Pillow'** module to resize the image to different resolutions and convert it to the RGBA format. Finally, it uses the **'shutil'** module to save the resized images as an icon set on your desktop.

## License

The Emoji to Icon Converter is released under the MIT License.
