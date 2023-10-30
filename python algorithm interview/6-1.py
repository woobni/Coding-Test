def isPalindrome(s: str) -> bool:
    s = s.lower()
    return s==s[::-1] 