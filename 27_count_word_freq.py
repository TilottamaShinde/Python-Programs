# Count the frequency of each word in a string

def count_word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        word = word.strip(".,!?")       #Remove punctuation
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage
sentence = "Hello Wrold! Hello Python. Python is fun and Python is powerful."
word_freq = count_word_frequency(sentence)

print("Word Frequencies : ")
for word, count in word_freq.items():
    print(f"{word}: {count}")
