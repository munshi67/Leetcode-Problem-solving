class Solution:
    def removeDuplicates(self, nums):
        k = 0  # Pointer for unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1

# Example usage:
nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)           # Output: 5
print(nums[:k])    # Output: [0, 1, 2, 3, 4]