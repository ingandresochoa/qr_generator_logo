import qrcode
import base64
import os
from PIL import Image
from flask import Flask, request, jsonify, render_template
from io import BytesIO

def generate_qr_with_logo(data, logo_path, output_path, logo_size_ratio=0.25):
    # Create a qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Open the logo image and resize it proportionally
    logo = Image.open(logo_path)
    logo_size = int(qr_image.size[0] * logo_size_ratio)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to center the logo on the qr code
    pos = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)

    # Paste the logo onto the qr code
    qr_image.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)

    # Save the qr code with logo
    qr_image.save(output_path)
    print(f"QR code and logo generated successfully! - {output_path}")

# Usage 
data = "https://www.tiktok.com/@ingandresochoa" # Replace with your data to be encoded
logo_path = "ouroboro.jpg" # Replace with the path to your logo
output_path = "" # Replace with the desired output path
generate_qr_with_logo(data, logo_path, output_path)