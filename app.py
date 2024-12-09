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

@app.route('/work/brighttech')
def brighttech():
    return render_template('brighttech.jinja')

@app.route('/contact')
def contact():
    return render_template('contact.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/work/Logos')
def Logos():
    return render_template('Logos.jinja')

@app.route('/work/poster')
def dominos():
    return render_template('dominos_blackfriday_poster.jinja')