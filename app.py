from flask import Flask,render_template,request,redirect
from werkzeug import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/V.Bhat/Desktop/Graduate Studies/Co-Corriculars/Projects/CSVAnalyzer/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form-action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':

    else:
        return redirect('/')
