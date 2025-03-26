import sys
import json
import random
import spacy
import re
import string
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import urllib.request
import bs4 as bs

# Download necessário para tokenização
nltk.download('punkt')

# Carregar modelo NLP do Spacy
pln = spacy.load('pt_core_news_sm')
stopWords = spacy.lang.pt.stop_words.STOP_WORDS

# Buscar texto de uma página da Wikipedia (exemplo)
conjuntoDados = urllib.request.urlopen("https://pt.wikipedia.org/wiki/Ataques_de_8_de_janeiro_em_Bras%C3%ADlia#:~:text=Os%20ataques%20de%208%20de,bolsonaristas%20extremistas%20que%20invadiu%20edif%C3%ADcios").read()
dadosHTML = bs.BeautifulSoup(conjuntoDados, 'lxml')
dadosTexto = dadosHTML.find_all('p')

# Limpar Tags HTML
dadosSemTags = " ".join([item.text for item in dadosTexto]).lower()

# Tokenizar frases
frasesTokenizadas = sent_tokenize(dadosSemTags)

def preProcessamento(texto):
    texto = re.sub(r'https?://\S+', '', texto)  # Remover URLs
    texto = re.sub(r'\s+', ' ', texto)  # Remover espaços extras
    listaLemas = [palavra.lemma_ for palavra in pln(texto)]
    lista = [palavra for palavra in listaLemas if palavra not in stopWords and palavra not in string.punctuation]
    return ' '.join([str(item) for item in lista if not item.isdigit()])

listaPreProcessada = [preProcessamento(frase) for frase in frasesTokenizadas]

entradaInicialUsuario = ['hey', 'olá', 'bom', 'e aí chat', 'olá tudo bem?', 'opa', 'chat', 'bom dia']
respostaInicial = ['E aí meu caro!', 'Hey', 'Salve meu Compadre', 'E aí, tudo Certo?', 'Olá', 'Olá, como posso ajudar?']

def responderUsuario(texto):
    palavras = texto.lower().split()
    for palavra in palavras:
        if palavra in entradaInicialUsuario:
            return random.choice(respostaInicial)
    return None
    

def respostaChat(textoUsuario):
    listaPreProcessada.append(textoUsuario)
    tfidf = TfidfVectorizer()
    palavrasVetorizadas = tfidf.fit_transform(listaPreProcessada)
    calcSimilaridade = cosine_similarity(palavrasVetorizadas[-1], palavrasVetorizadas)
    indiceFrase = calcSimilaridade.argsort()[0][-2]
    vetorSimilar = calcSimilaridade.flatten()
    vetorSimilar.sort()
    vetorSelecionado = vetorSimilar[-2]

    if vetorSelecionado == 0:
        return "Desculpe, não consegui compreender!"
    else:
        return frasesTokenizadas[indiceFrase]

# Loop para receber mensagens do WebSocket via stdin
if __name__ == "__main__":
    while True:
        try:
            user_input = sys.stdin.readline().strip()
            if not user_input:
                continue
            data = json.loads(user_input)  # Recebe JSON do Node.js
            response = responderUsuario(data["message"]) or respostaChat(preProcessamento(data["message"]))
            print(json.dumps({"response": response}))  # Retorna JSON
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
