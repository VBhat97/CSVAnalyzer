from flask import Flask,render_template,request,redirect
from werkzeug import secure_filename

app = Flask(__name__)
path ='C:/Users/V.Bhat/Desktop/Graduate Studies/Co-Corriculars/Projects/CSVAnalyzer/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form-action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        file = request.form['file']
        filename = secure_filename(file.filename)
        return render_template('form_action.html' , file=file.filename)
    else:
        return redirect('/')
