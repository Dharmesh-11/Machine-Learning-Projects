from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle

# laoding models
df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:21]:
        songs.append(df.iloc[m_id[0]].song)

    return songs


# flask app
app = Flask(__name__)
# paths
@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('index.html',name = names)
@app.route('/recom',methods=['POST'])
def mysong():
    # Use .get to avoid BadRequestKeyError when the field is missing
    user_song = request.form.get('names')
    names = list(df['song'].values)
    if not user_song:
        # no selection made — render the index with a friendly message
        return render_template('index.html', name=names, songs=None, error='Please select a song from the list')

    songs = recommendation(user_song)
    return render_template('index.html', name=names, songs=songs)


# python
if __name__ == "__main__":
    app.run(debug=True)