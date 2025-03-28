import torch
import torch.nn as nn
import torch.optim as optim
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

# Dados de treinamento
treinamento = [
    {"input": "Oi, tudo bem?", "output": "Olá! Como posso te ajudar?"},
    {"input": "Qual é o seu nome?", "output": "Sou um chatbot treinado para responder suas perguntas!"},
    {"input": "O que você faz?", "output": "Eu respondo perguntas e ajudo no que puder!"},
    # Saudações
    {"input": "Oi!", "output": "Olá! Como posso te ajudar?"},
    {"input": "Bom dia!", "output": "Bom dia! Como você está?"},
    {"input": "Boa tarde!", "output": "Boa tarde! Em que posso ajudar?"},
    {"input": "Boa noite!", "output": "Boa noite! O que deseja saber?"},
    {"input": "Tudo bem?", "output": "Estou bem, obrigado por perguntar! E você?"},
    {"input": "Como você está?", "output": "Estou sempre pronto para ajudar!"},
    
    # Informações sobre o chatbot
    {"input": "Qual é o seu nome?", "output": "Sou um chatbot treinado para responder suas perguntas!"},
    {"input": "O que você faz?", "output": "Eu respondo perguntas e ajudo no que puder!"},
    {"input": "Você é humano?", "output": "Não, sou um assistente virtual baseado em inteligência artificial."},
    {"input": "Você aprende sozinho?", "output": "Ainda não, mas posso ser atualizado com novos conhecimentos!"},

    # Tecnologia
    {"input": "O que é inteligência artificial?", "output": "É um campo da computação que simula a inteligência humana em máquinas."},
    {"input": "O que é um algoritmo?", "output": "Um conjunto de instruções para resolver um problema ou realizar uma tarefa."},
    {"input": "O que é machine learning?", "output": "É um ramo da IA que ensina computadores a aprenderem com dados."},
    {"input": "Qual a melhor linguagem de programação?", "output": "Depende do uso! Python é ótimo para IA, enquanto JavaScript é excelente para web."},
    {"input": "O que é um banco de dados?", "output": "É um sistema que armazena e organiza informações de forma estruturada."},
    {"input": "O que significa HTML?", "output": "HyperText Markup Language, a linguagem de marcação para páginas web."},
    
    # Esportes
    {"input": "Quem é o melhor jogador de futebol?", "output": "Isso é subjetivo, mas alguns dos maiores são Pelé, Maradona, Messi e Cristiano Ronaldo."},
    {"input": "Quantos jogadores tem um time de futebol?", "output": "Um time de futebol tem 11 jogadores em campo."},
    {"input": "Quais são as regras do basquete?", "output": "O objetivo é marcar pontos jogando a bola na cesta adversária, seguindo regras como dribles e faltas."},
    {"input": "O que é um Grand Slam no tênis?", "output": "São os quatro principais torneios de tênis: Australian Open, Roland Garros, Wimbledon e US Open."},
    
    # Entretenimento
    {"input": "Qual é o filme mais famoso de todos os tempos?", "output": "Alguns dos mais famosos são O Poderoso Chefão, Titanic e Star Wars."},
    {"input": "Quem criou a Marvel?", "output": "A Marvel foi fundada por Martin Goodman e teve Stan Lee como um dos principais criadores."},
    {"input": "Qual é a série mais assistida da Netflix?", "output": "Entre as mais assistidas estão Stranger Things, La Casa de Papel e Round 6."},
    {"input": "Quem é o autor de Harry Potter?", "output": "J.K. Rowling."},
    
    # Educação
    {"input": "O que é a tabela periódica?", "output": "É uma tabela que organiza todos os elementos químicos conhecidos."},
    {"input": "Quem descobriu a gravidade?", "output": "Isaac Newton."},
    {"input": "Quantos planetas existem no sistema solar?", "output": "Oito planetas: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno."},
    {"input": "O que é uma fração?", "output": "Uma fração representa uma parte de um todo, como 1/2 ou 3/4."},
    
    # Saúde
    {"input": "Como ter uma alimentação saudável?", "output": "Comer frutas, legumes, proteínas e evitar alimentos processados."},
    {"input": "Quantos litros de água devo beber por dia?", "output": "Recomenda-se cerca de 2 litros por dia para um adulto."},
    {"input": "O que é colesterol?", "output": "É uma substância gordurosa essencial para o corpo, mas em excesso pode ser prejudicial."},
    {"input": "O que é hipertensão?", "output": "É a pressão arterial elevada, que pode aumentar o risco de doenças cardíacas."},
    
    # Curiosidades
    {"input": "Quem foi Albert Einstein?", "output": "Um físico famoso pela teoria da relatividade."},
    {"input": "Qual é o maior animal do mundo?", "output": "A baleia-azul."},
    {"input": "Qual é o menor país do mundo?", "output": "O Vaticano."},
    {"input": "O que é o Monte Everest?", "output": "A montanha mais alta do mundo, com 8.848 metros de altura."},

    # Clima e Natureza
    {"input": "Por que chove?", "output": "A chuva ocorre quando o vapor d'água se condensa e cai em forma de gotas."},
    {"input": "O que é um furacão?", "output": "É um sistema de tempestades com ventos fortes e chuvas intensas."},
    {"input": "O que é aquecimento global?", "output": "É o aumento da temperatura média do planeta devido à poluição e gases do efeito estufa."},

    # História
    {"input": "Quem foi Napoleão Bonaparte?", "output": "Um general francês que se tornou imperador e conquistou grande parte da Europa."},
    {"input": "O que foi a Revolução Industrial?", "output": "Foi um período de grandes mudanças tecnológicas e econômicas nos séculos XVIII e XIX."},
    {"input": "Quem descobriu o Brasil?", "output": "Pedro Álvares Cabral, em 1500."},
    
    # Matemática
    {"input": "Quanto é 2 + 2?", "output": "2 + 2 é igual a 4."},
    {"input": "O que é um número primo?", "output": "É um número que só pode ser dividido por 1 e por ele mesmo."},
    
    # Programação
    {"input": "O que é um loop em programação?", "output": "É uma estrutura que repete um bloco de código enquanto uma condição for verdadeira."},
    {"input": "O que significa 'bug' em programação?", "output": "É um erro ou falha no código de um programa."},
    
    # Internet e redes sociais
    {"input": "O que significa Wi-Fi?", "output": "É uma tecnologia que permite conexão sem fio à internet."},
    {"input": "O que é um domínio na internet?", "output": "É o nome de um site, como google.com."},
    {"input": "O que é um influencer digital?", "output": "Uma pessoa que influencia outras através das redes sociais."},
    
    # Vida cotidiana
    {"input": "Como economizar dinheiro?", "output": "Crie um orçamento, evite gastos desnecessários e poupe parte do seu salário."},
    {"input": "Como melhorar a produtividade?", "output": "Planeje seu dia, elimine distrações e faça pausas estratégicas."},
    # ⚽ Futebol
    {"input": "Quem é o maior jogador de futebol de todos os tempos?", "output": "Pelé, Maradona, Messi e Cristiano Ronaldo são considerados alguns dos maiores."},
    {"input": "Qual seleção venceu mais Copas do Mundo?", "output": "O Brasil, com 5 títulos."},
    {"input": "Quando foi a primeira Copa do Mundo?", "output": "Em 1930, no Uruguai."},
    {"input": "Quem ganhou a última Copa do Mundo?", "output": "Depende do ano! Me pergunte sobre um ano específico."},
    {"input": "Qual é o maior time do Brasil?", "output": "Isso é subjetivo! Alguns dos maiores são Flamengo, Palmeiras, São Paulo, Corinthians e Santos."},
    {"input": "O que é impedimento no futebol?", "output": "Quando um jogador recebe a bola estando mais próximo do gol adversário do que o penúltimo defensor."},
    {"input": "O que significa hat-trick?", "output": "É quando um jogador marca três gols em uma mesma partida."},
    {"input": "Qual foi o placar da final da Copa de 2002?", "output": "Brasil 2x0 Alemanha, com dois gols de Ronaldo Fenômeno."},
    {"input": "Quem é o maior artilheiro da história das Copas do Mundo?", "output": "Miroslav Klose, com 16 gols."},
    {"input": "Quantos jogadores tem um time de futebol?", "output": "11 jogadores em campo por equipe."},

    # 🏛 Política
    {"input": "O que é democracia?", "output": "É um sistema de governo no qual o poder é exercido pelo povo, diretamente ou por representantes eleitos."},
    {"input": "O que é ditadura?", "output": "É um regime político onde o poder está concentrado em uma única pessoa ou grupo, sem participação popular."},
    {"input": "O que é esquerda e direita na política?", "output": "São espectros políticos: a esquerda defende igualdade social, enquanto a direita valoriza o livre mercado e a tradição."},
    {"input": "Quem faz as leis no Brasil?", "output": "O Congresso Nacional, composto pela Câmara dos Deputados e pelo Senado Federal."},
    {"input": "O que é um golpe de estado?", "output": "É uma tomada de poder, geralmente ilegal e abrupta, derrubando um governo."},
    {"input": "Quem foi o primeiro presidente do Brasil?", "output": "Deodoro da Fonseca."},
    {"input": "O que é um impeachment?", "output": "É um processo de remoção do presidente por crimes de responsabilidade."},
    {"input": "O que é voto obrigatório?", "output": "É quando a participação nas eleições é obrigatória por lei, como no Brasil."},
    {"input": "Qual a função do STF?", "output": "O Supremo Tribunal Federal julga questões constitucionais e garante o cumprimento da Constituição."},
    {"input": "O que é um parlamento?", "output": "É a instituição responsável por criar leis e fiscalizar o governo em países democráticos."},

    # 📜 História
    {"input": "O que foi a Revolução Francesa?", "output": "Um movimento que derrubou a monarquia francesa em 1789, influenciando o mundo com ideais de liberdade e igualdade."},
    {"input": "Quem foi Napoleão Bonaparte?", "output": "Foi um líder militar e imperador francês que conquistou grande parte da Europa no século XIX."},
    {"input": "Quem descobriu o Brasil?", "output": "Pedro Álvares Cabral, em 1500."},
    {"input": "O que foi a Segunda Guerra Mundial?", "output": "Um conflito global entre 1939 e 1945, envolvendo grandes potências como Alemanha, EUA e União Soviética."},
    {"input": "O que foi a Guerra Fria?", "output": "Foi um período de tensão entre EUA e União Soviética, sem confrontos diretos, mas com disputas políticas e ideológicas."},
    {"input": "O que foi o Holocausto?", "output": "O extermínio de milhões de judeus e outras minorias pelo regime nazista de Adolf Hitler durante a Segunda Guerra Mundial."},
    {"input": "Quem foi Getúlio Vargas?", "output": "Foi presidente do Brasil em dois períodos e responsável por grandes mudanças políticas e sociais."},
    {"input": "O que foi o feudalismo?", "output": "Um sistema econômico e social da Idade Média baseado em terras e servidão."},
    {"input": "Quem foi Dom Pedro I?", "output": "O primeiro imperador do Brasil, responsável pela independência do país em 1822."},
    {"input": "O que foi a Revolução Industrial?", "output": "Uma transformação econômica e tecnológica no século XVIII, com avanços na produção e urbanização."},

    # 🌍 Geografia
    {"input": "Qual é o maior país do mundo?", "output": "A Rússia, com o maior território do planeta."},
    {"input": "Qual é o menor país do mundo?", "output": "O Vaticano, com menos de 1 km²."},
    {"input": "Quantos continentes existem?", "output": "Seis: África, América, Antártica, Ásia, Europa e Oceania."},
    {"input": "Qual é o maior oceano?", "output": "O Oceano Pacífico, cobrindo um terço da Terra."},
    {"input": "Qual é o rio mais longo do mundo?", "output": "O Rio Nilo, na África."},
    {"input": "Qual é a montanha mais alta do mundo?", "output": "O Monte Everest, com 8.848 metros de altitude."},
    {"input": "Qual é a capital do Brasil?", "output": "Brasília."},
    {"input": "Qual é o deserto mais seco do mundo?", "output": "O Deserto do Atacama, no Chile."},
    {"input": "Qual país tem mais habitantes?", "output": "A China, seguida pela Índia."},
    {"input": "O que é um bioma?", "output": "Uma grande área com características climáticas, fauna e flora específicas, como a Amazônia e o Cerrado."},
    {"input": "O que é longitude?", "output": "É a medida da posição leste-oeste de um ponto na Terra."},
    {"input": "O que é latitude?", "output": "É a medida da posição norte-sul de um ponto na Terra."},
    {"input": "Quais são as zonas climáticas do planeta?", "output": "Tropical, temperada e polar."},
    {"input": "O que é um vulcão?", "output": "Uma estrutura geológica que libera lava, cinzas e gases do interior da Terra."},
    {"input": "O que é um terremoto?", "output": "Um tremor da crosta terrestre causado pelo movimento das placas tectônicas."},
    {"input": "O que são placas tectônicas?", "output": "São grandes blocos que formam a superfície da Terra e se movem lentamente."},
    {"input": "O que é um mapa topográfico?", "output": "Um mapa que representa a elevação do terreno através de curvas de nível."},
    {"input": "O que é o Círculo Polar Ártico?", "output": "É a linha imaginária que marca a região fria do Hemisfério Norte."},
    {"input": "O que é o Trópico de Capricórnio?", "output": "Uma linha imaginária ao sul do Equador que define zonas climáticas."}

]

# Criar vocabulário
all_words = []
for pair in treinamento:
    all_words.extend(word_tokenize(pair["input"].lower()))
    all_words.extend(word_tokenize(pair["output"].lower()))

all_words = sorted(set(all_words))  # Remove palavras duplicadas

# Mapear palavras para índices
word_to_idx = {word: i+1 for i, word in enumerate(all_words)}  # Índices começam em 1 (0 será token desconhecido)
word_to_idx["<UNK>"] = 0  # Token para palavras desconhecidas

# Criar mapeamento das respostas para índices
respostas_para_idx = {pair["output"]: i for i, pair in enumerate(treinamento)}
idx_para_respostas = {i: pair["output"] for i, pair in enumerate(treinamento)}

# Função para converter texto em tensor de índices
def texto_para_tensor(texto):
    tokens = word_tokenize(texto.lower())
    return torch.tensor([word_to_idx.get(word, 0) for word in tokens], dtype=torch.long)

# Criar os dados de treinamento
dados_treinamento = [(texto_para_tensor(pair["input"]), respostas_para_idx[pair["output"]]) for pair in treinamento]

# Criar o modelo
class SimpleChatbot(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, output_size):
        super(SimpleChatbot, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
        out = self.fc(hidden[-1])
        return out

# Configuração do modelo
vocab_size = len(word_to_idx)
embed_size = 10
hidden_size = 20
output_size = len(treinamento)

modelo = SimpleChatbot(vocab_size, embed_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(modelo.parameters(), lr=0.01)

# Treinamento
for epoch in range(100):
    total_loss = 0
    for input_tensor, target_idx in dados_treinamento:
        optimizer.zero_grad()
        output = modelo(input_tensor.unsqueeze(0))
        loss = criterion(output, torch.tensor([target_idx], dtype=torch.long))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    print(f"Época {epoch + 1}, Loss: {total_loss / len(dados_treinamento)}")

print("Treinamento concluído!")

# Teste do chatbot
def chatbot_responder(pergunta):
    tensor_input = texto_para_tensor(pergunta)
    output = modelo(tensor_input.unsqueeze(0))
    resposta_idx = torch.argmax(output).item()
    return idx_para_respostas.get(resposta_idx, "Desculpe, não entendi.")

# Exemplo de uso
print(chatbot_responder("Oi, tudo bem?"))

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais!")
        break
    resposta = chatbot_responder(pergunta)
    print(f"Chatbot: {resposta}")
