import pickle
import requests
import pandas as pd
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Load data
movies = pickle.load(open('movie_dict_list.pkl', 'rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=5)
        data = data.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return ""
    except:
        return ""

def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url, timeout=5).json()
        return {
            'overview': data.get('overview', 'No overview available.'),
            'release_date': data.get('release_date', 'N/A'),
            'vote_average': data.get('vote_average', 0),
            'runtime': data.get('runtime', 0),
            'genres': [g['name'] for g in data.get('genres', [])],
            'tagline': data.get('tagline', ''),
        }
    except:
        return {
            'overview': 'No overview available.',
            'release_date': 'N/A',
            'vote_average': 0,
            'runtime': 0,
            'genres': [],
            'tagline': '',
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    """Return list of all movie titles for the dropdown"""
    movie_list = movies['title'].tolist()
    return jsonify(movie_list)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    """Get recommendations for a selected movie"""
    data = request.get_json()
    movie_name = data.get('movie', '')
    
    if movie_name not in movies['title'].values:
        return jsonify({'error': 'Movie not found'}), 404
    
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in distances[1:11]:  # Get top 10 recommendations
        movie_id = int(movies.iloc[i[0]].movie_id)
        title = str(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        details = fetch_movie_details(movie_id)
        
        recommendations.append({
            'title': title,
            'poster': poster,
            'movie_id': movie_id,
            'overview': details['overview'],
            'release_date': details['release_date'],
            'vote_average': float(details['vote_average']) if details['vote_average'] else 0,
            'runtime': int(details['runtime']) if details['runtime'] else 0,
            'genres': details['genres'],
            'tagline': details['tagline'],
        })
    
    return jsonify(recommendations)

@app.route('/api/trending')
def trending():
    """Return popular movies with small poster URLs for the homepage background"""
    import random
    sample_indices = random.sample(range(len(movies)), min(40, len(movies)))
    trending_movies = []
    for idx in sample_indices:
        movie_id = int(movies.iloc[idx].movie_id)
        title = str(movies.iloc[idx].title)
        # Use w200 for background thumbnails (faster loading)
        try:
            url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
            data = requests.get(url, timeout=3).json()
            poster_path = data.get('poster_path', '')
            if poster_path:
                poster = f"https://image.tmdb.org/t/p/w200/{poster_path}"
                trending_movies.append({
                    'title': title,
                    'poster': poster,
                    'movie_id': movie_id
                })
        except:
            continue
    return jsonify(trending_movies)

if __name__ == '__main__':
    print("[*] Movie Recommender System by Abdulla Ansari")
    print("[*] Server starting at http://localhost:5000")
    app.run(debug=True, port=5000)
