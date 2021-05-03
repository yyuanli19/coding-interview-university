"""
quick sort
Runtime: 40 ms, faster than 7.97% of Python3 online submissions for Sort Colors.
Memory Usage: 14.3 MB, less than 11.00% of Python3 online submissions for Sort Colors.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        self.quick_sort(nums, 0, len(nums)-1)
        # print(nums)
    
    def quick_sort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quick_sort(nums, low, pi-1)
            self.quick_sort(nums, pi+1, high)
        # return nums
        
    def partition(self, nums, low, high):
        i = low -1
        pivot = nums[high]
        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if nums[j] <= pivot:
                # increment index of smaller element
                i = i+1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high] = nums[high], nums[i+1]
        return (i+1)
  
        
  
"""
Runtime: 32 ms, faster than 71.29% of Python3 online submissions for Sort Colors.
Memory Usage: 14.3 MB, less than 11.00% of Python3 online submissions for Sort Colors.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        nums[:red] = [0]*red
        nums[red:red+white] = [1]*white
        nums[red+white:] = [2]*blue
        
  
