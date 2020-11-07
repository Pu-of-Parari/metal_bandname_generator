import numpy as np
import random
import re
from collections import defaultdict
import pprint

def make_by_word(seed_word, num_word, init_dict):
    """指定した単語を使って生成"""
    result_words = [seed_word]
    seed_word = seed_word.lower()
    for i in range(num_word-1):
        chosen_word = random.choice(tokenized_text)
        result_words.append(chosen_word)

    bandname = result_words
    if "the" in bandname or "The" in bandname:
        for i, res in enumerate(result_words):
            if res.lower() == "the":
                bandname[0], bandname[i] = bandname[i], bandname[0]
    else:
        random.shuffle(bandname)

    print(" ".join(bandname))

def make_by_initial_name(seed, init_dict):
    """指定したイニシャルを基に生成"""
    seed = seed.lower()
    result_words = []
    for initial in seed:
        #print(initial)
        #print(init_dict[initial])
        choices = init_dict[initial]
        chosen_word = random.choice(choices)
        result_words.append(chosen_word.capitalize())

    print(" ".join(result_words))

def walk_graph(seed, graph, distance=5, start_node=None):
    """単語数を指定してマルコフ連鎖を用いて生成"""
    if distance <= 0:
        return []
    #print(seed)
    # If not given, pick a start node at random.
    if not start_node:
        start_node = random.choice(list(graph.keys()))


    weights = np.array(
        list(markov_graph[start_node].values()),
        dtype=np.float64)
    # Normalize word counts to sum to 1.
    weights /= weights.sum()

    # Pick a destination using weighted distribution.
    choices = list(markov_graph[start_node].keys())
    #print(choices)

    chosen_word = np.random.choice(choices, None, p=weights)

    result_words = [chosen_word] + walk_graph(seed,
        graph, distance=distance-1,
        start_node=chosen_word)

    return result_words


if __name__ == '__main__':
    # preprocess
    ## Read text from file and tokenize.
    path = './band_list/band_list.txt'

    with open(path) as f:
      text = f.read()
    #print(text)
    tokenized_text = [
        word
        for word in re.split('\W+', text)
        if word != ''
    ]

    init_dict = defaultdict(list)
    for word in set(tokenized_text):
      word_ = word.lower()
      init_dict[word_[0]].append(word_)

    ## Create graph.
    markov_graph = defaultdict(lambda: defaultdict(int))

    last_word = tokenized_text[0].lower()
    for word in tokenized_text[1:]:
        word = word.lower()
        markov_graph[last_word][word] += 1
        last_word = word


    # main process
    print("""\
    mode:
    1: generate the words you want to use and the num of words you set(e.g. bring 4)
    2: set the acronym you want to use(e.g. BMTH)
    3: set hte word count and generate a Markov chain model(e.g. 4)""")
    mode = int(input("mode? >> "))

    if mode == 1:
        seed = input("seed? >> ")
        num_word = int(input("word num? >> "))
        print("--------------------------")
        for i in range(10):
            make_by_word(seed, num_word, init_dict)

    elif mode == 2:
        seed = input("initial? >> ")
        print("--------------------------")
        for i in range(10):
            make_by_initial_name(seed, init_dict)

    else:
        seed = int(input("word num? >> "))
        print("--------------------------")
        for i in range(10):
            #print(' '.join(walk_graph(
            #      markov_graph, distance=len(seed))), '\n')
            count = 0
            res = walk_graph(seed, markov_graph, distance=seed)
            print(" ".join(res))
