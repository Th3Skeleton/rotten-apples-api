from enum import Enum

from songs import Song, SongsInAlbum, songsTest

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Genre(str, Enum):
    rock = "rock"
    pop = "pop"
    jazz = "jazz"
    classical = "classical"
    rap = "rap"
    rnb = "rnb"
    musical = "musical"
    edm = "edm"
    psychedelic = "psychedelic"
    lofi = "lofi"
    soul = "soul"
    hip_hop = "hip_hop"
    other = "other"
    
    
class Album(BaseModel):
    id: int
    title: str
    artist: str
    year: int
    score: float
    personal: float = 0.0
    mean: float = 0.0
    genre: Genre
    songs: list[Song] = []

albums = [
    Album(id=1, title="Shoot For The Stars, Aim For The Moon", artist="Pop Smoke", year=2020, score=81.79, personal=8.2, mean=8.16, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 1]),
    Album(id=2, title="GOD DID", artist="DJ Khaled", year=2022, score=52.95, personal=4.0, mean=6.59, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 2]),
    Album(id=3, title="Doo-Wops & Hooligans", artist="Bruno Mars", year=2010, score=94.40, personal=9.5, mean=9.38, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 3]),
    Album(id=4, title="Spider-Man: Into the Spider-Verse", artist="Various Artists", year=2018, score=79.00, personal=7.8, mean=8.00, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 4]),
    Album(id=5, title="TIM", artist="Avicii", year=2019, score=81.79, personal=8.1, mean=8.26, genre=Genre.edm, songs=[song for song in songsTest if song.album_id == 5]),
    Album(id=6, title="Music Of The Spheres", artist="Coldplay", year=2021, score=68.83, personal=7.0, mean=6.77, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 6]),
    Album(id=7, title="Parachutes", artist="Coldplay", year=2000, score=77.80, personal=7.6, mean=7.96, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 7]),
    Album(id=8, title="Ghost Stories", artist="Coldplay", year=2014, score=85.00, personal=8.5, mean=8.50, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 8]),
    Album(id=9, title="Legends Never Die", artist="Juice WRLD", year=2020, score=93.14, personal=9.6, mean=9.03, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 9]),
    Album(id=10, title="BALLADS 1", artist="Joji", year=2018, score=80.67, personal=8.0, mean=8.13, genre=Genre.rnb, songs=[song for song in songsTest if song.album_id == 10]),
    Album(id=11, title="17", artist="XXXTENTACION", year=2017, score=89.18, personal=9.0, mean=8.84, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 11]),
    Album(id=12, title="Nectar", artist="Joji", year=2020, score=82.28, personal=8.3, mean=8.16, genre=Genre.rnb, songs=[song for song in songsTest if song.album_id == 12]),
    Album(id=13, title="Circles", artist="Mac Miller", year=2020, score=94.00, personal=9.7, mean=9.10, genre=Genre.rnb, songs=[song for song in songsTest if song.album_id == 13]),
    Album(id=14, title="K.I.D.S. (Deluxe)", artist="Mac Miller", year=2018, score=81.33, personal=8.2, mean=8.07, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 14]),
    Album(id=15, title="JACKBOYS", artist="JACKBOYS", year=2019, score=84.93, personal=8.5, mean=8.49, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 15]),
    Album(id=16, title="SKINS", artist="XXXTENTACION", year=2018, score=72.20, personal=7.0, mean=7.44, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 16]),
    Album(id=17, title="?", artist="XXXTENTACION", year=2017, score=85.94, personal=8.7, mean=8.49, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 17]),
    Album(id=18, title="CALM", artist="5SOS", year=2020, score=75.15, personal=7.0, mean=8.03, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 18]),
    Album(id=19, title="Swimming", artist="Mac Miller", year=2018, score=91.46, personal=9.3, mean=8.99, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 19]),
    Album(id=20, title="IGOR", artist="Tyler, The Creator", year=2019, score=85.88, personal=8.7, mean=8.48, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 20]),
    Album(id=21, title="Life After The Show", artist="YourBoySponge", year=2023, score=70.09, personal=7.0, mean=7.02, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 21]),
    Album(id=22, title="Fighting Demons (DELUXE)", artist="Juice WRLD", year=2023, score=86.50, personal=8.7, mean=8.60, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 22]),
    Album(id=23, title="GB&GR", artist="Juice WRLD", year=2020, score=93.03, personal=9.5, mean=9.11, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 23]),
    Album(id=24, title="B.I.B.L.E.", artist="Fivio Foreign", year=2022, score=70.67, personal=6.8, mean=7.33, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 24]),
    Album(id=25, title="Curious George", artist="Jack Johnson", year=2006, score=84.81, personal=8.5, mean=8.46, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 25]),
    Album(id=26, title="homemade", artist="mamerico", year=2019, score=84.19, personal=8.4, mean=8.44, genre=Genre.jazz, songs=[song for song in songsTest if song.album_id == 26]),
    Album(id=27, title="Two / Seven", artist="Aso", year=2020, score=87.86, personal=8.8, mean=8.77, genre=Genre.lofi, songs=[song for song in songsTest if song.album_id == 27]),
    Album(id=28, title="Trip At Knight", artist="Trippie Redd", year=2021, score=68.89, personal=6.5, mean=7.28, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 28]),
    Album(id=29, title="FOTO", artist="Kota the Friend", year=2021, score=76.34, personal=7.5, mean=7.77, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 29]),
    Album(id=30, title="I Love Life, Thank You", artist="Mac Miller", year=2020, score=86.62, personal=8.8, mean=8.52, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 30]),
    Album(id=31, title="La La Land", artist="Various Artists", year=2016, score=89.73, personal=9.1, mean=8.85, genre=Genre.musical, songs=[song for song in songsTest if song.album_id == 31]),
    Album(id=32, title="THE GOAT", artist="Polo G", year=2023, score=81.87, personal=8.0, mean=8.37, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 32]),
    Album(id=33, title="B4 The Storm", artist="Internet Money", year=2021, score=65.46, personal=7.0, mean=6.09, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 33]),
    Album(id=34, title="A Love Letter To You 4", artist="Trippie Redd", year=2019, score=83.45, personal=8.3, mean=8.39, genre=Genre.hip_hop, songs=[song for song in songsTest if song.album_id == 34]),
    Album(id=35, title="Donda", artist="Kanye West", year=2021, score=74.04, personal=7.0, mean=7.81, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 35]),
    Album(id=36, title="SMITHEREENS", artist="Joji", year=2017, score=86.33, personal=8.4, mean=8.87, genre=Genre.soul, songs=[song for song in songsTest if song.album_id == 36]),
    Album(id=37, title="A Head Full Of Dreams", artist="Coldplay", year=2015, score=82.45, personal=8.0, mean=8.49, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 37]),
    Album(id=38, title="DR4L", artist="Juice WRLD", year=2020, score=87.70, personal=8.9, mean=8.64, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 38]),
    Album(id=39, title="Punk", artist="Young Thug", year=2021, score=66.35, personal=6.4, mean=6.87, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 39]),
    Album(id=40, title="÷ (DELUXE)", artist="Ed Sheeran", year=2017, score=90.19, personal=9.0, mean=9.04, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 40]),
    Album(id=41, title="x (DELUXE)", artist="Ed Sheeran", year=2014, score=85.44, personal=8.3, mean=8.79, genre=Genre.rnb, songs=[song for song in songsTest if song.album_id == 41]),
    Album(id=42, title="Her Loss", artist="Drake & 21 Savage", year=2022, score=81.53, personal=7.8, mean=8.51, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 42]),
    Album(id=43, title="Yeezus", artist="Kanye West", year=2013, score=77.05, personal=7.2, mean=8.21, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 43]),
    Album(id=44, title="channel ORANGE", artist="Frank Ocean", year=2012, score=86.24, personal=8.9, mean=8.35, genre=Genre.rnb, songs=[song for song in songsTest if song.album_id == 44]),
    Album(id=45, title="Best Day Ever", artist="Mac Miller", year=2010, score=83.22, personal=8.2, mean=8.44, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 45]),
    Album(id=46, title="HEROES & VILLIANS", artist="Metro Boomin", year=2022, score=84.60, personal=8.3, mean=8.62, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 46]),
    Album(id=47, title="Graduation", artist="Kanye West", year=2007, score=91.68, personal=9.4, mean=8.94, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 47]),
    Album(id=48, title="Its Almost Dry", artist="Pusha T", year=2022, score=82.67, personal=8.0, mean=8.53, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 48]),
    Album(id=49, title="MBDTF", artist="Kanye West", year=2010, score=89.19, personal=9.0, mean=8.84, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 49]),
    Album(id=50, title="Good Job", artist="Cookin Soul", year=2020, score=81.30, personal=8.0, mean=8.26, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 50]),
    Album(id=51, title="JESUS IS KING", artist="Kanye West", year=2019, score=72.14, personal=6.5, mean=7.93, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 51]),
    Album(id=52, title="Cheers to the Best Memories", artist="dvsn & TD$", year=2023, score=80.50, personal=8.0, mean=8.10, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 52]),
    Album(id=53, title="MANSION MUSIK", artist="Trippie Redd", year=2023, score=63.40, personal=5.0, mean=7.68, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 53]),
    Album(id=54, title="Starboy", artist="The Weeknd", year=2016, score=90.39, personal=9.2, mean=8.88, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 54]),
    Album(id=55, title="Like..?", artist="Ice Spice", year=2023, score=47.25, personal=3.0, mean=6.45, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 55]),
    Album(id=56, title="Let's Start Here.", artist="Lil Yachty", year=2023, score=88.68, personal=9.0, mean=8.74, genre=Genre.psychedelic, songs=[song for song in songsTest if song.album_id == 56]),
    Album(id=57, title="i am > i was", artist="21 Savage", year=2018, score=83.53, personal=8.0, mean=8.71, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 57]),
    Album(id=58, title="Meet The Woo", artist="Pop Smoke", year=2019, score=72.22, personal=7.3, mean=8.14, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 58]),
    Album(id=59, title="MOTM", artist="Kid Cudi", year=2009, score=89.33, personal=9.0, mean=8.87, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 59]),
    Album(id=60, title="Whole Lotta Red", artist="Playboi Carti", year=2020, score=77.63, personal=7.3, mean=8.23, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 60]),
    Album(id=61, title="UTOPIA", artist="Travis Scott", year=2023, score=87.18, personal=8.7, mean=8.74, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 61]),
    Album(id=62, title="Austin", artist="Post Malone", year=2023, score=87.10, personal=0.0, mean=0.00, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 62]),
    Album(id=63, title="SpiderMan: Across the Spider-Verse", artist="Metro Boomin", year=2023, score=85.22, personal=8.5, mean=8.54, genre=Genre.hip_hop, songs=[song for song in songsTest if song.album_id == 63]),
    Album(id=64, title="Flower Boy", artist="Tyler, The Creator", year=2017, score=87.42, personal=8.7, mean=8.77, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 64]),
    Album(id=65, title="Moon Music", artist="Coldplay", year=2024, score=75.10, personal=7.0, mean=8.02, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 65]),
    Album(id=66, title="GNX", artist="Kendrick Lamar", year=2024, score=90.63, personal=9.0, mean=9.13, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 66]),
    Album(id=67, title="CHROMAKOPIA", artist="Tyler, The Creator", year=2024, score=87.32, personal=8.7, mean=8.76, genre=Genre.rap, songs=[song for song in songsTest if song.album_id == 67]),
    Album(id=68, title="Unorthodox Jukebox", artist="Bruno Mars", year=2012, score=93.90, personal=9.6, mean=9.18, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 68]),
    Album(id=69, title="Random Access Memories", artist="Daft Punk", year=2013, score=90.50, personal=9.2, mean=8.90, genre=Genre.edm, songs=[song for song in songsTest if song.album_id == 69]),
    Album(id=70, title="The Stranger", artist="Billy Joel", year=1977, score=95.17, personal=9.6, mean=9.43, genre=Genre.pop, songs=[song for song in songsTest if song.album_id == 70]),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# This endpoint will match any path that starts with /album/ followed by an integer (the album_id).
# The album_id will be passed as a parameter to the read_item function, and the optional query parameter q can also be included in the request.
@app.get("/album/{album_id}")
def query_album_by_id(album_id: int) -> Album:
    if album_id not in range(1, len(albums) + 1):
        raise HTTPException(status_code=404, detail="Album not found")
    return albums[album_id - 1]