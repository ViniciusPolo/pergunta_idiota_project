import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import sys
import json
from transformers import pipeline

# Carregar modelo de linguagem
gerador_texto = pipeline("text-generation", model="gpt2", max_length=100)

def gerar_resposta_ia_local(mensagem):
    resposta = gerador_texto(mensagem, max_length=100, num_return_sequences=1)
    return resposta[0]["generated_text"]

if __name__ == "__main__":
    while True:
        try:
            user_input = sys.stdin.readline().strip()
            if not user_input:
                continue
            
            data = json.loads(user_input)  # Recebe JSON do Node.js
            response_text = gerar_resposta_ia_local(data["message"])

            resposta_json = json.dumps({"response": response_text})
            print(resposta_json)  # Enviar resposta
            sys.stdout.flush()  # Garantir envio imediato

        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
