import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("pt_core_news_sm")

perguntas_respostas = {
    "Qual é a capital do Brasil?": "A capital do Brasil é Brasília.",
    "Quem descobriu o Brasil?": "Pedro Álvares Cabral descobriu o Brasil em 1500.",
    "Qual é o maior time de futebol do mundo?": "Isso é uma questão de opinião, mas muitos consideram o Real Madrid ou o Flamengo.",
}

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

