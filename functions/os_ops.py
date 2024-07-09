import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Define your sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Process the sentence using SpaCy
doc = nlp(sentence)

# Print the context of each word in the sentence
for token in doc:
    print(f"Word: {token.text}, Context: {token.sent}")