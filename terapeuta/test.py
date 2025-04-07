cd /home/jimsow/Downloads/ubersalemlieben/terapeuta

# Crea y activa un entorno virtual
python3 -m venv myenv
source myenv/bin/activate

# Instala las dependencias desde el archivo requirements.txt
pip install -r terapeuta_requirements.txt

# Descargar el modelo de lenguaje de SpaCy
python -m spacy download en_core_web_sm

# Ejecuta el script
python emotion_classifier.py
