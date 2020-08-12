from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form-action')
def form_action():
    return render_template('form_action.html', email=request.args['email'])