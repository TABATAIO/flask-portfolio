from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
@app.route('/work/MIGAKE')
def migake():
    return render_template('MIGAKE.jinja')

@app.route('/precompany')
def precompany():
    return render_template('precompany.jinja')

@app.route('/contact')
def contact():
    return render_template('contact.jinja')