from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import DateField  # Änderung des Imports für DateField
from wtforms.validators import InputRequired
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

tasks = []
documents = []
notes = []
events = []

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt'}

class EventForm(FlaskForm):
    date = DateField('Date', validators=[InputRequired()])
    event = StringField('Event', validators=[InputRequired()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/2DO', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_name = request.form['task']
        tasks.append({'name': task_name, 'completed': False})
    return render_template('2DO.html', tasks=tasks)

@app.route('/delete_task/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect(url_for('todo'))

@app.route('/2DATE', methods=['GET', 'POST'])
def date():
    form = EventForm()
    if form.validate_on_submit():
        event_date = form.date.data
        event = form.event.data
        events.append({'date': event_date, 'event': event})
        return redirect(url_for('date'))
    return render_template('2DATE.html', form=form, events=events)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/2DOC', methods=['GET', 'POST'])
def doc():
    if request.method == 'POST':
        if 'document' in request.files:
            file = request.files['document']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                documents.append({'filename': filename})
                return redirect(url_for('doc'))
        elif 'note' in request.form:
            note = request.form['note']
            notes.append(note)
            return redirect(url_for('doc'))
    return render_template('2DOC.html', documents=documents, notes=notes)

@app.route('/view_document/<filename>')
def view_document(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/back')
def back():
    referrer = request.referrer or url_for('home')
    return redirect(referrer)

if __name__ == '__main__':
    app.run(debug=True)
