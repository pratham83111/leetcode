class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s=[]
        d=[]
        for i in range(len(nums)):
            if nums[i] != 0:
                s.append(nums[i])
        print(s)
        for j in range(len(nums)):
            if nums[j] == 0:
                d.append(nums[j])
        nums[:]= s+d