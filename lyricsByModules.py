from PyLyrics import *
import speech_recognition as sr
from tkinter import *
from lyrics_extractor import SongLyrics 
import datetime


MyA="-"
Myproj="-"
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

a=r.recognize_google(audio, language="en-us")+"."

a=a.lower()
a=a.replace("play ","")
a=a.replace(" by ","$")
start_artist = a.find('$') + 1
artist_end= a.find('.')
artist=a[start_artist:artist_end]
song=a[:start_artist-1]
song=song.title()
artist=artist.title()
datenow = datetime.datetime.now().strftime("%X").replace(":","_")
datenow =datenow +(chr(int("10"+datenow[3])))
extract_lyrics = SongLyrics(MyA,Myproj)
print("ok your Lyrics for "+song+" by "+artist+" have been saved succesfully")
lyrics=extract_lyrics.get_lyrics(song)
res = lyrics['lyrics']
