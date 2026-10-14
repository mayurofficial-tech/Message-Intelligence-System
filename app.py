import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR= Path().cwd()
MODEL_DIR = BASE_DIR/'model'

st.set_page_config(
    page_title="Message Spam Intelligence",
    page_icon="📩",
    layout="centered"
)

@st.cache_resource
def load_models():
    return {
        "KNN":joblib.load(MODEL_DIR/"best_knn.pkl"),
        "SVC":joblib.load(MODEL_DIR/"best_svm.pkl"),
        "NB":joblib.load(MODEL_DIR/"best_nb.pkl")
    }

models = load_models()

FEATURES = [
    "message_length",
    "word_count",
    "num_urls",
    "num_digits",
    "num_special_chars",
    "spam_keyword_score",
    "legit_keyword_score",
    "sender_activity_score",
    "sender_account_age_days",
    "messages_sent_last_24h",
    "hour_of_day",
    "day_of_week"
]

st.title("📩 Message Spam Intelligence")
st.write("Enter message and sender features to detect Spam or Ham.")

st.sidebar.header("Model Settings")

model_name = st.sidebar.selectbox(
    "Choose Classifier",
    list(models.keys())
)

st.subheader("Message Features")

with st.form("spam_form"):

    col1, col2 = st.columns(2)

    with col1:
        message_length = st.number_input(
            "Message Length", min_value=0, value=100
        )
        word_count = st.number_input(
            "Word Count", min_value=0, value=20
        )
        num_urls = st.number_input(
            "Number of URLs", min_value=0, value=0
        )
        num_digits = st.number_input(
            "Number of Digits", min_value=0, value=0
        )
        num_special_chars = st.number_input(
            "Special Characters", min_value=0, value=2
        )
        spam_keyword_score = st.number_input(
            "Spam Keyword Score", min_value=0.0, value=0.0
        )

    with col2:
        legit_keyword_score = st.number_input(
            "Legitimate Keyword Score", min_value=0.0, value=0.0
        )
        sender_activity_score = st.number_input(
            "Sender Activity Score", min_value=0.0, value=0.5
        )
        sender_account_age_days = st.number_input(
            "Sender Account Age (days)", min_value=0, value=365
        )
        messages_sent_last_24h = st.number_input(
            "Messages Sent Last 24 Hours", min_value=0, value=5
        )
        hour_of_day = st.number_input(
            "Hour of Day (0-23)", min_value=0, max_value=23, value=12
        )
        day_of_week = st.number_input(
            "Day of Week (0-6)", min_value=0, max_value=6, value=2
        )

    submitted = st.form_submit_button("Analyze Message")

if submitted:

    input_data = pd.DataFrame([{
        "message_length": message_length,
        "word_count": word_count,
        "num_urls": num_urls,
        "num_digits": num_digits,
        "num_special_chars": num_special_chars,
        "spam_keyword_score": spam_keyword_score,
        "legit_keyword_score": legit_keyword_score,
        "sender_activity_score": sender_activity_score,
        "sender_account_age_days": sender_account_age_days,
        "messages_sent_last_24h": messages_sent_last_24h,
        "hour_of_day": hour_of_day,
        "day_of_week": day_of_week
    }], columns=FEATURES)

    model = models[model_name]
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Ham (Not Spam)")

    st.caption(f"Selected model: {model_name}")
