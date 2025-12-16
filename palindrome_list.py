class Palindrome:
    def checkPalindromeList(self, nums=list[int]) ->str :
        newNumList=nums.copy()
        newNumList.reverse()
        
        if nums == newNumList:
            return 'Nums is palindrome'
        else :
            return 'Nums is not palindrome'
     
     
palindrome =Palindrome()
nums =[1,2,3,2,1]

print(palindrome.checkPalindromeList(nums))