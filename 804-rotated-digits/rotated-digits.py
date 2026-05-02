class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_same = {'0', '1', '8'}
        valid_diff = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_good = False
            
            for ch in s:
                if ch in valid_diff:
                    is_good = True
                elif ch not in valid_same:
                    is_good = False
                    break
            
            if is_good:
                count += 1
        
        return count
        