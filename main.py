# the following function converts a roman numeral to an integer
# parameters s : a string containing the romain numeral
# return - an integer signifying the value of the numeral
# author - Ashwin Rachha
# text editor - atom

class Solution:
    def romanToInt(self, s: str) -> int:

        singles = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        result = 0

        for c in s:

            result += singles[c]

        return result
