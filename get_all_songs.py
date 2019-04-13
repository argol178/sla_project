from webapp import create_app
from webapp.add_song_text import get_new_song

app = create_app()
with app.app_context():
    get_new_song()