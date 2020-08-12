from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form-action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        return render_template('form_action.html', email=request.form['email'], file=request.form['myfile'])
    else :
        return redirect('/')