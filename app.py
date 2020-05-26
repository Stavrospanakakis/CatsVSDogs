import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from ai.predict import Predict
from ai.train.train import Train

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SECRET_KEY = '3489eghrhpg3wg[43ghw34ghw340ghw3[5tgh'
app.config['SECRET_KEY'] = SECRET_KEY    

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
  for img in os.listdir(UPLOAD_FOLDER):
    os.remove(os.path.join(UPLOAD_FOLDER,img))
  return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_image():
  for img in os.listdir(UPLOAD_FOLDER):
    os.remove(os.path.join(UPLOAD_FOLDER,img))
  file = request.files['file']

  if file and allowed_file(file.filename):
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
  
    prediction = Predict(os.path.join(UPLOAD_FOLDER, filename))
    flash(prediction)
    return render_template('index.html', filename=filename)
  
  else:
    flash('Allowed image types are --> png, jpg, jpeg. Try uploading another image')
    return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename=filename), code=301)

@app.route('/train/')
def train_model():
  Train()
  return redirect("/")

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port)
	app.run(debug=False)
