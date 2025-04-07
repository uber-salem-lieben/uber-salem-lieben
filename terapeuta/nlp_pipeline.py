import spacy
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)  # Descargar stopwords silenciosamente

def create_nlp_pipeline():
    nlp = spacy.load('en_core_web_sm')
    return nlp

def preprocess_text(text):
    """
    Preprocesa el texto para limpieza y normalización.
    """
    if not isinstance(text, str):
        return ""  # Manejar casos donde la entrada no es una cadena

    # Convertir a minúsculas
    text = text.lower()
    # Eliminar URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Eliminar menciones y hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Eliminar caracteres especiales y números
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenización
    tokens = text.split()
    # Eliminar stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Unir tokens de nuevo en una cadena
    return " ".join(tokens)
