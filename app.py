from flask import Flask,render_template,request,redirect,flash,session
from werkzeug import secure_filename
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

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
        checkbox_values=request.form.getlist('options')
        accuracy_SVC=0
        accuracy_kNN=0
        accuracy_NV=0
        accuracy_DTree=0
        accuracy_RF=0
        if 'SVC' in checkbox_values:
            clf = make_pipeline(StandardScaler(),LinearSVC(random_state=0, tol=1e-5))
            clf.fit(X_train, y_train)
            y_pred=clf.predict(X_test)
            accuracy_SVC=accuracy_score(y_pred,y_test)
        if 'kNN' in checkbox_values:
            # TODO: Fix n_neighbours value
            knnr = KNeighborsClassifier(n_neighbors = 3)
            knnr.fit(X_train, y_train)
            y_pred=knnr.predict(X_test)
            accuracy_kNN=accuracy_score(y_pred,y_test)
        if 'NV' in checkbox_values:
            gnb = GaussianNB()
            y_pred = gnb.fit(X_train, y_train).predict(X_test)
            accuracy_NV=accuracy_score(y_pred,y_test)
        if 'DTree' in checkbox_values:
            clf = tree.DecisionTreeClassifier()
            clf = clf.fit(X_train, y_train)
            y_pred=clf.predict(X_test)
            accuracy_DTree=accuracy_score(y_pred,y_test)
        if 'RF' in checkbox_values:
            clf = RandomForestClassifier(max_depth=2, random_state=0)
            clf.fit(X_train,y_train)
            y_pred=clf.predict(X_test)
            accuracy_RF=accuracy_score(y_pred,y_test)
        Accuracy_matrix=[]
        Name_matrix=[]
        if accuracy_SVC != 0:
            Accuracy_matrix.append(100*accuracy_SVC)
            Name_matrix.append('SVC')
        if accuracy_kNN != 0:
            Accuracy_matrix.append(100*accuracy_kNN)
            Name_matrix.append('kNN')
        if accuracy_NV != 0:
            Accuracy_matrix.append(100*accuracy_NV)
            Name_matrix.append('NV')
        if accuracy_DTree != 0:
            Accuracy_matrix.append(100*accuracy_DTree)
            Name_matrix.append('DTree')
        if accuracy_RF != 0:
            Accuracy_matrix.append(100*accuracy_RF)
            Name_matrix.append('RF')
        plt.figure(figsize=(9, 3))
        plt.bar(Name_matrix,Accuracy_matrix)
        print(Name_matrix)
        plt.savefig('static//img//foo.png')
        # TODO: Add till results on next page.
    return render_template('results.html', traincols=traincols, testcol=testcol)