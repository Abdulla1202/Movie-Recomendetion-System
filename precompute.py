"""
Pre-compute all movie recommendations and save as JSON files.
This eliminates the need for the large similarity.pkl on Vercel.
Run this script ONCE locally before deploying.
"""
import pickle
import json
import pandas as pd

print("[*] Loading movie data...")
movies = pickle.load(open('movie_dict_list.pkl', 'rb'))
movies = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))

print(f"[*] Total movies: {len(movies)}")

# 1. Save movie list with IDs
movies_list = []
for idx in range(len(movies)):
    movies_list.append({
        'title': str(movies.iloc[idx].title),
        'movie_id': int(movies.iloc[idx].movie_id)
    })

with open('data/movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies_list, f, ensure_ascii=False)
print(f"[*] Saved data/movies.json ({len(movies_list)} movies)")

# 2. Precompute recommendations for every movie
recommendations = {}
for idx in range(len(movies)):
    title = str(movies.iloc[idx].title)
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    recs = []
    for i in distances[1:11]:  # Top 10 recommendations
        recs.append({
            'title': str(movies.iloc[i[0]].title),
            'movie_id': int(movies.iloc[i[0]].movie_id)
        })
    
    recommendations[title] = recs
    
    if (idx + 1) % 500 == 0:
        print(f"[*] Processed {idx + 1}/{len(movies)} movies...")

with open('data/recommendations.json', 'w', encoding='utf-8') as f:
    json.dump(recommendations, f, ensure_ascii=False)

print(f"[*] Saved data/recommendations.json")
print("[*] Done! You can now deploy to Vercel.")
