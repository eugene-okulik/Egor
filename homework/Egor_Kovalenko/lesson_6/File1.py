text = \
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
    Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
new_text = ''
for word in words:
    punctuation = ''
    if word[-1] in [',', '.']:
        punctuation = word[-1]
        word = word[:-1]

    if len(word) >= 2:
        word += 'ing'

    word += punctuation
    new_text += word + ' '
print(new_text)
