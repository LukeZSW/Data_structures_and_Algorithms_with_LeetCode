class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        longestn = 0
        tempn = 0
        for i in range(len(s)):
            a = s[i]
            if a not in temp:
                temp.append(a)
                tempn += 1
                if tempn > longestn:
                    longestn = tempn
            else:
                indexrepeat = temp.index(a)
                temp.append(a)
                temp = temp[indexrepeat+1 : len(temp)]
                if tempn > longestn:
                    longestn = tempn
                tempn = len(temp)
        return longestn
        