from flask import Flask, render_template, request, send_file, jsonify
import qrcode
import io
import base64
from PIL import Image, ImageColor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    print('Preview form data:', request.form)  # Debug log
    try:
        data = request.form['qr_data']
        dpi = int(request.form.get('dpi', 300))
        fg_color = request.form.get('fg_color', '#000000')
        bg_color = request.form.get('bg_color', '#FFFFFF')

        if not data:
            return jsonify({'error': 'Please enter text or a URL'}), 400

        # Convert hex to RGB
        fg_color_rgb = ImageColor.getrgb(fg_color)
        bg_color_rgb = ImageColor.getrgb(bg_color)

        base_box_size = 10
        scale = dpi / 300
        box_size = int(base_box_size * scale)

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=box_size, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fg_color_rgb, back_color=bg_color_rgb)

        img_io = io.BytesIO()
        img.save(img_io, 'PNG', optimize=True)
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'image': f'data:image/png;base64,{img_base64}'})
    except Exception as e:
        print('Preview error:', str(e))  # Debug log
        return jsonify({'error': f'Failed to generate QR code: {str(e)}'}), 500

@app.route('/download', methods=['POST'])
def download():
    print('Download form data:', request.form)  # Debug log
    try:
        data = request.form['qr_data']
        dpi = int(request.form.get('dpi', 300))
        fg_color = request.form.get('fg_color', '#000000')
        bg_color = request.form.get('bg_color', '#FFFFFF')

        if not data:
            return render_template('index.html', error="Please enter text or a URL")

        fg_color_rgb = ImageColor.getrgb(fg_color)
        bg_color_rgb = ImageColor.getrgb(bg_color)

        base_box_size = 10
        scale = dpi / 300
        box_size = int(base_box_size * scale)

        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=box_size, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fg_color_rgb, back_color=bg_color_rgb)

        img_io = io.BytesIO()
        img.save(img_io, 'PNG', optimize=True)
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    except Exception as e:
        print('Download error:', str(e))  # Debug log
        return render_template('index.html', error=f"Failed to generate QR code: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)