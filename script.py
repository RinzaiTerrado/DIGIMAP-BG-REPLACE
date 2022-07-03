from flask import Flask, render_template,request
import os
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

        return render_template("index.html", filename=filename, filename2=filename2)

    return render_template("index.html")


app.run(port=5000)