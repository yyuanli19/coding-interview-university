
"""
    my own solution
    Runtime: 172 ms, faster than 38.90% of Python3 online submissions for Majority Element.
    Memory Usage: 15.6 MB, less than 33.92% of Python3 online submissions for Majority Element.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
                if dic[i] > len(nums)//2:
                    return i

"""
    found solution based on moore vote algorithm
    Runtime: 168 ms, faster than 51.78% of Python3 online submissions for Majority Element.
    Memory Usage: 15.5 MB, less than 57.94% of Python3 online submissions for Majority Element.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        major, count = nums[0], 1
        for i in nums[1:]:
            if count == 0:
                count += 1
                major = i
            elif major == i:
                count += 1
            else:
                count -= 1
        return major
