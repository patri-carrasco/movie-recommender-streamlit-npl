
import pandas as pd

def user_input_features(title, df):

    film = df.loc[df['original_title']== title]
    data = {'original_title': film.original_title,
            'year': film.year,
            'genre': film.genre,
            'director': film.director,
            'avg_vote':film.avg_vote,
            'votes':film.votes
            }
    features = pd.DataFrame(data)
    
    return features