def popular_words (text, words):
    splitted = text.lower().split(" ")
    count_words = {}
    for word in words:
        count_words[word] = 0

    for item in splitted:
        if item in count_words:
            count_words[item] += 1
    print(count_words)
    return count_words
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

