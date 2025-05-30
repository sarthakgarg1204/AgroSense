
# 🌾 CropGenie: AI-Powered Crop & Fertilizer Recommendation System

CropGenie is an intelligent, ML-powered assistant that helps farmers and agricultural advisors make **data-driven decisions** on:

- ✅ The most suitable **crop** for a specific plot of land
- ✅ The best **fertilizer** based on crop and soil type

Built with **Streamlit**, this application provides a user-friendly interface and delivers instant, reliable recommendations.

---

## 🚀 Live Demo

You can access the live deployed version of AgroSense here:
🔗 [https://kropgenie.streamlit.app](https://kropgenie.streamlit.app)

---

## 🚀 Features

- 🌱 **Crop Recommendation** using a trained Decision Tree model
- 💊 **Fertilizer Suggestion** based on crop type and soil condition
- 📊 Clean UI with tabs and sidebar navigation
- ⚙️ Scalable, open-source, and easy to deploy

---

## 🧪 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **ML Model**: Decision Tree Classifier (Scikit-learn)
- **Data Handling**: Pandas, NumPy
- **Deployment**: Streamlit Cloud or localhost

---

## 📁 Folder Structure

```
AgroSense/
├── app.py                       # Streamlit application
├── crop_model.pkl               # Trained ML model
├── crop_scaler.sav              # Feature scaler (StandardScaler)
├── Fertilizer Prediction.csv    # Dataset for fertilizer lookup
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 💻 How to Run Locally

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AgroSense.git
cd AgroSense
```

### 🐍 Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Step 4: Launch the App

```bash
streamlit run app.py
```

The app will open in your browser at:
[http://localhost:8501](http://localhost:8501)

---

## 🌐 How to Deploy

1. Push the project folder to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io) and connect your GitHub repo.
3. Select `app.py` as the entry point.
4. Deploy your app in seconds 🚀

---

## 📊 Datasets Used

- **Crop Dataset**: `Crop_recommendation.csv`
- **Fertilizer Dataset**: `Fertilizer Prediction.csv`

---

## 👥 Team

**CropGenie** is developed by:
- **Sarthak Garg**
- **Team AgroSense** — B.Tech Computer Science (2026)

---

## 📌 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and contribute!

---

## 📬 Contact

Got feedback or want to collaborate?

- 📧 Email: [sarthakgarg1204@gmail.com](mailto:sarthakgarg1204@gmail.com)
- 🌐 GitHub: [github.com/sarthakgarg1204](https://github.com/sarthakgarg1204)
