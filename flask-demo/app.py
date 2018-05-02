#coding:utf-8

import os
import time

from flask import Flask, jsonify, abort, render_template, request, make_response, send_from_directory

import service
from config import sql


app = Flask(__name__)



@app.route('/api/test', methods=['GET'])
def test():
    filename = "a.jpg"
    dirpath = os.path.join(app.root_path, 'upload')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True)  



@app.route('/')
def test_():
    import datetime
    datetime = str(datetime.datetime.now())
    start_date, end_date = service.get_date()
    data = {
        'start_date': start_date,
        'end_date': end_date,
        'time': datetime
    }
    return render_template('upload.html', **data)



@app.route('/api/result', methods=['POST'])
def result():
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    data = service.get_hello(start_date, end_date)
    filename = service.save_excel(data)

    dirpath = os.path.join(app.root_path, 'upload')
    return send_from_directory(dirpath, filename, as_attachment=True)  



if __name__ == '__main__':
    app.run()