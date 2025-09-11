Given a 0-indexed string s, permute s to get a new string t such that:
All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
Return the resulting string.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowel_positions = []
        vowel_chars = []
        for i, ch in enumerate(s):
            if ch in vowels:
                vowel_positions.append(i)
                vowel_chars.append(ch)
        vowel_chars.sort()
        t = list(s)
        for pos, ch in zip(vowel_positions, vowel_chars):
            t[pos] = ch
        return ''.join(t)
