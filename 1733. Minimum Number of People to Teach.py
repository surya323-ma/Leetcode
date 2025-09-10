On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.
You are given an integer n, an array languages, and an array friendships where:
There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
from collections import defaultdict
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = [set(langs) for langs in languages]
        intervention_set = set()

        # Step 1: Identify friendships that can't communicate
        for u, v in friendships:
            u -= 1
            v -= 1
            if not user_langs[u].intersection(user_langs[v]):
                intervention_set.add(u)
                intervention_set.add(v)

        # Step 2: Count how many users in intervention_set know each language
        lang_count = defaultdict(int)
        for user in intervention_set:
            for lang in user_langs[user]:
                lang_count[lang] += 1

        # Step 3: Find the language that minimizes teaching
        min_teachings = float('inf')
        for lang in range(1, n + 1):
            teach_count = len(intervention_set) - lang_count.get(lang, 0)
            min_teachings = min(min_teachings, teach_count)

        return min_teachings
