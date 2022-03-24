class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                c += 1
        
        if c == len(digits):
            digits.append(0)
            digits[0] = 1
        return digits
