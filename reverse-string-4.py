# Q: Write a function that reverses a string inplace.
# INPUT:  ["h","e","l","l","o"] -
# OUTPUT: ["o","l","l","e","h"]
# IDEA:   1. Use 2 pointers, 1 pointing to index 0 (ptr1) and one pointing to index len(input)-1 (ptr2).
#         2. Swap values at 2 indexes.
#         3. Loop until ptr1 <= ptr2

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        t = ''
        i = 0
        j = n-1
        if n>1:
            while i<=j:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1