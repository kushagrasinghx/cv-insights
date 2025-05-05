import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from utils.text import pdftotext
from utils.name import extract_name
from utils.emails import extract_email
from utils.phoneno import extract_phone_number
from utils.skills import extract_skills
from utils.education import extract_education

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ResumeParser:
    def __init__(self, filepath):
        self.text = pdftotext(filepath)

    def get_name(self):
        return extract_name(self.text)

    def get_email(self):
        return extract_email(self.text)

    def get_phone(self):
        return extract_phone_number(self.text)

    def get_skills(self):
        return extract_skills(self.text)

    def get_education(self):
        return extract_education(self.text)


@app.route('/')
def index():
    return render_template('index.html')  # form to upload PDF


@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return "No file part"

    file = request.files['resume']
    if file.filename == '':
        return "No selected file"

    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    parser = ResumeParser(path)
    
    # Split skills string into list (and strip extra spaces)
    raw_skills = parser.get_skills()
    skill_list = [skill.strip() for skill in raw_skills.split(",") if skill.strip()]

    result = {
        "name": parser.get_name(),
        "email": parser.get_email(),
        "phone": parser.get_phone(),
        "skills": skill_list,  # Pass as list to Jinja
        "education": parser.get_education(),
    }

    return render_template('dashboard.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
