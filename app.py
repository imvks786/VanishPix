from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)
directory_path = os.path.dirname(__file__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_image():
    if request.method == 'POST':
        image = request.files['image']
        # GETTING FILE FROM USER
        file_name = image.filename
        input_file = os.path.join(directory_path, 'uploads', file_name)
        image.save(input_file)

        with Image.open(input_file) as img:
            # Perform background removal
            img_array = remove(img)

            #Convert the image to RGB mode
            #result_img = img_array.convert('RGB')
            
            output_file = os.path.join(directory_path, 'processed', file_name)
            #result_img.save(output_file)
            img_array.save(output_file)

            
            return send_file(output_file, as_attachment=True)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
