# 📩 Message Intelligence System

> **🎥 Project Video:** `PASTE_YOUR_GOOGLE_DRIVE_OR_UNLISTED_YOUTUBE_LINK_HERE`  
> **🚀 Live Streamlit App:** `https://message-intelligence-system-by-master.streamlit.app`

A machine-learning application that classifies message-related numerical features as **Spam (1)** or **Ham / Legitimate (0)**. The Streamlit interface lets users choose between K-Nearest Neighbors (KNN), Support Vector Classifier (SVC), and Naive Bayes (NB).

## 📌 Project Overview

The goal is to compare distance-based, margin-based, and probabilistic classification approaches for message spam detection.

### Models
- **KNN** — predicts using nearby training examples.
- **SVC (SVM)** — separates classes using a decision boundary.
- **Gaussian Naive Bayes** — predicts using class probabilities and the Naive Bayes assumption.

### Input Features

The app accepts these 12 numerical features:

1. `message_length`
2. `word_count`
3. `num_urls`
4. `num_digits`
5. `num_special_chars`
6. `spam_keyword_score`
7. `legit_keyword_score`
8. `sender_activity_score`
9. `sender_account_age_days`
10. `messages_sent_last_24h`
11. `hour_of_day`
12. `day_of_week`

## ✨ Features

- Select KNN, SVC, or Naive Bayes from the sidebar.
- Enter message and sender-behavior features through a Streamlit form.
- Predict whether the message is Spam or Ham.
- Train and save models using a Jupyter Notebook.
- Evaluate classifiers with metrics such as accuracy, precision, recall, and F1-score.

## 🗂️ Project Structure

```text
Message-Intelligence-System/
├── app(2).py
├── training.ipynb
├── requirements.txt
└── model/
    ├── best_knn.pkl
    ├── best_svm.pkl
    └── best_nb.pkl
```

Keep the saved model filenames and the paths in the app consistent. The model files must be available in the `model/` directory before launching the app.

## ⚙️ Installation and Setup

### 1. Clone your repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create and activate a virtual environment (recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Check project files

Make sure the `model/` folder contains:

- `best_knn.pkl`
- `best_svm.pkl`
- `best_nb.pkl`

The Streamlit app loads these files when it starts.

### 5. Run the app

Run the command from the project root, where the `model/` folder is located:

```bash
streamlit run "app(2).py"
```

Streamlit will display a local URL in the terminal, usually `http://localhost:8501`.

## 🧪 Training Notebook

Open `training.ipynb` in Jupyter Notebook or VS Code and run the cells in order to prepare data, train and evaluate the classifiers, and save the model files. Update dataset paths in the notebook to match your local setup.

## 📊 Evaluation

Compare the models using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix (if generated in the notebook)

For a spam detector, review precision and recall alongside accuracy: false positives can hide legitimate messages, while false negatives can allow spam through.

## 🛠️ Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## ⚠️ Notes

- The app expects the 12 feature values in the same order and format used during model training.
- Use the same preprocessing steps during training and prediction. If preprocessing is part of a saved scikit-learn pipeline, save and load the complete pipeline.
- Do not commit private data or secrets to the public repository.
- Replace the two link placeholders at the top with your actual video and deployed app URLs before publishing.

## 👤 Author

**Mayur Makwana**

GitHub: https://github.com/mayurofficial-tech
