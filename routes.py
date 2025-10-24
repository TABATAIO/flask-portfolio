from flask import Blueprint, render_template, session, redirect, url_for
from functools import wraps
from models import Works

bp = Blueprint('routes', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def home():
    try:
        works = Works.query.all()
        return render_template('index.jinja', works=works)
    except Exception as e:
        # ログにエラーを記録
        app.logger.error(f"Error fetching works: {e}")
        # エラーページにリダイレクト
        return render_template('error.jinja', message="データの取得中にエラーが発生しました。")