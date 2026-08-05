class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]== nums[i-1]:
                continue
            target1 = target - nums[i]
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]== nums[j-1]:
                    continue
                target2 = target1 - nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum == target2:
                        ans.append([nums[i],nums[j], nums[left],nums[right]])
                        left +=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left+=1
                        while left < right and nums[right] == nums[right+1]:
                            right-=1
                    elif curr_sum < target2:
                        left+=1
                    else:
                        right-=1
                    
        return ans

