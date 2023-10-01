from flask import Flask, render_template, request, send_file
from flask_uploads import UploadSet, configure_uploads, IMAGES


import os

app = Flask(__name__)

@app.route("/")
def hello_zap():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)