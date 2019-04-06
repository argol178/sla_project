import lyricsgenius
import pandas as pd


lyricsgenius.remove_section_headers = True  #Remove section headers (e.g. [Chorus]) from lyrics when searching
lyricsgenius.skip_non_songs = True  #Include hits thought to be non-songs (e.g. track lists)
lyricsgenius.excluded_terms = [
    "Remix", "Live", "Unplugged", "Demo", "Bonus",
    "Remastered", "Promo", "Version", "Instrumental"
    ]#Exclude songs with these words in their title


client_access_token = 'ke3Pnl3QrBw7R6QhKv_BieE80GfHg2CryO1Lru-Kdrvp9Kr78jngScx-5otrk0WV'
genius = lyricsgenius.Genius(client_access_token)
genius.verbose = True  # Turn off status messages
artist = genius.search_artist("Electric Wizard", sort="title")
artist.save_lyrics()
song_dataset = pd.DataFrame(columns=['Album', 'Title', 'Lyrics'])
#  print(artist.songs)
albums = {}
#  print(song.album, song.title)


for song in artist.songs:
    song_dataset = song_dataset.append({'Album': song.album, 'Title': song.title, 'Lyrics': song.lyrics},
                                       ignore_index=True)
#  print(song_dataset.head())
song_dataset = song_dataset.to_csv('song_dataset.csv', encoding='utf-8')


#  open csv
song_df = pd.read_csv('song_dataset.csv', encoding='utf-8', header=0, index_col=0, )
emotion_df = pd.read_csv('NRC_Emotion_Lexicon.csv', encoding='utf-8', header=0, index_col=0,)

#  data cleaning
exclude_sym = ["\n", "&", "/"]
song_df = song_df.replace(exclude_sym, ' ', regex=True)
song_df.fillna('No information', inplace=True)
