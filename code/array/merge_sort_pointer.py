"""
    Runtime: 36 ms, faster than 66.29% of Python3 online submissions for Merge Sorted Array.
    Memory Usage: 14.4 MB, less than 18.71% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            nums1[:] = nums2[:]
        else:
            s1, s2 = 0, 0
            while s1 < m+n and s2<n:
                if s1==m:
                    nums1[s1:] = nums2[s2:]
                    break

                if nums1[s1] > nums2[s2]:
                    nums1[s1+1:] = nums1[s1:-1]
                    nums1[s1] = nums2[s2]
                    s2 += 1
                    m+=1
                s1 += 1


"""
    cleaner answear found online
    Runtime: 40 ms, faster than 28.78% of Python3 online submissions for Merge Sorted Array.
    Memory Usage: 14.1 MB, less than 93.02% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
