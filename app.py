from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import boto3
from dotenv import load_dotenv
import json
from werkzeug.utils import secure_filename
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

# 環境変数を読み込む
load_dotenv('./etc/secrets/')  # .envファイルを読み込む

app = Flask(__name__)

#データベース設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://iotabata:hoKvRQ2ojxTyouzYidvcM553GTtQXVvf@dpg-ctj6jt5svqrc7386fna0-a:5432/iotabata_db_for_flask_app_rexz'
app.config['UPLOAD_FOLDER'] = 'uploads/'


# AWSの設定を環境変数から読み込む
app.config['S3_BUCKET'] = os.getenv('S3_BUCKET')
app.config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
app.config['AWS_REGION'] = os.getenv('AWS_REGION')

# AWS S3クライアント
s3_client = boto3.client('s3', 
                         aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
                         region_name=app.config['AWS_REGION'])

db = SQLAlchemy(app)

migrate = Migrate(app, db)



#Class↓
class Works(db.Model):
    __tablename__='works'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    secondtitle = db.Column(db.String(225))
    description = db.Column(db.String(500))
    topimg = db.Column(db.String(225))
    otherimgs = db.Column(JSON, nullable=True)  # JSON形式で複数画像のURLを保存
    created_at = db.Column(db.DateTime,default = datetime.now)
    updated_at = db.Column(db.DateTime,default = datetime.now, onupdate=datetime.now)
    
    def set_otherimgs(self, image_urls):
        self.otherimgs = image_urls

    def get_otherimgs(self):
        return self.otherimgs or []


#root↓
@app.route('/')
def home():
    return render_template('index.jinja')
    
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


@app.route('/add_page', methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        # フォームデータの取得
        title = request.form['title']
        secondtitle = request.form['secondtitle']
        description = request.form['description']

        # S3に画像をアップロードしてURLを取得
        topimg_file = request.files['topimg']
        topimg_filename = secure_filename(topimg_file.filename)
        topimg_url = upload_to_s3(topimg_file, topimg_filename)

        otherimgs_files = request.files.getlist('otherimage')
        otherimgs_urls = [
            upload_to_s3(img, secure_filename(img.filename)) for img in otherimgs_files
        ]

        # データベースに保存
        work = Works(
            title=title,
            secondtitle=secondtitle,
            description=description,
            topimg=topimg_url,
            otherimgs=json.dumps(otherimgs_urls)
        )
        db.session.add(work)
        db.session.commit()

        return redirect(url_for('work_detail', work_id=work.id))

    return render_template('add_page.html')

# S3にアップロードする関数
def upload_to_s3(file, filename):
    s3_client.upload_fileobj(file, app.config['S3_BUCKET'], filename)
    return f"https://{app.config['S3_BUCKET']}.s3.{app.config['AWS_REGION']}.amazonaws.com/{filename}"

@app.route('/work/<int:work_id>')
def work_detail(work_id):
    work = Works.query.get_or_404(work_id)
    return render_template('detail.jinja', content=work, otherimgs=json.loads(work.otherimgs), topimg = work.topimg)

#renderで環境設定に入れた鍵をちゃんと読めてるかの確認
@app.route('/check-env')
def check_env():
    return {
        "S3_BUCKET": os.getenv('S3_BUCKET'),
        "AWS_ACCESS_KEY_ID": os.getenv('AWS_ACCESS_KEY_ID'),
        "AWS_SECRET_ACCESS_KEY": "HIDDEN_FOR_SECURITY",  # セキュリティ上非表示
        "AWS_REGION": os.getenv('AWS_REGION')
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)