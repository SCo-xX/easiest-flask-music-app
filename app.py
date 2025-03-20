from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

#List of random songs
data = {
    "title":["Blinding Lights","Shape of You", "Bohemian Rhapsody", "Someone Like You","Uptown Funk"],
    "artist":["The Weeknd", "Ed Sheeran", "Queen", "Adele", "Mark Ronson ft. Bruno Mars"]
}

songs = pd.DataFrame(data)

@app.route("/")
def home():
    song = songs.sample(n=1).iloc[0] #Pick a random song
    return render_template("index.html", song=song)


if __name__=="__main__":
    app.run(debug=True)
