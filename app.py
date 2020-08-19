from flask import Flask,render_template,request,redirect
from werkzeug import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        filename='Hello'
        # file = request.files['file']
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('form_action.html',filename=filename)
    else:
        return redirect('/')
