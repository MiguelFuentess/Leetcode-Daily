"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
Example 4:

Input: s = "("
Output: false
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        d = 0
        for i in range(n):
            if s[i] in '(*': 
                d += 1
            else: 
                d -= 1
            if d < 0: 
                return False

        d = 0
        for i in range(n - 1, -1, -1):
            if s[i] in ')*': 
                d += 1
            else:
                d -= 1
            if d < 0: 
                return False

        return True