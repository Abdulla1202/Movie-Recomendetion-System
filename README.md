# 🎬 CineMatch — AI Movie Recommender System

Tired of scrolling endlessly on Netflix and still not finding what to watch?  
**CineMatch** solves this using Machine Learning by recommending movies similar to your choice.

---

## 🌐 Live Demo

👉 https://cinematch-mocha.vercel.app/  

👉 LinkedIn Project Post:  
https://www.linkedin.com/posts/abdulla-ansari-62910b296_machinelearning-webdevelopment-python-ugcPost-7452818500512944128-71VJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEeQOcEBFlNJZGNY1nwU2TD-gT_TpFFtRuk  

---

## 🚀 Features

- 🔍 Search any movie  
- 🎯 Get top similar recommendations  
- 🖼️ Posters and movie details (via TMDB API)  
- ⚡ Fast performance using precomputed data  
- 🎨 Clean and interactive UI  
- 📊 Autocomplete search  

---

## 🧠 How It Works

- Movies are converted into feature vectors  
- Cosine similarity is used to find similar movies  
- Based on your selection, top recommendations are shown  

💡 **Optimization:**  
Instead of loading heavy ML files, recommendations are precomputed and stored in JSON for faster performance.

---

## ⚙️ Tech Stack

- Python (Pandas, Pickle)  
- Flask (Backend)  
- HTML, CSS, JavaScript (Frontend)  
- TMDB API  
- Vercel (Deployment)  

---

## 📂 Project Structure


├── data/
│ ├── movies.json
│ └── recommendations.json
├── static/
├── templates/
├── app.py
├── backend.py
├── precompute.py
├── vercel.json
└── index.html


---

## 🛠️ Run Locally

```bash
git clone https://github.com/Abdulla1202/Movie-Recomendetion-System.git
cd Movie-Recomendetion-System
pip install -r requirements.txt
python backend.py

Open in browser:
http://localhost:5000
