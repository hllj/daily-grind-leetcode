// https://leetcode.com/problems/count-of-smaller-numbers-after-self

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = list(enumerate(nums))
        count = [0 for _ in range(n)]
        def merge(nums, left, right):
            mid = (left + right) // 2
            tmp = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if nums[i][1] <= nums[j][1]:
                    tmp.append(nums[j])
                    j += 1
                else:
                    count[nums[i][0]] += right - j + 1
                    tmp.append(nums[i])
                    i += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1
            while j <= right:
                tmp.append(nums[j])
                j += 1
            for x in range(left, right + 1):
                nums[x] = tmp[x - left]
        
        def mergeSort(nums, left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, right)
        
        mergeSort(nums, 0, n - 1)
        return count