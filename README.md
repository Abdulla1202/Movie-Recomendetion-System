# 🎬 CineMatch — AI Movie Recommender System

Ever spent 20 minutes scrolling Netflix and still couldn’t decide what to watch?  
CineMatch solves this problem using Machine Learning.

---

## 🌐 Live Links

👉 **Live App (Try it now)**: https://cinematch-mocha.vercel.app/  
👉 **LinkedIn Post (Project Showcase)**: https://www.linkedin.com/posts/abdulla-ansari-62910b296_machinelearning-webdevelopment-python-ugcPost-7452818500512944128-71VJ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEeQOcEBFlNJZGNY1nwU2TD-gT_TpFFtRuk  

---

## 🚀 Features

- 🔍 Search any movie  
- 🎯 Get top similar movie recommendations  
- 🖼️ Movie posters & details (via TMDB API)  
- ⚡ Fast performance using precomputed data  
- 🎨 Modern UI with animations  
- 📊 Autocomplete search system  

---

## 🧠 How It Works

This project uses a **content-based filtering** approach:

- Movies are converted into feature vectors  
- A **similarity matrix** is computed using cosine similarity  
- Based on user input, the system finds the most similar movies  

💡 **Optimization Trick:**  
Instead of loading heavy `.pkl` files in production, recommendations are precomputed and stored in JSON — making the app faster and deployment-friendly.

---

## ⚙️ Tech Stack

- **Machine Learning**: Python, Pandas, Pickle  
- **Backend**: Flask  
- **Frontend**: HTML, CSS, JavaScript  
- **API**: TMDB (for posters & movie details)  
- **Deployment**: Vercel  

---

## 📂 Project Structure

