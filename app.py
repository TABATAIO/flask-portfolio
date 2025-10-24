from flask import Flask, render_template, request, redirect, url_for, jsonify, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
import os
import boto3
from dotenv import load_dotenv
import json
from werkzeug.utils import secure_filename
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from functools import wraps
from datetime import datetime

# 環境変数を読み込む
load_dotenv('./etc/secrets/')  # .envファイルを読み込む

app = Flask(__name__)

#データベース設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')


# AWSの設定を環境変数から読み込む
app.config['S3_BUCKET'] = os.getenv('S3_BUCKET')
app.config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
app.config['AWS_REGION'] = os.getenv('AWS_REGION')

# Auth0設定
app.secret_key = os.getenv('SECRET_KEY')
if not app.secret_key:
    raise ValueError("SECRET_KEY must be set")
app.config['AUTH0_CLIENT_ID'] = os.getenv('AUTH0_CLIENT_ID')
app.config['AUTH0_CLIENT_SECRET'] = os.getenv('AUTH0_CLIENT_SECRET')
app.config['AUTH0_DOMAIN'] = os.getenv('AUTH0_DOMAIN')

# OAuthの設定
oauth = OAuth(app)
auth0 = oauth.register(
    'auth0',
    client_id=app.config['AUTH0_CLIENT_ID'],
    client_secret=app.config['AUTH0_CLIENT_SECRET'],
    api_base_url=f"https://{app.config['AUTH0_DOMAIN']}",
    access_token_url=f"https://{app.config['AUTH0_DOMAIN']}/oauth/token",
    authorize_url=f"https://{app.config['AUTH0_DOMAIN']}/authorize",
    client_kwargs={
        'scope': 'openid profile email',
    },
    server_metadata_url=f"https://{app.config['AUTH0_DOMAIN']}/.well-known/openid-configuration"
)

# AWS S3クライアント
s3_client = boto3.client('s3', 
                         aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
                         region_name=app.config['AWS_REGION'])



db = SQLAlchemy(app)

migrate = Migrate(app, db)

# ユーザーがログインしているかどうかを確認するデコレーター
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

#Class↓
class Works(db.Model):
    __tablename__='works'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    secondtitle = db.Column(db.String(225))
    description = db.Column(db.Text)
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
    works = Works.query.all()  # 全データを取得
    return render_template('index.jinja', works=works)
    
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

@app.route('/work/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/work/namelogo')
def namelogo():
    return render_template('namelogo.html')


@app.route('/add_page', methods=['GET', 'POST'])
@login_required
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

#動的ページの表示
@app.route('/work/<int:work_id>')
def work_detail(work_id):
    work = Works.query.get_or_404(work_id)
    return render_template('detail.jinja', content=work, otherimgs=json.loads(work.otherimgs), topimg = work.topimg)


# Auth0のログインページ
@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri=url_for('callback', _external=True))

# Auth0のコールバックページ
@app.route('/callback')
def callback():
    token = auth0.authorize_access_token()
    session['user'] = token.get('userinfo')
    return redirect(url_for('home'))

# Auth0のログアウトページ
@app.route('/logout')
def logout():
    session.clear()
    return redirect(f"https://{app.config['AUTH0_DOMAIN']}/v2/logout?returnTo={url_for('home', _external=True)}&client_id={app.config['AUTH0_CLIENT_ID']}")

# セッションに保存されたユーザー情報を表示するページ
@app.route('/profile')
def profile():
    if 'user' in session:
        return jsonify(session['user'])
    return redirect(url_for('login'))

#renderで環境設定に入れた鍵をちゃんと読めてるかの確認
@app.route('/check-env')
def check_env():
    return {
        "S3_BUCKET": os.getenv('S3_BUCKET'),
        "AWS_ACCESS_KEY_ID": os.getenv('AWS_ACCESS_KEY_ID'),
        "AWS_SECRET_ACCESS_KEY": "HIDDEN_FOR_SECURITY",  # セキュリティ上非表示
        "AWS_REGION": os.getenv('AWS_REGION'),
        "AUTH0_DOMAIN": app.config['AUTH0_DOMAIN'],
        "AUTH0_CLIENT_ID": app.config['AUTH0_CLIENT_ID'],
        "AUTH0_CLIENT_SECRET": "HIDDEN"  # セキュリティ上非表示
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    pages = []
    base_url = "https://flask-portfolio-a21y.onrender.com"
    now = datetime.now().date().isoformat()

    # 静的なページを手動で登録（必要に応じて追加）
    static_pages = ['/', '/about', '/contact']
    for page in static_pages:
        pages.append(f"""
            <url>
                <loc>{base_url}{page}</loc>
                <lastmod>{now}</lastmod>
            </url>
        """)

    # 動的ページ（例：制作実績）をDBから取得
    works = Works.query.all()
    for work in works:
        pages.append(f"""
            <url>
                <loc>{base_url}/work/{work.id}</loc>
                <lastmod>{work.updated_at.date().isoformat()}</lastmod>
            </url>
        """)

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        {''.join(pages)}
    </urlset>"""

    return Response(sitemap_xml, mimetype='application/xml')