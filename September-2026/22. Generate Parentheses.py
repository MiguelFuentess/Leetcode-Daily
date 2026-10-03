"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(current_str, open_count, closed_count):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, closed_count)
                
            if closed_count < open_count:
                backtrack(current_str + ")", open_count, closed_count + 1)
                
        backtrack("", 0, 0)
        return res