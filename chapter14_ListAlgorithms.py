# find unknown words
# known_words = ['apple', 'tree', 'fish', 'river', 'boy', 'girl']
# book_words = "the apple fell from the tree to the river".split()

def find_unknown(known, exist):
    result = []
    for word in exist:
        if word not in known:
            result.append(word)
    return result

# print(find_unknown(known_words, book_words))

def load_words_from_file(filename):
    f = open(filename, 'r')
    file_content = f.read()
    f.close()
    lower = file_content.lower()
    nokomma = lower.replace(',',' ')              # 去掉文本中的各类符号
    nodoc = nokomma.replace('.', ' ')
    nodoubledoc = nodoc.replace('''"''',' ')
    noquestion = nodoubledoc.replace('?', ' ')
    nosurprise = noquestion.replace('!', ' ')
    wds = nosurprise.split()                      # 将文本分割
    return wds

# 导入小学的英文单词
primary_voc = load_words_from_file('words.txt')
print(len(primary_voc))
known_words = primary_voc[:]

# 导入故事的英文单词
story_voc = load_words_from_file('story.txt')
print(len(story_voc))
story_words = story_voc[:]

# 对比词汇
unknown_words = find_unknown(known_words,story_words)
print(unknown_words)

# 去掉重复的词汇
def clean(words):
    words.sort()
    t = words[-1]
    for i in range(len(words)-2,-1,-1):
        if t == words[i]:
            words.remove(words[i])
        else:
            t = words[i]
    return words

print(clean(unknown_words))

# binary search
def search_binary(xs,target):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:
            return -1

        mid_index = (lb+ub) // 2
        item_at_mid = xs[mid_index]
        
        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index