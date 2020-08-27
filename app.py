from flask import Flask,render_template,request,redirect,flash
from werkzeug import secure_filename
import pandas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        print('Hi')
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(uploaded_file.filename)
            return render_template('form_action.html',filename=filename)
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/results_action', methods=["GET","POST"])
def results_action():
    if request.method == 'POST':
        trainrows = request.form.get("trainrows")
        testrows = request.form.get("testrows")
        csvFile = pandas.read_csv('Housing.csv')
        # TODO: Working correctly, just find a proper csv for uploading.
        # random_value=csvFile.shape[0]
        # print(random_value)

    return render_template('results.html', trainrows=trainrows, testrows=testrows,random_value=random_value)
