# -*- coding: utf-8 -*-
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import nltk
from nlp_pipeline import preprocess_text  # Asegúrate de que esto esté al principio del archivo

# Verificar la versión de Python
if sys.version_info < (3, 6):
    print("Este script requiere Python 3.6 o superior.")
    sys.exit(1)

# Descargar stopwords si es necesario
nltk.download('stopwords')

# Cargar el dataset (asegúrate de tener el archivo CSV en la ruta correcta)
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Renombrar las columnas para que coincidan con lo esperado
    data.rename(columns={'text': 'text', 'sentiment': 'emotion'}, inplace=True)
    return data

# Preprocesar los datos
def preprocess_data(data):
    # Tokenización y limpieza de texto
    data['text'] = data['text'].apply(lambda x: preprocess_text(x))
    return data

# Dividir los datos en entrenamiento y prueba
def split_data(data):
    X = data['text']
    y = data['emotion']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Vectorización del texto
def vectorize_text(X_train, X_test):
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_test_vec

# Entrenamiento con RandomForest
def train_random_forest(X_train_vec, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_vec, y_train)
    return model

# Entrenamiento con SVM
def train_svm(X_train_vec, y_train):
    model = SVC(kernel='linear', random_state=42)
    model.fit(X_train_vec, y_train)
    return model

# Predicción en tiempo real
def predict(model, vectorizer, text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return prediction[0]

# Evaluar el modelo
def evaluate_model(model, X_test_vec, y_test):
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: {:.2f}%'.format(accuracy * 100))

# Main function to run the pipeline
def main():
    # Cargar datos
    data = load_data('/home/jimsow/Downloads/ubersalemlieben/terapeuta/data/cleaned_tweet_emotions.csv')  # Ruta al archivo limpio
    data = preprocess_data(data)
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = split_data(data)
    
    # Vectorizar texto
    X_train_vec, X_test_vec = vectorize_text(X_train, X_test)
    
    # Entrenar el modelo (Random Forest o SVM)
    model = train_random_forest(X_train_vec, y_train)  # O usa train_svm para SVM
    
    # Evaluar el modelo
    evaluate_model(model, X_test_vec, y_test)
    
    # Predicción en tiempo real
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit(X_train)  # Ajustar el vectorizador con los datos de entrenamiento
    sample_text = "I'm so happy today!"
    prediction = predict(model, vectorizer, sample_text)
    print("Predicted emotion: {}".format(prediction))

if __name__ == '__main__':
    main()
