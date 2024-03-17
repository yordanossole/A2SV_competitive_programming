class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverseNo = 0
        originalNo = x
        while x>0:
            reverseNo = reverseNo * 10 + x%10
            x//=10
    
        if originalNo == reverseNo:
            return True
        else:
            return False
