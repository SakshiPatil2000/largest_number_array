class Solution:
    def largestNumberFromList(self, nums:list[int]) -> int :
        largest =nums[0]
        
        for number in nums:
            if number > largest :
                largest =number
        return largest
        
        
 #Take user input
 
nums = list(map(int, input("Enter numbers separated by space: ").split())) 
 
sol = Solution()
 
result = sol.largestNumberFromList(nums)
 
print(result)    