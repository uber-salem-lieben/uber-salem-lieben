import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

# Descargar solo las stopwords una vez para evitar múltiples descargas
nltk.download('punkt')

# Cargar las stopwords en inglés
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Preprocesa el texto: tokenización y eliminación de stopwords."""
    tokens = word_tokenize(text)  # Tokeniza el texto en palabras
    tokens = [token for token in tokens if token.isalpha()]  # Elimina puntuación
    tokens = [token for token in tokens if token.lower() not in stop_words]  # Elimina stopwords
    return ' '.join(tokens)  # Devuelve el texto procesado

def create_nlp_pipeline():
    """Crea el pipeline de NLP con spaCy."""
    nlp = spacy.load('en_core_web_sm')  # Carga el modelo de spaCy para procesamiento
    return nlp

nlp = create_nlp_pipeline()  # Inicializa el pipeline de NLP

# Ejemplo de uso del pipeline
sample_text = "The quick brown fox jumped over the lazy dog!"
processed_text = preprocess_text(sample_text)
doc = nlp(processed_text)

print(f"Texto original: {sample_text}")
print(f"Texto procesado: {processed_text}")

