from flask import Flask,render_template,request,redirect,flash,session
from werkzeug import secure_filename
import pandas as pd

app = Flask(__name__)
app.secret_key = "aLKG21BFAJH"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            session['filename'] = filename
            uploaded_file.save(uploaded_file.filename)
            csvFile = pd.read_csv(filename)
            random_value=csvFile.shape[0]
            random_value2=csvFile.shape[1]
            return render_template('form_action.html',filename=filename,random_value=random_value,random_value2=random_value2)
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/results_action', methods=["GET","POST"])
def results_action():
    if request.method == 'POST':
        traincols = request.form.get("traincols")
        # TODO: Add case for no value entered
        testcol = request.form.get("testcol")
        traincols=traincols.split('-')
        filename = session.get('filename', None)
        data=pd.read_csv(filename)
        train_data=data[:,traincols[0]:traincols[1]]
        print(len(train_data))
        print(type(train_data))
        
        
    return render_template('results.html', traincols=traincols, testcol=testcol)
