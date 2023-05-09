import re

from functions import (
    replace_last,
    m_Prefix,
    p_Prefix,
    di_Prefix,
    ke_Prefix,
    ter_Prefix,
    ber_Prefix,
    b_Prefix,
    Suffix,
    Verify,
)

# Read stop words from file
with open("stopwords.txt", "r", encoding="utf-8") as f:
    stop_words = [word.strip() for word in f.readlines()]

# Main function to stem Malay words
def malaystemmer(text):
    if text.startswith("pe"):
        stemmedword = p_Prefix(text)
    elif text.startswith("me"):
        stemmedword = m_Prefix(text)
    elif text.startswith("be"):
        stemmedword = b_Prefix(text)
    elif text.startswith("di"):
        stemmedword = di_Prefix(text)
    elif text.startswith("ke"):
        stemmedword = ke_Prefix(text)
    elif text.startswith("ter"):
        stemmedword = ter_Prefix(text)
    elif text.startswith("ber"):
        stemmedword = ber_Prefix(text)
    else:
        stemmedword = p_Prefix(text)

    return stemmedword



# Tokenize the input text into words
def tokenize(text):
    return text.split()


# Stem each word in the list of words and join them back into a sentence
def stem_sentence(sentence):
    words = tokenize(sentence)
    stemmed_words = []
    for word in words:
        if word.endswith("lah"):
            stemmed_word = malaystemmer(word[:-3])
        elif word.endswith("kah"):
            stemmed_word = malaystemmer(word[:-3])
        else:
            stemmed_word = malaystemmer(word)
        stemmed_words.append(stemmed_word)
    return " ".join(stemmed_words)


# Get user input
input_text = input("Enter Malay text to be stemmed: ")

# Remove emojis and convert to lowercase
input_text = input_text.encode("ascii", "ignore").decode("ascii").lower()

# Remove punctuations
input_text = re.sub(r"[^\w\s]", "", input_text)

# Remove stop words
input_text = " ".join([word for word in input_text.split() if word not in stop_words])

# Stem the input text
stemmed_text = stem_sentence(input_text)

# Print output
print("Stemmed text: ", stemmed_text)
