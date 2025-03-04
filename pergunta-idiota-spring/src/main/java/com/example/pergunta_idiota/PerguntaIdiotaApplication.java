package com.example.pergunta_idiota;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = "com.example.pergunta_idiota")
public class PerguntaIdiotaApplication {
    public static void main(String[] args) {
        SpringApplication.run(PerguntaIdiotaApplication.class, args);
    }
}
