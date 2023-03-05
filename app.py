from flask import Flask, request, render_template
from PIL import Image
import cv2
import os
import numpy as np

app = Flask(__name__)

os.makedirs('uploads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Obtem o arquivo enviado pelo usuário
    file = request.files['file']

    # Abre a imagem com a biblioteca Pillow
    img = Image.open(file)

    # Redimensiona a imagem para 500x500 pixels utilizando a biblioteca OpenCV
    img = np.array(img.resize((500, 500)))

    # Salva a imagem redimensionada em um diretório chamado "uploads"
    filename = file.filename
    filepath = os.path.join('uploads', filename)
    cv2.imwrite(filepath, img)

    # Retorna uma mensagem de sucesso para o usuário
    return 'Imagem salva com sucesso em: {}'.format(filepath)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
