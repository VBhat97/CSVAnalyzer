from flask import Flask,render_template,request,redirect,flash
from werkzeug import secure_filename

app = Flask(__name__)
# UPLOAD_FOLDER = 'C:\Users\V.Bhat\Desktop\Graduate Studies\Co-Corriculars\Projects\CSVAnalyzer\uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(uploaded_file.filename)
            return render_template('form_action.html',filename=filename)
        return render_template('home.html',filename=filename)
    else:
        return redirect('/')
