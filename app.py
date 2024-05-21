from flask import Flask, jsonify, request, render_template
import io, base64

from utils import generate_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Generate the image
    image = generate_image(prompt)
    
    # Convert the PIL image to base64
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    encoded_image = base64.b64encode(img_byte_arr).decode('utf-8')

    return jsonify({'image': encoded_image})


if __name__ == '__main__':
    app.run(debug=True)
