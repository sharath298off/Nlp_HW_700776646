CS5760 Natural Language Processing 
Spring 2026
Homework 1. 
Student name: sharath chandra seriyala
student id: 700776646



Q1. Regex

1) ZIP Codes:
Regex: \b\d{5}(?:[- ]\d{4})?\b
Comment: Matches 5-digit ZIP with optional space or hyphen +4 part.

2) Words not starting with capital:
Regex: \b(?![A-Z])[a-zA-Z]+(?:[-'][a-zA-Z]+)*\b
Comment: Negative lookahead blocks capital starts; allows apostrophes/hyphens.

3) Numbers with sign, commas, decimals, sci notation:
Regex: [+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?
Comment: Handles integers, decimals, commas, scientific notation.

4) Email variants:
Regex: (?i)\be(?:-|–|\s)?mail\b
Comment: Case-insensitive, accepts hyphen, en-dash, or space.

5) go, goo, gooo with punctuation:
Regex: \bgo+\b[!.,?]?
Comment: One or more 'o', optional punctuation.

6) Line ending with question + quotes/brackets:
Regex: \?["\)\]’”\s]*$
Comment: Anchors to line end allowing quotes/brackets.

------------------------------------------------------------

Q2. Manual BPE

Corpus:
low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

Initial vocab: l, o, w, e, s, t, n, r, i, d, _

Step 1 Merge: l o -> lo
Step 2 Merge: lo w -> low
Step 3 Merge: low _ -> low_

Explanation: Frequent pairs combine into common morphemes like low_ and er_.

Q2.2 Mini BPE Code (Python with comments)

from collections import Counter, defaultdict

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in v_in:
        new_word = word.replace(bigram, replacement)
        v_out[new_word] = v_in[word]
    return v_out

# Initial corpus with end-of-word marker
words = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new".split()
vocab = Counter([" ".join(list(w)) + " _" for w in words])

for i in range(3):
    pairs = get_stats(vocab)
    best = max(pairs, key=pairs.get)
    print("Best pair:", best)
    vocab = merge_vocab(best, vocab)
    print("Vocab size:", len(vocab))

Q2.2 Explanation (5–6 sentences):
Subwords help solve OOV because unknown words can be broken into known pieces.
For example, "newestest" becomes new + est + est.
This avoids unknown tokens.
The subword er_ matches English comparative/agent suffix.
This improves generalization.
BPE balances vocabulary size and coverage.

------------------------------------------------------------

Q2.3 English Paragraph BPE

Paragraph:
Natural language processing is fascinating. It allows computers to understand text. Tokenization is the first step. Subwords help generalize. Models learn patterns.

Five frequent merges: (example)
1) n a -> na
2) t i -> ti
3) i n -> in
4) e r_ -> er_
5) s _ -> s_

Five longest subwords: processing_, language_, tokenization_, computers_, understand_

Segmented words:
processing -> process + ing_
tokenization -> token + ization_
computers -> computer + s_
understand -> under + stand_
generalize -> general + ize_

Reflection:
BPE learned stems and suffixes.
It captured -ing_, -s_, -ize_.
Pros: handles rare words, reduces OOV.
Cons: subwords can break semantics.
It may split named entities oddly.
Longer merges may overfit small data.

------------------------------------------------------------

Q3. Bayes Rule

P(c): Prior probability of class.
P(d|c): Likelihood of document given class.
P(c|d): Posterior probability of class given document.
P(d) is constant for all classes, so ignored in argmax.

------------------------------------------------------------

Q4. Add-1 Smoothing

Denominator = total tokens + vocab size = 14 + 20 = 34

P(predictable|-):
(2 + 1) / 34 = 3/34

P(fun|-):
(0 + 1) / 34 = 1/34

------------------------------------------------------------

Q5. Tokenization

Paragraph:
I can't believe it's not butter! NLP tools handle punctuation well. Tokenization is tricky sometimes.

Naive tokens:
I, can't, believe, it's, not, butter!, NLP, tools, handle, punctuation, well., Tokenization, is, tricky, sometimes.

Manual corrected tokens:
I, can, n't, believe, it, 's, not, butter, !, NLP, tools, handle, punctuation, well, ., Tokenization, is, tricky, sometimes, .

Tool (spaCy) output similar to manual.

MWEs:
New York, natural language processing, machine learning

Reflection:
Tokenization is hard due to punctuation and contractions.
English contractions split into clitics.
MWEs should be single tokens.
Punctuation causes boundary issues.
Morphology affects token boundaries.

