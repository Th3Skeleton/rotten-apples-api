import csv
from pydantic import BaseModel

class Song(BaseModel):
    album_id: int
    name: str
    score: float

class SongsInAlbum(BaseModel):
    songs: list[Song]
    
def load_songs_from_csv(filepath: str) -> list[Song]:
    songs = []
    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                song = Song(
                    album_id=int(row['album_id']),
                    name=row['name'],
                    score=float(row['score'])
                )
                songs.append(song)
    except FileNotFoundError:
        print(f"File {filepath} not found")
    return songs

# Load the songs from CSV
songsTest: list[Song] = load_songs_from_csv('songs.csv')