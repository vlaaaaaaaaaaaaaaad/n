from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_image', methods=['POST'])
def save_image():
    # Получаем данные изображения в base64
    data = request.json['image']
    # Убираем заголовок base64
    img_data = data.split(',')[1]
    # Декодируем изображение
    img_bytes = base64.b64decode(img_data)
    img_np = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    # Сохраняем изображение
    cv2.imwrite('saved_image.jpg', img)

    return jsonify({'message': 'Image saved successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

