from flask import Flask, render_template,request
import os
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from PIL import Image
from werkzeug.utils import secure_filename
app = Flask(__name__)


port = int(os.environ.get('PORT', 5000))


@app.route("/", methods=['POST',"GET"])
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
        image.save("static/images/"+filename)
        image2.save("static/images/"+filename2)




        return render_template("index.html", filename=filename, filename2=filename2)

    return render_template("index.html")

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename = '/Images/'+filename),code=301)
app.run(host='0.0.0.0', port=port, debug=True)
