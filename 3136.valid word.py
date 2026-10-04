A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for c in word:
            if not c.isalnum():  # Not alphanumeric
                return False

            if c.isalpha():
                lower = c.lower()
                if lower in 'aeiou':
                    has_vowel = True
                else:
                    has_consonant = True

            if has_vowel and has_consonant:
                continue

        return has_vowel and has_consonant
