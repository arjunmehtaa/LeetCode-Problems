class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
        res = []
        
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            s = letters[digits[i]]
            for char in s:
                backtrack(i + 1, currStr + char)
                
        if digits:
            backtrack(0, "")
            
        return res