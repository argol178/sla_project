from flask import Flask, render_template

from webapp.model import db, Songs

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def index():
        page_title = 'Тексты песен'
        hits_list = Songs.query.all()
        return render_template('index.html', page_title = page_title, hits = hits_list)

    return app