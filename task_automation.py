from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    unique_emails = {email.lower() for email in emails}
    return sorted(unique_emails)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    text = file.read().decode('utf-8')
    emails = extract_emails(text)
    return render_template('results.html', emails=emails)

if __name__ == '__main__':
    app.run(debug=True)
