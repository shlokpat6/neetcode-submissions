class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i,j in enumerate(nums):
            if j != val:
                nums[k] = nums[i]
                k +=1
        return k