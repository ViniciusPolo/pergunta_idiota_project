package com.example.pergunta_idiota.model;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "corpus")
public class Corpus {
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "title", nullable = false)
  private String title;
  @Column(name = "text", nullable = false, length = 2000)
  private String text;
  @Column(name = "language", nullable = true)
  private String language;
  @Column(name = "font", nullable = true)
  private String font;
  @OneToMany(mappedBy = "corpus", cascade = CascadeType.ALL, orphanRemoval = true)
  private List<Occurrences> occurrences;
  @Temporal(TemporalType.TIMESTAMP)
  @Column(name = "created_at", nullable = false, updatable = false)
  private Date createdAt = new Date();  // Auto-set timestamp
}
