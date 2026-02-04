# CS5760 -- Homework 1 (Natural Language Processing)

**Student:** Sharath Chandra Seriyala\
**Course:** CS5760 -- Natural Language Processing\
**Semester:** Spring 2026

## Contents

-   `Homework_1_Solutions.docx` -- Full written solutions with
    explanations.
-   `bpe_mini.py` -- Mini BPE learner for Q2.2 (well-commented).
-   `tokenization_q5.py` -- Tokenization comparison for Q5 (naive vs
    manual vs spaCy).
-   `README.md` -- This file.

## How to Run

### Q2.2 Mini BPE

``` bash
python bpe_mini.py
```

### Q5 Tokenization

``` bash
python tokenization_q5.py
```

> Note: `tokenization_q5.py` optionally uses spaCy. If spaCy is not
> installed:

``` bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Description

This repo contains solutions for Homework 1. The BPE script learns
merges on a toy corpus and prints the top pair at each step and evolving
vocabulary size. The tokenization script compares naive space-based
tokenization with a manual correction and a tokenizer tool output.

## Academic Integrity

This submission is for educational purposes and follows the course
submission requirements.
