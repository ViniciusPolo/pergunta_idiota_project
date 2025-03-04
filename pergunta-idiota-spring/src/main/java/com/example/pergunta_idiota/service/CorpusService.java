package com.example.pergunta_idiota.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.pergunta_idiota.model.Corpus;
import com.example.pergunta_idiota.repository.CorpusRepository;

@Service
public class CorpusService {
  private final CorpusRepository corpusRepository;

  public CorpusService(CorpusRepository corpusRepository) {
    this.corpusRepository = corpusRepository;
  }

  public List<Corpus> getCorpus() {
    return corpusRepository.findAll();
  }

  public Corpus getCorpusById(Long id) {
    return corpusRepository.findById(id).orElse(null);
  }

  public Corpus createCorpus(Corpus corpus) {
    return corpusRepository.save(corpus);
  }

}
