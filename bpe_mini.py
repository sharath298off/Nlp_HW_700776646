from collections import Counter, defaultdict

def get_stats(vocab):
    """Count bigram frequencies across the vocabulary."""
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, v_in):
    """Merge a selected bigram in the vocabulary."""
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in v_in:
        new_word = word.replace(bigram, replacement)
        v_out[new_word] = v_in[word]
    return v_out

def main():
    # Toy corpus with end-of-word marker
    corpus = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new".split()
    vocab = Counter([" ".join(list(w)) + " _" for w in corpus])

    num_merges = 10  # you can increase this
    print("Initial vocab size:", len(vocab))

    for i in range(num_merges):
        pairs = get_stats(vocab)
        best = max(pairs, key=pairs.get)
        print(f"Step {i+1} | Best pair: {best} | Count: {pairs[best]}")
        vocab = merge_vocab(best, vocab)
        print("Vocab size:", len(vocab))

    # Segment some words
    test_words = ["new", "newer", "lowest", "widest", "newestest"]
    print("\nSegmentation examples (final merges applied conceptually):")
    for w in test_words:
        print(w, "->", " ".join(list(w)) + " _")  # illustrative segmentation

if __name__ == "__main__":
    main()