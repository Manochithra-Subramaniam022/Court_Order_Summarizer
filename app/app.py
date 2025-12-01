# app/app.py
import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

# For PDF and DOCX text extraction
import fitz  # PyMuPDF
import docx


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.summarizer import summarize_order # Assuming this function exists


app = Flask(__name__)
# IMPORTANT: Change this to a random secret string for production
app.config['SECRET_KEY'] = 'a_very_secret_key_that_you_should_change' 
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Ensure the upload folder exists

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Redirect to login page if user is not authenticated
login_manager.login_message_category = 'info'

# =================================================================
# 2. DATABASE MODEL
# =================================================================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Flask-Login requires this function to load a user by ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =================================================================
# 3. HELPER FUNCTIONS FOR FILE PROCESSING
# =================================================================

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(filepath):
    """Extracts text from a PDF or DOCX file."""
    text = ""
    extension = filepath.rsplit('.', 1)[1].lower()
    
    if extension == "pdf":
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    elif extension == "docx":
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\\n"
            
    return text

# =================================================================
# 4. AUTHENTICATION ROUTES (SIGNUP, LOGIN, LOGOUT)
# =================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'warning')
            return redirect(url_for('signup'))
            
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# =================================================================
# 5. MAIN SUMMARIZER ROUTE (PROTECTED)
# =================================================================

@app.route("/", methods=["GET", "POST"])
@login_required # This decorator protects the route
def home():
    if request.method == "POST":
        text = request.form.get("order_text", "")
        file = request.files.get("file_input")

        # Prioritize file upload over text area
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            text = extract_text_from_file(filepath)
            
            os.remove(filepath) # Clean up the uploaded file

        if text.strip():
            # This is your core logic
            result = summarize_order(text) 
            return render_template("index.html", result=result, original_text=text)
    
    return render_template("index.html", result=None)

# =================================================================
# 6. MAIN EXECUTION
# =================================================================

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Creates the database file and tables if they don't exist
    app.run(debug=True)