def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    max_length = 0

    for word in words:
        word = word.strip('.,!?')
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return f"{longest_word} is the longest word"

sample_input = "Hai I'm Niranjan and Im from Nagercoil"
result = find_longest_word(sample_input)
print(result)