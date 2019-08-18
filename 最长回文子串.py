class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s)<=0:
            return ""
        start=0
        end=0
        max_len=""
        for i in range(0,len(s)):
            len1=0
            len2=0
            # i为中心点
            left1=i
            right1=i
            while left1>=0 and right1<len(s) and s[left1]==s[right1]:
                left1-=1
                right1+=1
            len1=right1-left1-1
            # i和i+1的中间为对称点
            left2=i
            right2=i+1
            while left2>=0 and right2<len(s) and s[left2]==s[right2]:
                left2-=1
                right2+=1
            len2=right2-left2-1
            
            if len(max_len)<len1 or len(max_len)<len2:
                if len1<len2:
                    max_len=s[left2+1:right2]
                else:
                    max_len=s[left1+1:right1]
                    
        return max_len