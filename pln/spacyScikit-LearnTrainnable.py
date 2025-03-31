import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import json

nlp = spacy.load("pt_core_news_sm")

dataBase = 'base_pergunta_idiota.json'

# Open and read the JSON file
with open(dataBase, 'r') as file:
    data = json.load(file)

perguntas_respostas = (data)

def responder(pergunta):
    perguntas = list(perguntas_respostas.keys())
    respostas = list(perguntas_respostas.values())

    vectorizer = TfidfVectorizer()
    matriz = vectorizer.fit_transform(perguntas + [pergunta])
    
    similaridades = cosine_similarity(matriz[-1], matriz[:-1])
    indice_mais_similar = similaridades.argmax()

    return respostas[indice_mais_similar]

# Teste
while True:
    user_input = input("Você: ")
    print("Chatbot:", responder(user_input))

