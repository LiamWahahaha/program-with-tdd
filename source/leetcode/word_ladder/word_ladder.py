from collections import deque

class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        def validTransformation(beginWord, transformWord):
            diff = 0
            for char_b, char_t in zip(beginWord, transformWord):
                if char_b != char_t:
                    diff += 1
                if diff > 1:
                    return False
            return True

        queue = deque([(beginWord, 1)])
        word_dictionary = {word: True for word in wordList}

        if endWord not in word_dictionary:
            return 0

        while queue:
            begin, length = queue.pop()
            if begin == endWord:
                return length
            for key_word in word_dictionary:
                if validTransformation(begin, key_word):
                    word_dictionary[key_word] = False
                    queue.appendleft((key_word, length + 1))
            word_dictionary = dict(filter(lambda kv: kv[1], word_dictionary.items()))

        return 0
