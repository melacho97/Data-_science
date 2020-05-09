from flask import Flask, request
from werkzeug.utils import secure_filename
#from pandas import read_csv
import csv
#import numpy
from flask import jsonify
import os

app = Flask(__name__)

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


