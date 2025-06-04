You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
All the split words are put into a box.
Find the lexicographically largest string from the box after all the rounds are finished.
#code here
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word

        n = len(word)
        length = n - numFriends + 1
        max_char = max(word)
        result = ""

        for i in range(n):
            if word[i] == max_char:
                substr = word[i:i + length]
                result = max(result, substr)

        return result
