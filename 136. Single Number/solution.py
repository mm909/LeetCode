# Solution -> XOR!


class Solution:
    # 3n time but n space
    def singleNumber3n2n(self, nums: List[int]) -> int:
        hash = {}
        for i, num0 in enumerate(nums):
                hash[num0] = 0
        for i, num1 in enumerate(nums):
            hash[num1] += 1
        for i, num2 in enumerate(nums):
            if hash[num2] == 1:
                return num2

    # n^2 time
    def singleNumbern2(self, nums: List[int]) -> int:
        for i, num1 in enumerate(nums):
            single = True
            for j, num2 in enumerate(nums):
                if i != j:
                    if num1 == num2:
                        single = False
            if single:
                return num1

class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
