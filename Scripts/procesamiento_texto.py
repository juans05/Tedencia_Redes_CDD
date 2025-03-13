
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('spanish'))
lemmatizer = WordNetLemmatizer()

def limpiar_y_tokenizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñ# ]", "", texto)
    tokens = word_tokenize(texto, language="spanish")
    tokens = [lemmatizer.lemmatize(palabra) for palabra in tokens if palabra not in stop_words]
    return tokens
