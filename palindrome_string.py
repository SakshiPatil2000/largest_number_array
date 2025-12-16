class PalindromeString:
    def checkStringpalindrome(self, text:str) -> bool :
        start=0
        end=len(text)-1
        
        while start < end :
            if text[start] != text[end]:
                return False
            start += 1
            end   -= 1
            
        return True
    
palindromeString = PalindromeString()

word =input("Enter any word :")

print("Palindrome" if palindromeString.checkStringpalindrome(word.lower()) else "Not Palindrome")