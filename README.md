# Flask Portfolio

## 📝 概要
Flask製のポートフォリオサイト＆コンテンツ管理システム。Auth0による認証とAWS S3によるメディア管理を実装したモダンなウェブアプリケーションです。

## 🛠 使用技術

### バックエンド
![Flask](https://img.shields.io/badge/-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

### フロントエンド
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### インフラ・その他
![AWS S3](https://img.shields.io/badge/-Amazon%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)
![Auth0](https://img.shields.io/badge/-Auth0-EB5424?style=for-the-badge&logo=auth0&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## ✨ 主要機能

- 📱 レスポンシブデザイン
- 🔒 Auth0による安全な認証
- 💾 AWS S3によるメディアファイル管理
- 📝 コンテンツの動的追加・編集
- 🎨 カスタマイズ可能なポートフォリオページ

## 💡 開発経緯

フロントエンドだけでなく、バックエンドの実践的な経験を積むために開発を始めました。
主な目標は：

1. 動的コンテンツ管理の実装
2. クラウドサービス（AWS S3）の活用
3. セキュアな認証システムの導入
4. データベース設計と管理の実践
5. 本番環境へのデプロイ経験

## 🔍 システム概要

- フォームからのコンテンツ投稿機能
- AWS S3を利用した画像管理システム
- PostgreSQLによるデータ永続化
- Auth0による安全な認証
- レスポンシブなUI/UXデザイン

## 🚀 セットアップ

### 前提条件
- Python 3.8以上
- PostgreSQL
- AWS アカウント（S3バケット用）
- Auth0アカウント

### インストール手順

1. リポジトリのクローン
```bash
git clone https://github.com/TABATAIO/flask-portfolio.git
cd flask-portfolio
```

2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\\Scripts\\activate
```

3. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
```bash
# .envファイルを作成し、以下の変数を設定
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
AUTH0_CLIENT_ID=your-auth0-client-id
AUTH0_CLIENT_SECRET=your-auth0-client-secret
AUTH0_DOMAIN=your-auth0-domain
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_REGION=your-aws-region
S3_BUCKET=your-bucket-name
```

5. データベースのセットアップ
```bash
flask db upgrade
```

6. アプリケーションの起動
```bash
flask run
```

## 📁 プロジェクト構造

```
.
├── app.py              # メインアプリケーション
├── models.py           # データベースモデル
├── routes.py           # ルート定義
├── aws_s3.py          # AWS S3関連の処理
├── static/            # 静的ファイル
│   ├── css/
│   ├── js/
│   └── images/
├── templates/         # テンプレート
├── migrations/        # データベースマイグレーション
└── etc/
    └── secrets/      # 環境変数
```

## 🔧 開発環境のセットアップ

開発環境では以下の追加パッケージをインストールすることを推奨します：

```bash
pip install pytest pytest-cov black flake8
```

## 📝 コントリビューション

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

[MIT License](LICENSE)

## 👥 作者

- TABATA IO - [GitHub](https://github.com/TABATAIO)

## 🙏 謝辞

- [Flask](https://flask.palletsprojects.com/)
- [Auth0](https://auth0.com/)
- [AWS](https://aws.amazon.com/)
│   │   │   └── forsplash_namelogo.svg
│   │   ├── Top.png
│   │   ├── X.png
│   │   ├── app_logoMIGAKE.png
│   │   ├── confalence.png
│   │   ├── dominos_pizza_poster.png
│   │   ├── fasion.png
│   │   ├── forsplash_namelogo.svg
│   │   ├── home.png
│   │   ├── icon_about.png
│   │   ├── icon_contact.png
│   │   ├── icon_home.png
│   │   ├── icon_top.png
│   │   ├── icon_works.png
│   │   ├── instagram.png
│   │   ├── logo1.png
│   │   ├── mail.jpg
│   │   ├── me_adlt.png
│   │   ├── me_child.png
│   │   ├── migake_route.png
│   │   ├── my_logo.png
│   │   ├── phone.png
│   │   ├── precompany_ABOUTUS(for phone).png
│   │   ├── precompany_PROJECTS(for phone).png
│   │   ├── precompany_Top(for phone).png
│   │   ├── precompany_contact(for phone).png
│   │   ├── precompany_contact.png
│   │   ├── precompany_projectdetail.png
│   │   ├── precompany_top.png
│   │   ├── schoolfecworks.png
│   │   ├── unknown_coffee_logo-(1).png
│   │   ├── wave1.png
│   │   ├── wave2.png
│   │   ├── windelect.svg
│   │   └── wood.png
│   └── js
│       └── my_script.js
└── templates
    ├── Logos.jinja
    ├── MIGAKE.jinja
    ├── about.jinja
    ├── add_page.html
    ├── base.jinja
    ├── brighttech.jinja
    ├── contact.jinja
    ├── detail.jinja
    ├── dominos_blackfriday_poster.jinja
    └── index.jinja
<br>
セキュリティー保護のため'.env'はgit上にはあげていません。
</p>
