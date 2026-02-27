# Email Extracter Web App

A modern Flask‑based web application that extracts, deduplicates, normalizes, and sorts email addresses from uploaded text files. Built as part of the **CodeAlpha
Internship**, this project blends technical precision with a sleek, professional UI powered by TailwindCSS and custom CSS.

---

## Features
- Upload `.txt` files and automatically extract valid email addresses using regex.
- Case‑insensitive deduplication and alphabetical sorting for clean results.
- Responsive UI with a blue gradient background and glowing buttons.
- Results displayed in a professional table with hover effects.
- Option to re‑upload files for multiple runs.

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, TailwindCSS, custom CSS  
- **Regex:** Robust pattern for email validation  

---

## Getting Started

### Prerequisites
- Python 3.8+ installed
- pip installed and working

### Installation
1. Clone the repository:
   
2. Install dependencies:
  python -m pip install -r requirements.txt
  
3. Run the app:
  python app.py

4. Open in browser:
http://127.0.0.1:5000

## Project Structure
Code
CodeAlpha_EmailExtracter/
│── app.py
│── requirements.txt
│── templates/
│    └── index.html
│    └── results.html
│── static/
│    └── style.css
│── README.md
│── LICENSE

## Screenshots
Add screenshots of your UI here (index page + results page) to showcase the design.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

## License
This project is licensed under the MIT License — feel free to use and adapt it.

## Acknowledgements
Developed during CodeAlpha Python Internship
TailwindCSS for rapid UI styling
Flask for lightweight backend development

---

git clone https://github.com/Mairaarshad19/CodeAlpha_EmailExtracter.git
cd CodeAlpha_EmailExtracter
