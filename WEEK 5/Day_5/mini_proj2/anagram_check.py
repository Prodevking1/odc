from itertools import permutations

class AnagramChecker():
    def __init__(self):
        with open('file.txt') as f:
            buff  = f.read().splitlines()
        self.word_list = [w.lower() for w in buff]

    def is_valid_word(self, word):
        if word in self.word_list:
            return True
        return False

    def get_anagrams(self, word):
        perms = [''.join(p) for p in permutations(word)]
        perms_set = set(perms) # get rid of duplicates
        anagrams = [term for term in perms_set if term in self.word_list]
        anagrams.remove(word)
        return anagrams
