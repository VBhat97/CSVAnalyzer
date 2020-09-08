from flask import Flask,render_template,request,redirect,flash,session
from werkzeug import secure_filename
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

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
        # TODO: Add case for no value entered.
        testcol = request.form.get("testcol")
        traincols=traincols.split('-')
        filename = session.get('filename', None)
        # TODO: Get header=0 from the user itself if not a proper csv file.
        data=pd.read_csv(filename,header=None)
        data_features=data.iloc[:,int(traincols[0]):int(traincols[1])]
        data_output=data.iloc[:,int(testcol)]
        X_train, X_test, y_train, y_test = train_test_split(data_features, data_output, test_size=0.2, random_state=42)
        clf = make_pipeline(StandardScaler(),LinearSVC(random_state=0, tol=1e-5))
        clf.fit(X_train, y_train)
        y_pred=clf.predict(X_test)
        print(accuracy_score(y_test,y_pred))
    return render_template('results.html', traincols=traincols, testcol=testcol)
