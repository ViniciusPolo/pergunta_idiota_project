import joblib
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dados de exemplo (treinamento)
corpus = [
    "Promoção imperdível! Compre agora e ganhe 50% de desconto!",
    "Oferta exclusiva para você, não perca essa chance!",
    "Olá, como você está? Precisamos conversar sobre o projeto.",
    "O relatório da reunião de hoje está pronto, veja no anexo.",
    "Ganhe dinheiro fácil! Trabalhe de casa e lucre muito!"
]
labels = [1, 1, 0, 0, 1]  # 1 = Spam, 0 = Não Spam

# Criando o vetorizador
vectorizer = HashingVectorizer(n_features=16)

# Transformando os textos
X_train_vectorized = vectorizer.fit_transform(corpus)

# Treinando o modelo
modelo = MultinomialNB()
modelo.fit(X_train_vectorized, labels)

# Salvando o modelo e o vetorizar
joblib.dump(modelo, "modelo_spam.pkl")
joblib.dump(vectorizer, "vetorizador.pkl")

print("Modelo e vetorizador salvos com sucesso!")
