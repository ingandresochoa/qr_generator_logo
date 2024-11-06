import qrcode
import base64
import os
from PIL import Image
from flask import Flask, request, jsonify, render_template
from io import BytesIO

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def generate_qr_with_logo(data, logo_path, logo_size_ratio=0.25):
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
    img_buffer = BytesIO()
    qr_image.save(img_buffer, format="PNG")
    img_str = base64.b64encode(img_buffer.getvalue()).decode()

    return img_str

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.form.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        if 'logo' not in request.files:
            return jsonify({'error': 'No logo provided'}), 400
        
        logo_file = request.files['logo']
        if logo_file.filename == '':
            return jsonify({'error': 'No logo selected'}), 400
        
        img_str = generate_qr_with_logo(data, logo_file)

        return jsonify({'success': True, 'image': img_str})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Usage 
if __name__ == '__main__':
    app.run(debug=True)