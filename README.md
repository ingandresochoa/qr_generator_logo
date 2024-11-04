# QR Code Generator with Logo in Python

This project is a simple tool in Python to generate QR codes that include a logo image at the center. The image is automatically resized to maintain the readability of the QR code. It's ideal for customizing QR codes for marketing, social media, and more.

## Features

- **QR Code Generation**: Generates a QR code from a link or any other data.
- **Logo in the Center**: Inserts an image in the center of the QR code.
- **Logo Size Adjustment**: Controls the size of the logo to ensure it doesn't affect the QR code's readability.
- **Error Correction**: Uses a high level of error correction to ensure the QR code works properly, even with the logo.

## Requirements

- Python 3.x
- Libraries: `qrcode` and `Pillow`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ingandresochoa/qr_generator_logo
   cd repository-name

2. Install the necessary libraries:
   ```bash
   pip install qrcode[pil]
   pip install pillow

## Usage:
- Place your logo image in the project folder. Ensure it's in .png format for better compatibility.
- In the main file (qr_with_logo.py), adjust the following variables according to your needs:
   data: The content of the QR code (e.g., a URL or text).
   logo_path: The path to your logo image (e.g., "logo.png").
   output_path: The path and filename where the generated QR code will be saved (e.g., "qr_with_logo.png").
   logo_size_ratio: The relative size of the logo compared to the QR code (e.g., 0.25 for the logo to occupy 25% of the QR code width).

## Run the script:
  ```bash
   python main.py

