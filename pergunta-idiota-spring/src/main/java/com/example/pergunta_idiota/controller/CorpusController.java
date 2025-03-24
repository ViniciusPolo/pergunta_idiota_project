package com.example.pergunta_idiota.controller;

import java.util.List;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.pergunta_idiota.model.Corpus;
import com.example.pergunta_idiota.model.Tokens;
import com.example.pergunta_idiota.service.CorpusService;
import com.example.pergunta_idiota.service.Tokenizer;

@RestController
@RequestMapping("/corpus")
public class CorpusController {
  private final CorpusService corpusService;
  private final Tokenizer tokenizer;
  
    public CorpusController(CorpusService corpusService, Tokenizer tokenizer) {
      this.corpusService = corpusService;
      this.tokenizer = tokenizer;
    }

  @GetMapping("/")
  @PreAuthorize("hasRole('USER')")
  public List<Corpus> getCorpus() {
    return corpusService.getCorpus();
  }

  @PostMapping("/")
  @PreAuthorize("hasRole('USER')")
  public Corpus createCorpus(@RequestBody Corpus corpus) {
      corpusService.createCorpus(corpus);
    
      String textoCorpus = corpus.getText(); // Certifique-se de que `getText()` existe
      tokenizer.tokenizeAndSave(textoCorpus); // Usa o método correto para tokenizar e salvar
    
      return corpusService.createCorpus(corpus);
  }
  
}
