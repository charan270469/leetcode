class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        while True:
            sorted_array = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    sorted_array = False
                    break

            if sorted_array:
                return ops

            min_sum = nums[0]+nums[1]
            idx = 0

            for i in range(1,len(nums)-1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    idx = i
                
            nums[idx] += nums[idx+1]
            nums.pop(idx+1)
            ops+=1

            