class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        odd=[]
        even=[]
        for i in nums:
            if i %2==0:
                even.append(i)
            else: odd.append(i)
        return even+odd
        
