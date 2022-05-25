
# lyrics is a LIST of words


lyrics = ['hello', 'world', 
    'beep', 'beep', 
    'foo', 'foo', 
    'python', 'python', 'python']

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict: 
            myDict[word] += 1
        else: 
            myDict[word] = 1
    return myDict

print('dict:', lyrics_to_frequencies(lyrics))


def most_common_words(freq): 
    values = freq.values()
    best = max(values)
    words = []
    for k in freq:
        if freq[k] == best:
            words.append(k)
    return (words, best) # return a tuple


common_words = lyrics_to_frequencies(lyrics)
print(common_words)
print('most:', most_common_words(common_words))


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(common_words, 2))