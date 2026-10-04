""Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:
For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.""

 class Solution:
    def braceExpansionII(self, expr: str) -> list[str]:
        def expand(e):
            stack = [set([""])]
            i = 0
            while i < len(e):
                if e[i].isalpha():
                    j = i
                    while j < len(e) and e[j].isalpha(): j += 1
                    word = {e[i:j]}
                    stack[-1] = {a+b for a in stack[-1] for b in word}
                    i = j
                elif e[i] == '{':
                    bal, j = 1, i+1
                    while bal:
                        if e[j] == '{': bal += 1
                        elif e[j] == '}': bal -= 1
                        j += 1
                    sub = expand(e[i+1:j-1])
                    stack[-1] = {a+b for a in stack[-1] for b in sub}
                    i = j
                elif e[i] == ',':
                    stack.append(set([""]))
                    i += 1
                else:
                    i += 1
            res = stack[0]
            for s in stack[1:]:
                res |= s
            return res
        return sorted(expand(expr))
