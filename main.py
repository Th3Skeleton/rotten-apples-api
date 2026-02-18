from enum import Enum
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

import csv

DATABASE_URL = "sqlite:///./albums.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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

class StatsDB(Base):
    __tablename__ = "stats"
    
    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("albums.id"))
    album_rank = Column(Integer)
    highest_song_rank = Column(Integer)
    rank_in_year = Column(Integer)
    rank_in_genre = Column(Integer)
    album = relationship("AlbumDB", back_populates="stats")

class SongDB(Base):
    __tablename__ = "songs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Float)
    album_id = Column(Integer, ForeignKey("albums.id"))
    album = relationship("AlbumDB", back_populates="songs")

class AlbumDB(Base):
    __tablename__ = "albums"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    year = Column(Integer)
    score = Column(Float)
    personal = Column(Float, default=0.0)
    mean = Column(Float, default=0.0)
    leng = Column(String, default=0)
    rec = Column(String, default="")
    review_date = Column(String, default="")
    stats = relationship("StatsDB", back_populates="album")
    genre = Column(String)
    songs = relationship("SongDB", back_populates="album")

class Stats(BaseModel):
    album_rank: int
    highest_song_rank: int
    rank_in_year: int
    rank_in_genre: int

    class Config:
        orm_mode = True

class Song(BaseModel):
    id: int
    name: str
    score: float
    album_id: int
    
    class Config:
        from_attributes = True

class Album(BaseModel):
    id: int
    title: str
    artist: str
    year: int
    score: float
    personal: float = 0.0
    mean: float = 0.0
    leng: str = "0"
    rec: str = ""
    review_date: str = ""
    stats: list[Stats] = []
    genre: Genre
    songs: list[Song] = []
    
    class Config:
        from_attributes = True

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Check if data already exists
        existing_songs = db.query(SongDB).first()
        existing_albums = db.query(AlbumDB).first()
        existing_stats = db.query(StatsDB).first()
        
        if existing_songs is None or existing_albums is None:
            # Load songs from CSV and add to database
            try:
                with open('songs.csv', 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        song = SongDB(
                            name=row['name'],
                            score=float(row['score']),
                            album_id=int(row['album_id'])
                        )
                        db.merge(song)
                db.commit()
            except FileNotFoundError:
                pass

            # Add albums to database
            albums = [
                Album(id=1, title="Shoot For The Stars, Aim For The Moon", artist="Pop Smoke", year=2020, score=81.79, personal=8.2, mean=8.16, leng="56:41", rec="Yes", review_date="10-09-2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=2, title="GOD DID", artist="DJ Khaled", year=2022, score=52.95, personal=4.0, mean=6.59, leng="57:11", rec="Only a few songs, not every", review_date="10-09-2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=3, title="Doo-Wops & Hooligans", artist="Bruno Mars", year=2010, score=94.40, personal=9.5, mean=9.38, leng="35:26", rec="ABSOLUTELY, LISTEN TO THIS!", review_date="10-09-2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=4, title="Spider-Man: Into the Spider-Verse", artist="Various Artists", year=2018, score=79.00, personal=7.8, mean=8.00, leng="41:41", rec="Its a surprising one so ye :>", review_date="10-10-2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=5, title="TIM", artist="Avicii", year=2019, score=81.79, personal=8.1, mean=8.26, leng="38:58", rec="If you like EDM, you like TIM", review_date="10-10-2022", genre=Genre.edm, stats=[], songs=[]),
                Album(id=6, title="Music Of The Spheres", artist="Coldplay", year=2021, score=68.83, personal=7.0, mean=6.77, leng="41:50", rec="Anything but the emojis", review_date="10-10-2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=7, title="Parachutes", artist="Coldplay", year=2000, score=77.80, personal=7.6, mean=7.96, leng="41:55", rec="Listen until Parachutes", review_date="10-10-2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=8, title="Ghost Stories", artist="Coldplay", year=2014, score=85.00, personal=8.5, mean=8.50, leng="40:18", rec="Some but yes", review_date="10-10-2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=9, title="Legends Never Die", artist="Juice WRLD", year=2020, score=93.14, personal=9.6, mean=9.03, leng="58:48", rec="you're gonna jus have to listen to it", review_date="10-10-2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=10, title="BALLADS 1", artist="Joji", year=2018, score=80.67, personal=8.0, mean=8.13, leng="35:11", rec="Yes", review_date="10-10-2022", genre=Genre.rnb, stats=[], songs=[]),
                Album(id=11, title="17", artist="XXXTENTACION", year=2017, score=89.18, personal=9.0, mean=8.84, leng="21:59", rec="Yess", review_date="10-10-2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=12, title="Nectar", artist="Joji", year=2020, score=82.28, personal=8.3, mean=8.16, leng="53:14", rec="YESS", review_date="10/17/2022", genre=Genre.rnb, stats=[], songs=[]),
                Album(id=13, title="Circles", artist="Mac Miller", year=2020, score=94.00, personal=9.7, mean=9.10, leng="48:44", rec="Look at the score, thats it", review_date="10/17/2022", genre=Genre.rnb, stats=[], songs=[]),
                Album(id=14, title="K.I.D.S. (Deluxe)", artist="Mac Miller", year=2018, score=81.33, personal=8.2, mean=8.07, leng="54:00", rec="a blast from the past, listen", review_date="10/17/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=15, title="JACKBOYS", artist="JACKBOYS", year=2019, score=84.93, personal=8.5, mean=8.49, leng="21:22", rec="Fire", review_date="10/27/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=16, title="SKINS", artist="XXXTENTACION", year=2018, score=72.20, personal=7.0, mean=7.44, leng="19:47", rec="Not the whole album. But yes?", review_date="10/17/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=17, title="?", artist="XXXTENTACION", year=2017, score=85.94, personal=8.7, mean=8.49, leng="37:35", rec="If you're sad sure lol", review_date="10/17/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=18, title="CALM", artist="5SOS", year=2020, score=75.15, personal=7.0, mean=8.03, leng="43:31", rec="Some songs not all", review_date="10/17/2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=19, title="Swimming", artist="Mac Miller", year=2018, score=91.46, personal=9.3, mean=8.99, leng="58:39", rec="LISTEN TO THIS ALBUM", review_date="10/17/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=20, title="IGOR", artist="Tyler, The Creator", year=2019, score=85.88, personal=8.7, mean=8.48, leng="39:46", rec="Yesssss", review_date="10/18/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=21, title="Life After The Show", artist="YourBoySponge", year=2023, score=70.09, personal=7.0, mean=7.02, leng="33:51", rec="If you want a laugh yea", review_date="10/19/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=22, title="Fighting Demons (DELUXE)", artist="Juice WRLD", year=2023, score=86.50, personal=8.7, mean=8.60, leng="1:14:00", rec="YES", review_date="10/21/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=23, title="GB&GR", artist="Juice WRLD", year=2020, score=93.03, personal=9.5, mean=9.11, leng="47:30", rec="YESSSS", review_date="10/21/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=24, title="B.I.B.L.E.", artist="Fivio Foreign", year=2022, score=70.67, personal=6.8, mean=7.33, leng="53:36", rec="Some not all", review_date="10/24/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=25, title="Curious George", artist="Jack Johnson", year=2006, score=84.81, personal=8.5, mean=8.46, leng="40:06", rec="YES", review_date="10/25/2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=26, title="homemade", artist="mamerico", year=2019, score=84.19, personal=8.4, mean=8.44, leng="29:02", rec="for comfort, yes", review_date="10/26/2022", genre=Genre.jazz, stats=[], songs=[]),
                Album(id=27, title="Two / Seven", artist="Aso", year=2020, score=87.86, personal=8.8, mean=8.77, leng="26:11", rec="for comfort, yes", review_date="10/27/2022", genre=Genre.lofi, stats=[], songs=[]),
                Album(id=28, title="Trip At Knight", artist="Trippie Redd", year=2021, score=68.89, personal=6.5, mean=7.28, leng="49:36", rec="if its high, listen to it", review_date="10/28/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=29, title="FOTO", artist="Kota the Friend", year=2021, score=76.34, personal=7.5, mean=7.77, leng="59:57", rec="Sure if you want something new", review_date="10/28/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=30, title="I Love Life Thank You", artist="Mac Miller", year=2020, score=86.62, personal=8.8, mean=8.52, leng="36:17", rec="YESSS", review_date="10/28/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=31, title="La La Land", artist="Various Artists", year=2016, score=89.73, personal=9.1, mean=8.85, leng="36:17", rec="YESSS", review_date="10/28/2022", genre=Genre.musical, stats=[], songs=[]),
                Album(id=32, title="THE GOAT", artist="Polo G", year=2023, score=81.87, personal=8.0, mean=8.37, leng="47:10", rec="YESSS", review_date="10/28/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=33, title="B4 The Storm", artist="Internet Money", year=2021, score=65.46, personal=7.0, mean=6.09, leng="48:13", rec="Not really", review_date="10/29/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=34, title="A Love Letter To You 4", artist="Trippie Redd", year=2019, score=83.45, personal=8.3, mean=8.39, leng="59:08", rec="Yeah", review_date="10/31/2022", genre=Genre.hip_hop, stats=[], songs=[]),
                Album(id=35, title="Donda", artist="Kanye West", year=2021, score=74.04, personal=7.0, mean=7.81, leng="1:48:00", rec="Not the full thing, some tho", review_date="10/31/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=36, title="SMITHEREENS", artist="Joji", year=2017, score=86.33, personal=8.4, mean=8.87, leng="24:23", rec="EYSSSSS", review_date="11/4/2022", genre=Genre.soul, stats=[], songs=[]),
                Album(id=37, title="A Head Full Of Dreams", artist="Coldplay", year=2015, score=82.45, personal=8.0, mean=8.49, leng="45:50", rec="YESSS", review_date="11/10/2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=38, title="DR4L", artist="Juice WRLD", year=2020, score=87.70, personal=8.9, mean=8.64, leng="1:15:00", rec="YES", review_date="12/9/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=39, title="Punk", artist="Young Thug", year=2021, score=66.35, personal=6.4, mean=6.87, leng="1:03:00", rec="Ehhhh", review_date="12/9/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=40, title="÷ (DELUXE)", artist="Ed Sheeran", year=2017, score=90.19, personal=9.0, mean=9.04, leng="59:33", rec="YESSSSSSSSS", review_date="12/10/2022", genre=Genre.pop, stats=[], songs=[]),
                Album(id=41, title="x (DELUXE)", artist="Ed Sheeran", year=2014, score=85.44, personal=8.3, mean=8.79, leng="1:05:00", rec="Yes", review_date="12/10/2022", genre=Genre.rnb, stats=[], songs=[]),
                Album(id=42, title="Her Loss", artist="Drake & 21 Savage", year=2022, score=81.53, personal=7.8, mean=8.51, leng="1:00:00", rec="Eh Yeah", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=43, title="Yeezus", artist="Kanye West", year=2013, score=77.05, personal=7.2, mean=8.21, leng="1:08:00", rec="Look at the notable songs", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=44, title="channel ORANGE", artist="Frank Ocean", year=2012, score=86.24, personal=8.9, mean=8.35, leng="55:47", rec="ye", review_date="12/10/2022", genre=Genre.rnb, stats=[], songs=[]),
                Album(id=45, title="Best Day Ever", artist="Mac Miller", year=2010, score=83.22, personal=8.2, mean=8.44, leng="51:24", rec="Yeah", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=46, title="HEROES & VILLIANS", artist="Metro Boomin", year=2022, score=84.60, personal=8.3, mean=8.62, leng="48:04", rec="YESSS", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=47, title="Graduation", artist="Kanye West", year=2007, score=91.68, personal=9.4, mean=8.94, leng="54:29", rec="ABSOLUTELY", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=48, title="Its Almost Dry", artist="Pusha T", year=2022, score=82.67, personal=8.0, mean=8.53, leng="35:53", rec="Yeah", review_date="12/10/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=49, title="MBDTF", artist="Kanye West", year=2010, score=89.19, personal=9.0, mean=8.84, leng="1:08:00", rec="YESS", review_date="12/11/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=50, title="Good Job", artist="Cookin Soul", year=2020, score=81.30, personal=8.0, mean=8.26, leng="24:15", rec="If you wanna spice up your playlist", review_date="12/20/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=51, title="JESUS IS KING", artist="Kanye West", year=2019, score=72.14, personal=6.5, mean=7.93, leng="27:04", rec="Ehhhh", review_date="12/30/2022", genre=Genre.rap, stats=[], songs=[]),
                Album(id=52, title="Cheers to the Best Memories", artist="dvsn & TD$", year=2023, score=80.50, personal=8.0, mean=8.10, leng="32:18", rec="Ehhhh", review_date="1/20/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=53, title="MANSION MUSIK", artist="Trippie Redd", year=2023, score=63.40, personal=5.0, mean=7.68, leng="1:16:00", rec="the first 5 songs, and colors", review_date="1/20/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=54, title="Starboy", artist="The Weeknd", year=2016, score=90.39, personal=9.2, mean=8.88, leng="1:08:00", rec="Absolutely", review_date="1/24/2023", genre=Genre.pop, stats=[], songs=[]),
                Album(id=55, title="Like..?", artist="Ice Spice", year=2023, score=47.25, personal=3.0, mean=6.45, leng="13:08", rec="Do not and I MEAN DO NOT LISTEN TO THIS", review_date="1/26/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=56, title="Let's Start Here.", artist="Lil Yachty", year=2023, score=88.68, personal=9.0, mean=8.74, leng="57:16", rec="Yes", review_date="1/28/2023", genre=Genre.psychedelic, stats=[], songs=[]),
                Album(id=57, title="i am > i was", artist="21 Savage", year=2018, score=83.53, personal=8.0, mean=8.71, leng="51:05", rec="Yes", review_date="1/30/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=58, title="Meet The Woo", artist="Pop Smoke", year=2019, score=72.22, personal=7.3, mean=8.14, leng="34:13", rec="Ehhhh", review_date="7/27/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=59, title="MOTM", artist="Kid Cudi", year=2009, score=89.33, personal=9.0, mean=8.87, leng="58:33", rec="Yes", review_date="7/27/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=60, title="Whole Lotta Red", artist="Playboi Carti", year=2020, score=77.63, personal=7.3, mean=8.23, leng="56:33", rec="no...", review_date="7/29/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=61, title="UTOPIA", artist="Travis Scott", year=2023, score=87.18, personal=8.7, mean=8.74, leng="56:33", rec="Yes", review_date="7/28/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=62, title="Austin", artist="Post Malone", year=2023, score=87.10, personal=0.0, mean=0.00, leng="56:33", rec="Not yet", review_date="9/3/2023", genre=Genre.pop, stats=[], songs=[]),
                Album(id=63, title="SpiderMan: Across the Spider-Verse", artist="Metro Boomin", year=2023, score=85.22, personal=8.5, mean=8.54, leng="56:33", rec="Yes", review_date="9/1/2023", genre=Genre.hip_hop, stats=[], songs=[]),
                Album(id=64, title="Flower Boy", artist="Tyler, The Creator", year=2017, score=87.42, personal=8.7, mean=8.77, leng="56:33", rec="Yes", review_date="8/29/2023", genre=Genre.rap, stats=[], songs=[]),
                Album(id=65, title="Moon Music", artist="Coldplay", year=2024, score=75.10, personal=7.0, mean=8.02, leng="56:33", rec="Ehhh", review_date="10/25/2024", genre=Genre.pop, stats=[], songs=[]),
                Album(id=66, title="GNX", artist="Kendrick Lamar", year=2024, score=90.63, personal=9.0, mean=9.13, leng="56:33", rec="Yes", review_date="11/22/2024", genre=Genre.rap, stats=[], songs=[]),
                Album(id=67, title="CHROMAKOPIA", artist="Tyler, The Creator", year=2024, score=87.32, personal=8.7, mean=8.76, leng="56:33", rec="Yes", review_date="10/28/2024", genre=Genre.rap, stats=[], songs=[]),
                Album(id=68, title="Unorthodox Jukebox", artist="Bruno Mars", year=2012, score=93.90, personal=9.6, mean=9.18, leng="56:33", rec="Yes", review_date="6/3/2025", genre=Genre.pop, stats=[], songs=[]),
                Album(id=69, title="Random Access Memories", artist="Daft Punk", year=2013, score=90.50, personal=9.2, mean=8.90, leng="56:33", rec="Yes", review_date="6/3/2025", genre=Genre.edm, stats=[], songs=[]),
                Album(id=70, title="The Stranger", artist="Billy Joel", year=1977, score=95.17, personal=9.6, mean=9.43, leng="56:33", rec="F*CKING YES!", review_date="10/21/2025", genre=Genre.pop, stats=[], songs=[]),
            ]

            for album in albums:
                db_album = AlbumDB(
                    id=album.id,
                    title=album.title,
                    artist=album.artist,
                    year=album.year,
                    score=album.score,
                    personal=album.personal,
                    mean=album.mean,
                    leng=album.leng,
                    rec=album.rec,
                    review_date=album.review_date,
                    genre=album.genre.value
                )
                db.merge(db_album)
            db.commit()
            
            # compute and store stats if table empty
            if existing_stats is None:
                # create map of song ranks
                all_songs = db.query(SongDB).order_by(SongDB.score.desc()).all()
                song_rank_map = {s.id: idx for idx, s in enumerate(all_songs, start=1)}
                # overall album ranking by score
                all_albums_list = db.query(AlbumDB).order_by(AlbumDB.score.desc()).all()
                for idx, alb in enumerate(all_albums_list, start=1):
                    year_list = db.query(AlbumDB).filter(AlbumDB.year == alb.year).order_by(AlbumDB.score.desc()).all()
                    rank_year = next((i for i,a in enumerate(year_list, start=1) if a.id == alb.id), 0)
                    genre_list = db.query(AlbumDB).filter(AlbumDB.genre == alb.genre).order_by(AlbumDB.score.desc()).all()
                    rank_genre = next((i for i,a in enumerate(genre_list, start=1) if a.id == alb.id), 0)
                    album_songs = db.query(SongDB).filter(SongDB.album_id == alb.id).all()
                    if album_songs:
                        highest_song_rank = min(song_rank_map[s.id] for s in album_songs)
                    else:
                        highest_song_rank = 0
                    stats_entry = StatsDB(
                        album_id=alb.id,
                        album_rank=idx,
                        highest_song_rank=highest_song_rank,
                        rank_in_year=rank_year,
                        rank_in_genre=rank_genre
                    )
                    db.add(stats_entry)
                db.commit()
        
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/album/{album_id}", response_model=Album)
def query_album_by_id(album_id: int, db: Session = Depends(get_db)) -> Album:
    album = db.query(AlbumDB).filter(AlbumDB.id == album_id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album
