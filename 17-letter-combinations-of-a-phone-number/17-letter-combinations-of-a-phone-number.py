class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        answer = [""]
        letters = {
            2: "abc", 
            3: "def", 
            4: "ghi", 
            5: "jkl", 
            6: "mno", 
            7: "pqrs", 
            8: "tuv", 
            9: "wxyz"
        }
        for digit in digits:
            s = letters[int(digit)]
            sub = []
            while(len(answer)) > 0:
                pre = answer.pop()
                for char in s:
                    sub.append(pre + char)
            answer.extend(sub)
        return answer 
        