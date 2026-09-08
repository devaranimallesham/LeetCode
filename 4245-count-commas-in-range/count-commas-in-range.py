class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for a in range(1, n + 1):
            if a > 999:
                res += 1
        return res