from flask import Flask, render_template,request
import os
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from PIL import Image
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = '/Users/Terra/Downloads/DIGIMAP/static/images'

@app.route("/home", methods=['POST',"GET"])
def upload_image():
    if request.method == "POST":
        image = request.files['file']
        image2 = request.files['file2']
        if image.filename == '' or image2.filename == '' :
            print("invalid file")
            return redirect(request.url)

        filename = secure_filename(image.filename)
        filename2 = secure_filename(image2.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"],filename))
        image2.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"],filename2))


        change_background_mp = mp.solutions.selfie_segmentation
        change_bg_segment = change_background_mp.SelfieSegmentation()

        sample_img = cv2.imread(os.path.join(basedir, app.config["IMAGE_UPLOADS"],filename))
        RGB_sample_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB)

        result = change_bg_segment.process(RGB_sample_img)
        binary_mask = result.segmentation_mask > 0.9
        binary_mask_3 = np.dstack((binary_mask,binary_mask,binary_mask))
        output_image = np.where(binary_mask_3, sample_img, 255)    
        bg_img = cv2.imread(os.path.join(basedir, app.config["IMAGE_UPLOADS"],filename2))

        output_image = np.where(binary_mask_3, sample_img, bg_img)  

        im = Image.fromarray(output_image)
        im.save("output.jpeg")


        return render_template("index.html", filename=filename, filename2=filename2)

    return render_template("index.html")


app.run(port=5000)
