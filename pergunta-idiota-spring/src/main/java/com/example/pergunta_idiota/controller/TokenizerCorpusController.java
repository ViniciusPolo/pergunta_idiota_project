package com.example.pergunta_idiota.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;

import com.example.pergunta_idiota.model.Tokens;
import com.example.pergunta_idiota.service.Tokenizer;



@RestController
@RequestMapping("/corpus-tokens")
public class TokenizerCorpusController {
  private final Tokenizer tokenizer;

  public TokenizerCorpusController(Tokenizer tokenizer) {
    this.tokenizer = tokenizer;
  }

    @GetMapping("/")
    @PreAuthorize("hasRole('USER')") // or use hasAuthority('USER') if roles are stored without "ROLE_" prefix
    public List<Tokens> getTokens() {
        return tokenizer.getCorpusTokens();
    }
}
