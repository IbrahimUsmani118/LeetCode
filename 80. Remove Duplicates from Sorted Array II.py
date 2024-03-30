# Solution to problem 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if length of nums in less than or equal to 2, it returns the length of the array nums
        if len(nums) <= 2:
            return len(nums)
        index = 2  # Pointer to track the position to update

        // For loop to initialize main logic
        for i in range(2, len(nums)):
            # if nums index i is not equal to its index 2 positions before, then nums[index] will be nums[i] and index will add 1 to its value
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        # returns index
        return index    
