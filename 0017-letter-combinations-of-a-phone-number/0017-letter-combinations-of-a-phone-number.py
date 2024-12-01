class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def backtrack(index, path):
            print(f"Backtracking at index {index} with path: {''.join(path)}")
            if index == len(digits):
                combinations.append("".join(path))
                print(f"Combination added: {''.join(path)}")
                return
            possible_letters = phone_map[digits[index]]
            print(f"Possible letters for digit '{digits[index]}': {possible_letters}") 
            
            for letter in possible_letters:
                print(f"Choosing letter: {letter}")  # Debug
                path.append(letter)  # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()  # Unchoose
                print(f"Backtracked path: {''.join(path)}")  # Debug

        combinations = []
        backtrack(0, [])
        return combinations