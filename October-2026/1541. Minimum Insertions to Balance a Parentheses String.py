"""
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insertions = left_count = index = 0
        while index < length:
            if s[index] == "(":
                left_count += 1; index += 1
            else:
                if left_count > 0: left_count -= 1
                else: insertions += 1
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insertions += 1; index += 1
        insertions += left_count * 2
        return insertions