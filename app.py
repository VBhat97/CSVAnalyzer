from flask import Flask,render_template,request,redirect
from werkzeug import secure_filename

app = Flask(__name__)
path ='C:\Users\V.Bhat\Desktop\GraduateStudies\Co-Corriculars\Projects\CSVAnalyzer\uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form-action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        email=request.form['email']
        file = request.files['myfile']
        filename = secure_filename(file.filename)
        UPLOAD_FOLDER = path
        file.save(UPLOAD_FOLDER, filename)   
        return render_template('form_action.html', email , file=file.filename)
    else:
        return redirect('/')