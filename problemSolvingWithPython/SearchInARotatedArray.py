## https://leetcode.com/problems/search-in-rotated-sorted-array/
#iterative solution
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
        

# recursive solution
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        return self.find( nums, target, 0 , (len(nums)-1))
        

    def find(self, nums: List[int], target:int , start:int , end:int) -> int:
        if start>end:
            return -1
        
        mid = int((start + end)/2)
        if nums[mid] == target:
            return mid
        
        if nums[start]<=nums[mid]:
            if target<=nums[mid] and target>= nums[start]:
                return self.find(nums, target, start, mid-1)
            return self.find(nums, target, mid+1, end)
        
        if target>= nums[mid] and target <= nums[end]:
            return self.find(nums, target, mid+1, end)
        return self.find(nums, target, start, mid-1)
