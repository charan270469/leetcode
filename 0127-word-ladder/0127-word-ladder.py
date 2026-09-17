class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        q = deque([(beginWord, 1)])
        s = set(wordList)

        if beginWord in wordList:
            s.remove(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                orginal = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + ch + word[i+1:]

                    if newword in s:
                        s.remove(newword)
                        q.append((newword, steps+1))
        return 0
