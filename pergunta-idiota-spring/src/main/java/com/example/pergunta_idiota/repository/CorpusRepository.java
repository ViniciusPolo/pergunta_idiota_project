package com.example.pergunta_idiota.repository;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.pergunta_idiota.model.Corpus;

@Repository
public interface CorpusRepository extends JpaRepository<Corpus, Long> {
}
