# Function to convert roman numeral to integer
# arameters : string indicating roman numeral
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

# the function converts an integer to a roman numeral
# param num - the number to be converted to a roman numeral
# return - string conataining the roman numeral
# author - Ashish Bhat
# text editor - visual studio code

def intToRoman(self, num: int) -> str: 
    # Dictionary containing mappings from integer to roman numeral
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for k in d:
        while num >= k:
            res += d[k]
            num -= k
    return res
            
       
