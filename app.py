from flask import Flask,render_template,request,redirect,flash
from werkzeug import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_action', methods=["GET","POST"])
def form_action():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('home.html')
        file = request.files['file']
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('form_action.html',filename=filename)
    else:
        return redirect('/')
