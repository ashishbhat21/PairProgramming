# Function to convert roman numeral to integer
# Parameters : string indicating roman numeral
# returns : integer conversion of roman numeral
# Author : Ashwin Rachha
# Text editor : atom

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

       
