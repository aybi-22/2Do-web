from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ein_sehr_starker_und_geheimer_schlüssel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meine_projektdatenbank.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)

from models import User

# Benutzermodell
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Datenbank initialisieren
with app.app_context():
    db.create_all()

class EventForm(FlaskForm):
    date = DateField('Date', validators=[InputRequired()])
    event = StringField('Event', validators=[InputRequired()])

# Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Login-Seite
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Ungültiger Benutzername oder Passwort')
    return render_template('login.html')

# Registrierungsseite
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('register.html', error="Benutzername bereits vergeben")
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        return redirect(url_for('home'))
    return render_template('register.html')

# Home-Seite nach dem Login
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

tasks = []  # Define the "tasks" variable

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

events = []  # Define the "events" variable

@app.route('/2DATE', methods=['GET', 'POST'])
def date():
    form = EventForm()
    if form.validate_on_submit():
        event_date = form.date.data
        event = form.event.data
        events.append({'date': event_date, 'event': event})
        return redirect(url_for('date'))
    return render_template('2DATE.html', form=form, events=events)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}  # Define the "ALLOWED_EXTENSIONS" variable

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

documents = []  # Define the "documents" variable

notes = []  # Define the "notes" variable

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
    db.create_all()
    app.run(debug=True)