package com.example.pergunta_idiota.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.pergunta_idiota.model.Corpus;
import com.example.pergunta_idiota.service.CorpusService;

@RestController
@RequestMapping("/corpus")
public class CorpusController {
  private final CorpusService corpusService;
  
    public CorpusController(CorpusService corpusService) {
      this.corpusService = corpusService;
  }

  @GetMapping("/")
  public List<Corpus> getCorpus() {
    return corpusService.getCorpus();
  }

  @PostMapping("/")
  public Corpus createCorpus(@RequestBody Corpus corpus) {
    return corpusService.createCorpus(corpus);
  }

}
