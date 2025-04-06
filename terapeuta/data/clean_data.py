# -*- coding: utf-8 -*-
import pandas as pd
import re
import emoji

# Cargar el archivo CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Limpiar el texto: eliminar emojis, caracteres especiales y normalizar el texto
def clean_text(text):
    # Eliminar emojis
    text = emoji.replace_emoji(text, replace='')
    # Eliminar caracteres especiales y números
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convertir todo a minúsculas
    text = text.lower()
    return text

# Limpiar los datos
def clean_data(data):
    # Aplicar la limpieza de texto
    data['text'] = data['content'].apply(lambda x: clean_text(x))
    return data

# Guardar el archivo limpio
def save_clean_data(data, output_path):
    data.to_csv(output_path, index=False)

# Función principal
def main():
    # Ruta al CSV original
    input_path = 'terapeuta/data/tweet_emotions.csv'
    output_path = 'terapeuta/data/cleaned_tweet_emotions.csv'
    
    # Cargar y limpiar los datos
    data = load_data(input_path)
    cleaned_data = clean_data(data)
    
    # Guardar los datos limpios
    save_clean_data(cleaned_data, output_path)
    print(f'Datos limpios guardados en {output_path}')

if __name__ == '__main__':
    main()
