Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
You are given a string word, which represents the final output displayed on Alice's screen.
Return the total number of possible original strings that Alice might have intended to type.
  # ccde here 

 class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        cnt = 0
        ans = 0

        i = 0

        while i < len(word):
            j = i
            while i < len(word) and word[j] == word[i]: i+=1
            ans += (i-j) if i-j > 1 else 0
            cnt += 1 if i-j > 1 else 0

        return ans - (cnt-1)
                
