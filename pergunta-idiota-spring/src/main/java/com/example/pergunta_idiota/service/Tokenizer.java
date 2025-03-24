package com.example.pergunta_idiota.service;

import java.text.Normalizer;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.regex.Pattern;

import org.springframework.stereotype.Service;

import com.example.pergunta_idiota.model.Tokens;
import com.example.pergunta_idiota.repository.TokensRepository;

@Service
public class Tokenizer {
    private static final Pattern PONTUACAO = Pattern.compile("\\p{Punct}"); // Remove pontuação
    private final TokensRepository tokensRepository;

    public Tokenizer(TokensRepository tokensRepository) {
        this.tokensRepository = tokensRepository;
    }

    public List<Tokens> getCorpusTokens () {
        return tokensRepository.findAll();
    }

    public List<Tokens> tokenizeAndSave(String texto) {
        texto = Normalizer.normalize(texto, Normalizer.Form.NFD) // Remove acentos
                .replaceAll("[^\\p{ASCII}]", ""); // Mantém apenas caracteres ASCII

        texto = PONTUACAO.matcher(texto).replaceAll(""); // Remove pontuação
        texto = texto.toLowerCase(); // Converte para minúsculas

        String[] palavras = texto.split("\\s+"); // Divide por espaços
        List<Tokens> tokensList = new ArrayList<>();

        for (String palavra : palavras) {
            if (!palavra.isBlank()) { // Evita espaços extras
                Tokens token = new Tokens();
                token.setText(palavra);
                token.setPos_tag("N/A"); // Ajuste para definir a POS-tag corretamente
                token.setLema(palavra); // Pode ser ajustado para usar um lematizador real
                token.setCreatedAt(new Date());

                tokensList.add(token);
            }
        }

        return tokensRepository.saveAll(tokensList); // Salva todos os tokens no banco de dados
    }
}
