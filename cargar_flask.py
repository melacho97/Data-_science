from flask import Flask, request
from werkzeug.utils import secure_filename
#from pandas import read_csv
import csv
#import numpy
from flask import jsonify
import os

app = Flask(__name__)
"""
#UPLOAD_FOLDER = "/home/juanfe/Escritorio/Data/Trabajos/uploads"
ALLOWED_EXTENSIONS = {'csv'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
#Define the path to the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Specifies the maximum size (in bytes) of the files to be uploaded
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded successfully'
        else:
            return 'No allowed extension'
"""
@app.route('/json_from_list')
def show_list():
        filename = "/home/melendes/Documentos/trabajos_data_science/data_science_fundamentals-master1/chapter_03/datasets/iris.csv"
        #names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
        #data = read_csv(filename, names=names)
        #return jsonify(data.shape)
        raw_data = open(filename, 'r')
        reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
        x = list(reader)
        return jsonify(x)
if __name__ == '__main__':
    app.run()


