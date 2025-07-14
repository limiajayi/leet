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
        array = []
    
        for i in range(0, len(nums) - 1):
        
            for j in range(i + 1, len(nums)):
        
                if (nums[i] + nums[j]) == target:
                    array.append([nums[i], nums[j]])
                
        return array
    
    def threeSum(nums):
        
        arrayOfArrays = []
        new = []
        
        for number in nums:
            
            nums.remove(number)
            minus = number * -1
            
            if len(Solution.twoSum(nums, minus)) != 0:
                
                targets = Solution.twoSum(nums, minus)
                
                for i in range(len(targets)):
                    targets[i].append(number)
                    arrayOfArrays.append(targets[i])
                    
            
            nums.append(number)
        
        for arrays in arrayOfArrays:
            if arrays not in new:
                new.append(arrays)
                
        return new
    
    

print(Solution.threeSum([-1,0,1,2,-1,-4]))