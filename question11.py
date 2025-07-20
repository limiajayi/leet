class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def maxArea(height):
        if not height:
            return 0
        
        ptrLeft = 0
        ptrRight = len(height) - 1
        areas = []
        
        width = ptrRight - ptrLeft
        length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
        area = width * length
        
        areas.append(area)
        
        while ptrLeft < len(height) and ptrRight > 0:
            
            if ptrLeft == ptrRight:
                break
            
            if height[ptrLeft] < height[ptrLeft + 1]:
                ptrLeft += 1
                
            width = ptrRight - ptrLeft
            length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
            area = width * length
            areas.append(area)
            
            if height[ptrRight - 1] > height[ptrRight]:
                ptrRight -= 1
            
            width = ptrRight - ptrLeft
            length = height[ptrLeft] if height[ptrLeft] <= height[ptrRight] else height[ptrRight]
            area = width * length
            areas.append(area)
                
            if len(areas) > 5:
                if areas[len(areas) - 2] == areas[len(areas) - 1]:
                    break
            
        return areas
    
    def intToRoman(num):
        #Ctrl + [] to change indent
        
        dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,  "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        romans = ""
        
        
        for letter in dict:
            while num >= dict[letter]:
                
                romans += letter
                num -= dict[letter]
                
        return romans
    
    def longestCommonPrefix(strs):
        """Find the longest common prefix amongst an array of strings"""
        if not strs:
            #if the array is empty just return an empty string
            return ""
        
        #let the initial prefix be the first string
        prefix = strs[0]
        
        #from the second string till the last
        for i in range(1, len(strs)):
            
            current = strs[i] #current string being compared with the first
            equal = len(prefix) == len(current) #conditional that helps with the loop
            
            while equal == False or prefix != current: 
                #while the current string and prefix are not equal in length or prefix is not equal to the current string
                #reduce the longer string by 1 until they're equal in length and in value
                if len(prefix) > len(current):
                    prefix = prefix[:-1]
                else:
                    current = current[:-1]
                
                equal = len(prefix) == len(current)
        
        #return the longest common prefix
        return prefix
    
    def twoSum(nums, target):
        arrayOfArrays = []
    
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
        
                if (nums[i] + nums[j]) == target:
                    arrayOfArrays.append([nums[i], nums[j]])
                
        return arrayOfArrays
    
    def threeSum(nums):
        
        arrayOfArrays = []
        memory = []
        
        for i in range(len(nums)):
            
            if nums[i] not in memory:
                minus = nums[i] * -1
                new = nums[i+1:]
                targets = Solution.twoSum(new, minus)
                
                for j in range(len(targets)):
                    targets[j].append(nums[i])
                    arrayOfArrays.append(targets[j])
            
            memory.append(nums[i])
            
        
        return arrayOfArrays
    
    def letterCombinations(digits):
        
        if not digits:
            return []
    
        def helper(processed, up):
            if not up:
                return [processed]
        
            button = int(up[0])
            ans = []
            
            if 2 <= button <= 6:
                for i in range((button-2)*3, (button-1)*3):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 7:
                for i in range(15, 19):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 8:
                for i in range(19, 22):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            elif button == 9:
                for i in range(22, 26):
                    ch = chr(ord('a') + i)
                    ans += helper(processed + ch, up[1:])
            return ans

        return helper("", digits)