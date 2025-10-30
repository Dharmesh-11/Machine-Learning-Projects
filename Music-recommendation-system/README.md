# Music Recommender System 🎵

A Flask-based music recommendation system that suggests similar tracks based on your song selection. Built with Python, scikit-learn, and a modern responsive UI.


## Features ✨

- **Instant Recommendations**: Select any song from our curated list and get tailored music recommendations
- **Modern UI**: Clean, responsive interface with gradient accents and smooth animations
- **Smart Selection**: Easy-to-use dropdown with a comprehensive song database
- **Visual Cards**: Each recommendation displayed in an attractive card layout
- **Mobile-Friendly**: Works seamlessly on all devices and screen sizes

## Tech Stack 🛠

- Python 3.11+
- Flask 3.1.2
- NumPy & Pandas for data processing
- scikit-learn for recommendation engine
- Bootstrap 5 for responsive design
- Custom CSS with modern gradients and animations

## Setup 🚀


1. Clone the repository:
```bash
git clone https://github.com/Dharmesh-11/beginner-projects.git
cd Music-Recomdation-system
```

2. Download the dataset:
   - Dataset: [Million Song Dataset (Kaggle)](https://www.kaggle.com/datasets/mathieuteissier/million-song-dataset)
   - Download and rename the dataset file to `songdata.csv`
   - Place the downloaded `songdata.csv` file in the project root directory

3. Set up Python virtual environment:
```bash
python -m venv ml
.\ml\Scripts\Activate.ps1  # On Windows PowerShell
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Running the App 🎯

1. Activate the virtual environment (if not already activated):
```bash
.\ml\Scripts\Activate.ps1  # On Windows PowerShell
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## Usage 📝

1. When the app loads, you'll see a clean interface with a song selection dropdown
2. Choose any song from the dropdown menu
3. Click "Get Recommendations" to see similar tracks
4. Browse through the recommended songs displayed in cards below

## Project Structure 📁

```
Music-Recomdation-system/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── df.pkl             # Preprocessed song dataset
├── similarity.pkl     # Similarity matrix for recommendations
├── static/            # Static assets (images)
└── templates/         # HTML templates
    └── index.html     # Main UI template
```

## Troubleshooting 🔧

- If you see a NumPy error, ensure you're using the project's virtual environment:
  ```bash
  .\ml\Scripts\python.exe app.py
  ```
- Clear your browser cache (Ctrl+F5) if images don't update
- Make sure all pickle files (df.pkl, similarity.pkl) are in the root directory

## Contributing 🤝

Feel free to open issues or submit pull requests if you have suggestions for improvements!

## License 📄

This project is open source and available under the MIT License.

---
Built with ❤️ by Dharmesh
