import json
import pickle
import pandas as pd
from flask import Flask, jsonify, request

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.read_pickle('movies.pkl')

app = Flask(__name__)

@app.route('/movie/<movie_title>')
def recommender(movie_title):
    recommendations =  {}
    try:
        index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            recommendations.update({int(movies.iloc[i[0]].id):str(movies.iloc[i[0]].title)})
        return jsonify(recommendations)
    except:
        return jsonify(recommendations) 
        
if __name__ == "__main__":
    app.run()