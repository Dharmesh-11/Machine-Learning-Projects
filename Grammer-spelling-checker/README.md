# 📝 Grammar and Spell Checker Web App

A simple and interactive **Flask-based web application** that detects and corrects spelling and grammar mistakes using **TextBlob** and **GingerIt2**.  
Built with Python, Flask, Bootstrap, and NLP libraries.

---

## 🚀 Features

- 🧠 **Spell Correction** using TextBlob  
- 🗣️ **Grammar Checking** using GingerIt2  
- 📂 **Supports File Uploads** (`.txt`)  
- 🌐 **Beautiful Web UI** with Bootstrap  
- ⚡ **Fast & Lightweight Flask App**

---

## 🗂️ Project Structure

```
Grammar-Spell-Checker/
│
├── app.py                        # Main Flask app
├── requirements.txt              # Dependencies
│
├── Model/
│   └── SpellCheckerModule.py     # Spell & grammar correction logic
│
└── templates/
    └── index.html                # Frontend template
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Grammar-Spell-Checker.git
cd Grammar-Spell-Checker
```

### 2️⃣ Create Virtual Environment (Optional)
```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate       # On macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

---

## ▶️ Run the App
```bash
python app.py
```

Then open in your browser:  
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧠 How It Works

- The user enters text or uploads a `.txt` file.
- The app uses:
  - **TextBlob** → fixes spelling mistakes.
  - **GingerIt2** → detects grammar issues.
- The corrected output and mistake summary are displayed on the same page.

---

## 🧰 Technologies Used

| Component | Technology |
|------------|-------------|
| Backend | Flask (Python) |
| Frontend | HTML5, CSS3, Bootstrap |
| NLP | TextBlob, GingerIt2 |
| Server | Gunicorn (for deployment) |

---

## 🧑‍💻 Author

**Dharmesh Panpatil** 


### 💡 Tip
If GingerIt2 doesn’t work (due to network or API issues), check your internet connection — it uses online grammar APIs.
