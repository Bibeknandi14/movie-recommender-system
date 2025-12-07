🎬 Movie Recommender System

A Streamlit-based movie recommendation app that suggests the top 5 similar movies using cosine similarity and preprocessed metadata. The system is fast, lightweight, and works entirely offline.

🚀 Features

✅ Content-based recommendations using cosine similarity
🎥 Top 5 similar movie suggestions
🖼️ Poster display using dataset metadata
⚡ Instant results (precomputed similarity)
📦 100% offline — no external APIs needed
🌐 Ready for Streamlit Cloud deployment

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Bibeknandi14/movie-recommender-system.git
cd movie-recommender-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

🧠 How It Works

User selects a movie from the dropdown

System finds its index in the dataset

Cosine similarity scores are computed from a preprocessed matrix

Top 5 closest movies are selected

Titles + Posters are displayed in columns

📂 Project Structure
movie-recommender-system/
│── app.py                # Streamlit App
│── movie_dict.pkl        # Titles + IDs
│── movies.pkl            # Movie DataFrame
│── movies_metadata.pkl   # Poster links
│── similarity.pkl        # Cosine similarity matrix
│── requirements.txt      # Dependencies
│── Procfile              # Deployment config
│── setup.sh              # Streamlit Cloud setup
└── README.md

🔮 Future Improvements

⭐ Add TMDB API for real-time posters
⭐ Add genre filtering
⭐ Add movie description & rating display
⭐ Add autocomplete search
⭐ Add collaborative filtering (hybrid model)

🤝 Contributing

Pull requests are welcome.
Feel free to open issues for new ideas or bugs.

📜 License

MIT License — free for personal and academic use.
