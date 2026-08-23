class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=s.split()
        c=""
        d=""
        for i in b:
            c+=i.lower()
        for i in c:
            if i.isalnum():
                d+=i
        return d==d[::-1]
       
        