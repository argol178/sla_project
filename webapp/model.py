from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Song {} {}>".format(self.song_title, self.artist)
