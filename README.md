<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Flask-092E20.svg?logo=flask&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- ミドルウェア一覧 -->
  <img src="https://img.shields.io/badge/-Postgresql-4479A1.svg?logo=postgresql&style=for-the-badge&logoColor=white">
  <!-- インフラ一覧 -->
  <img src="https://img.shields.io/badge/-Amazon%20aws%20s3-232F3E.svg?logo=amazons3&style=for-the-badge">
</p>

<!-- プロジェジェクト名 -->
<p style="display: flex, ">
  Flask を用いたポートフォリオサイト
</p>
<!-- 経緯 -->

  ## 経緯

<p>
  静的サイトは作ったが、毎回自分でページを作るのが大変になったのと、学校で習ってことを実践するため、そして実際企業で働いた時にフロントだけ知っていても意味がないので実際のデプロイまで経験するべきと思い制作に取り掛かった。<br>
</p>
<span></span>

<!-- 説明 -->
 ## ちょこっと解説
<h2>Flaskを用いたポートフォリオサイト＆自動ページ追加Webアプリ</h2>
<p>
  Add_pageにてテキストと画像をフォームで受け取り、テキストはそのままdbに、画像はAmazon AWS S3にアップロードしたのち、そのurlをdbに格納して'/work/<int:work_id>'でidを取得してdbからた値を持ってきてdetail.jinjaで組み合わせて表示している。
</p>

<!-- tree -->
## tree
<p>
  .
├── Procfile
├── README.md
├── __pycache__
│   ├── app.cpython-310.pyc
│   ├── aws_s3.cpython-310.pyc
│   └── db.cpython-310.pyc
├── app.py
├── aws_s3.py
├── etc
│   └── secrets
├── flask_sqlalchemy
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── cli.cpython-310.pyc
│   │   ├── extension.cpython-310.pyc
│   │   ├── model.cpython-310.pyc
│   │   ├── pagination.cpython-310.pyc
│   │   ├── query.cpython-310.pyc
│   │   ├── record_queries.cpython-310.pyc
│   │   ├── session.cpython-310.pyc
│   │   ├── table.cpython-310.pyc
│   │   └── track_modifications.cpython-310.pyc
│   ├── cli.py
│   ├── extension.py
│   ├── model.py
│   ├── pagination.py
│   ├── py.typed
│   ├── query.py
│   ├── record_queries.py
│   ├── session.py
│   ├── table.py
│   └── track_modifications.py
├── migrations
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-310.pyc
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── __pycache__
│       │   └── cfe185efb922_initial_migration.cpython-310.pyc
│       └── cfe185efb922_initial_migration.py
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── 1nennseisakubutu.png
│   │   ├── About us.png
│   │   ├── BUILD(_after).png
│   │   ├── BUILD.png
│   │   ├── Discord.png
│   │   ├── Drnature.png
│   │   ├── EcoWave_Ventures_logo.png
│   │   ├── Login.png
│   │   ├── SVG
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

    セキュリティー保護のため'.env'はgit上にはあげていません。
</p>