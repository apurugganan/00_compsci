# RECURSION: PALINDROME
# divide and conquer algorithm

def isPalindrome(str):
    def cleanString(str):
        str = str.lower()
        newString = ''
        for c in str:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                newString = newString + c
        return newString
    
    def isPal(str):
        if len(str) <= 1:
            return True
        else: 
            return str[0] == str[-1] and isPal(str[1:-1])
    
    return isPal(cleanString(str))

print(isPalindrome('hello'))
print(isPalindrome('eevee'))