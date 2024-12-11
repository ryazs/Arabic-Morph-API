import joblib
import numpy as np
import tensorflow as tf
from core.config import settings
from models.prediction import PredictionResponse
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from typing import Dict
import pickle

# Memuat tokenizer
try:
    with open('utils/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    print("Tokenizer loaded successfully")
except Exception as e:
    raise RuntimeError(f"Failed to load tokenizer: {str(e)}")


with open('utils/label_encoders.pickle', 'rb') as f:
    label_encoders = pickle.load(f)
    for class_name, encoder in label_encoders.items():
        print(f"Classes for {class_name}:", encoder.classes_)



try:
    # Muat model
    loaded_model = tf.keras.models.load_model(settings.MODEL_PATH)
    print(f"Model loaded successfully with input shape: {loaded_model.input_shape}")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {str(e)}")

try:
    # Muat tokenizer
    tokenizer = joblib.load(settings.VECTORIZER_PATH)
    print(f"Tokenizer loaded successfully: {type(tokenizer)}")
except Exception as e:
    raise RuntimeError(f"Failed to load tokenizer: {str(e)}")

# Panjang input yang diharapkan oleh model
expected_input_length = loaded_model.input_shape[1]

def predict_text(input_text: str) -> PredictionResponse:
    # Ubah teks menjadi sequence angka
    tokenized_text = tokenizer.texts_to_sequences([input_text])

    # Lakukan padding sequence agar sesuai dengan panjang input model
    padded_text = pad_sequences(tokenized_text, maxlen=expected_input_length)

    # Prediksi menggunakan model
    prediction = loaded_model.predict(padded_text)
    label = "jamid" if prediction[0][0] >= 0.5 else "musytaq"

    return PredictionResponse(text=input_text, prediction=label)

# Memuat model kedua
try:
    arabic_verb_model = tf.keras.models.load_model(settings.ARABIC_VERB_MODEL_PATH)
    print("Arabic verb model loaded successfully")
except Exception as e:
    raise RuntimeError(f"Failed to load Arabic verb model: {str(e)}")

def predict_arabic_verb(input_word: str) -> Dict[str, float]:
    try:
        # Preprocessing input dengan tokenizer yang dimuat
        test_sequence = tokenizer.texts_to_sequences([input_word])
        if not test_sequence or not test_sequence[0]:
            raise ValueError(f"Input word '{input_word}' tidak dikenali oleh tokenizer")

        # Padding sequence sesuai dengan panjang input yang diharapkan oleh model
        padded_sequence = pad_sequences(test_sequence, maxlen=expected_input_length, padding='post')

        # Prediksi menggunakan model
        predictions = arabic_verb_model.predict(padded_sequence)

        # Proses hasil prediksi untuk tiga kelas
        output_classes = ["Madhi", "Mudhari", "Amar"]
        decoded_results = {}

        for i, class_name in enumerate(output_classes):
            # Ambil prediksi untuk kelas tertentu
            predicted_index = np.argmax(predictions[i], axis=-1)
            decoded_results[class_name] = label_encoders[class_name].inverse_transform([predicted_index[0]])[0]

        return decoded_results

    except Exception as e:
        raise RuntimeError(f"Prediction failed: {str(e)}")






