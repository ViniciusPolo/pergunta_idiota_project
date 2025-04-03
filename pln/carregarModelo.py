# Carregando o modelo treinado
modelo = joblib.load("modelo_spam.pkl")
vectorizer = joblib.load("vetorizador.pkl")

# Novo texto para classificação
novo_texto = ["Ganhe dinheiro rápido e fácil trabalhando de casa!"]

# Transformando o novo texto com o mesmo vetorizar
X_novo = vectorizer.transform(novo_texto)

# Fazendo a predição
resultado = modelo.predict(X_novo)

# Exibindo o resultado
print("É SPAM" if resultado[0] == 1 else "NÃO É SPAM")
