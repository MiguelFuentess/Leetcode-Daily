"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.valid_expressions = set()
        self.min_removed = float('inf')

        def recurse(index, left_count, right_count, expr, removed_count):
            if index == len(s):
                if left_count == right_count:
                    if removed_count < self.min_removed:
                        self.valid_expressions.clear()
                        self.min_removed = removed_count
                    if removed_count == self.min_removed:
                        self.valid_expressions.add(expr)
                return

            char = s[index]
            if char not in ['(', ')']:
                recurse(index + 1, left_count, right_count, expr + char, removed_count)
            else:
                recurse(index + 1, left_count, right_count, expr, removed_count + 1)
                if char == '(':
                    recurse(index + 1, left_count + 1, right_count, expr + char, removed_count)
                elif char == ')' and left_count > right_count:
                    recurse(index + 1, left_count, right_count + 1, expr + char, removed_count)

        recurse(0, 0, 0, "", 0)
        return list(self.valid_expressions)